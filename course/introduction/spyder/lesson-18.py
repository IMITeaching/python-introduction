#!/usr/bin/env python
# coding: utf-8

#%%
# # Logic and Loops
# 
# This lesson covers:
# 
# * Mixing logic and loops 

#%%
# Setup: Load the momentum data

import pandas as pd

momentum = pd.read_csv("data/momentum.csv", index_col="date", parse_dates=True)

mom_01 = momentum.mom_01
print(momentum.head())


#%%
# ## Problem: Logical Statements and for Loops
# Use a for loop along with an `if` statement to simulate an asymmetric random
# walk of the form 
# 
# $$y_{i}=y_{i-1}+e_{i}+I_{[e_{i}<0]}e_{i}$$
# 
# where $I_{[e_{i}<0]}$ is known as an indicator variable that takes the value
# 1 if the statement in brackets is true. Plot y. $e$ is a standard normal
# shock. Use `cumsum` to simulate a symmetric one (`z`), and plot the two using
# the code in the cell below.
#  

#%%


#%%
# Plot the two random walks using the code.  We will cover data visualization
# in a later lesson. 
# 
# ```python
# %matplotlib inline
# import matplotlib.pyplot as plt
# plt.plot(y)
# plt.plot(z)
# plt.legend(["y", "z"])
# ```

#%%


#%%
# ## Problem: Simulate the asymmetric random walk without an `if`-`then`
# 
# Use boolean multiplication to simulate the same random walk without using
# an `if`-`then` statement. 

#%%


#%%
# Setup: Plot the data
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')


#%%


#%%
# ## Problem: Combining flow control
# For momentum portfolios 1 and 10, compute the length of the runs in the
# series. In pseudo code,
# 
# * Start at i=1 and define run(1) = 1
# * For i in 2,...,T, define run(i) = run(i-1) + 1 if 
#   $\textrm{sgn}\left(r_{i}\right)=\textrm{sgn}\left(r_{i-1}\right)$ else 1.
# 
# You will need to use `len` and `zeros`. 
# 
# 1. Compute the length longest run in the series and the index of the
#    location of the longest run. Was it positive or negative?
# 2. How many distinct runs lasted 5 or more days?

#%%


#%%
# Plot the runs using 
# 
# ```python
# %matplotlib inline
# 
# import matplotlib.pyplot as plt
# plt.plot(run)
# ```

#%%


#%%
# ## Exercises
# 
# ### Exercise: Compute Drawdown
# 
# Using the momentum data, compute the maximum drawdown over all
# 22-day consequitive periods defined as the smallest cumulative 
# produce of the gross return (1+r) for 1, 2, .., 22 days.
# 
# Finally, compute the mean drawdown for each of the portfolios.

#%%

