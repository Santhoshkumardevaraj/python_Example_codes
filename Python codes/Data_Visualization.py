# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:10:59 2020

@author: Defender
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

try:
    #read Movies.csv into df_var
    df_var=pd.read_csv("../Movies.csv")
    
    #visuaize insights in dataframe
    df_var.describe()
    
       
    plt.figure(figsize =(10, 4)) 
    df_var['imdbRating'].value_counts().sort_index().plot(kind='bar')
    
    plt.figure(figsize =(10, 4))
    df_var['imdbRating'].plot(kind='hist')
    
    plt.figure(figsize =(10, 4))
    df_var['imdbRating'].plot(kind='box')
    
    plt.figure(figsize =(10, 4))
    df_var['imdbRating'].plot(kind='line')
    
    plt.figure(figsize =(10, 4))
    df_var['imdbRating'].plot(kind='density')
    
    plt.figure(figsize =(10, 4))
    df_var['imdbRating'].plot(kind='area')
    
    plt.figure(figsize =(10, 4))
    df_var['imdbRating'].plot(kind='pie')
    
    plt.show()
    
except Exception as exp:
    print(exp)