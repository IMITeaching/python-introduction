"""
Execute and then clear code and output from solutions notebooks.
"""
from collections.abc import MutableMapping
import glob
import os

import nbconvert.preprocessors as pre
import nbformat

website_dir = os.path.join("..", "website")
if not os.path.exists(website_dir):
    os.mkdir(website_dir)

source_dir = "../solutions/"
nb_files = glob.glob(os.path.join(source_dir, "*.ipynb"))

for nb_file in nb_files:
    print(f"Processing {nb_file}")
    nb = nbformat.read(nb_file, nbformat.NO_CONVERT)
    executed = pre.execute.executenb(nb, cwd=source_dir)
    print(f"Writing executed version of {nb_file}")
    nbformat.write(executed, nb_file, nbformat.NO_CONVERT)
    cop = pre.ClearOutputPreprocessor()
    nb, _ = cop.preprocess(executed, {})

    for cell in nb["cells"]:
        if isinstance(cell, MutableMapping):
            if (
                "cell_type" not in cell
                or cell["cell_type"] != "code"
                or "# Setup" in cell["source"]
            ):
                continue
            cell["source"] = ""
            if "metadata" in cell and "pycharm" in cell["metadata"]:
                del cell["metadata"]["pycharm"]
    _, base = os.path.split(nb_file)
    out = os.path.abspath(os.path.join("..", base))
    print(f"Writing clean version to {out}")
    nbformat.write(nb, out, nbformat.NO_CONVERT)

    # Prepare for website
    slug, _ = os.path.splitext(base)
    title = slug.capitalize().replace("-", " ")
    nikola = {
        "category": "teaching",
        "date": "2019-09-04 17:18:32 UTC+01:00",
        "description": "",
        "link": "",
        "slug": slug,
        "tags": "",
        "title": title,
        "type": "text",
    }
    nb["metadata"]["nikola"] = nikola
    for cell in nb["cells"]:
        if isinstance(cell, MutableMapping) and cell["cell_type"] == "markdown":
            source = cell["source"]
            source = source.replace("(images/", "(/images/teaching/python/course/")
            cell["source"] = source
    out = os.path.abspath(os.path.join(website_dir, base))
    print(f"Writing website version to {out}")
    nbformat.write(nb, out, nbformat.NO_CONVERT)
