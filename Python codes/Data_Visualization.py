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
    #df_var['imdbRating'].hist(bins = 10) 
    
    plt.figure(figsize =(10, 4))
    y_pos = np.arange((df_var['imdbRating'].value_counts()))    
    plt.bar(df_var['imdbRating'],y_pos,width=5)
    
    df_var['imdbRating'].value_counts().sort_index().plot(kind='bar')
    df_var['imdbRating'].plot(kind='hist', hist_kwds={'bins':[i*0.1 for i in range(11)]})
    
    plt.show()
    
except Exception as exp:
    print(exp)