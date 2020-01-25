#!/usr/bin/env python
# coding: utf-8

#%%
# ## ARCH Model Estimation
# 
# **Functions**
# 
# `arch.arch_model`

#%%
# ### Exercise 50
# 
# Download 10 years of data for the S&P 500 and the EUR/USD exchange rate from FRED.
# 

#%%
# Setup
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')


#%%
# ### Exercise 51
# 
# Estimate a GARCH(1,1) and a GJR-GARCH(1,1,1) to the returns of both series.
# 
# **Note**: You need to install arch using
# 
# ```bash
# pip install arch
# ```
# 
# which contains ARCH and related models.
# 
# Documentation and examples for the arch package [are available online](https://bashtage.github.io/arch).

#%%


#%%
# ### Exercise 52
# Comment on the asymmetry.
# 
#   * Compare robust and non-robust standard errors.
#   * Plot the fit variance and fit volatility.
#   * Plot the standardized residuals.
# 

#%%

