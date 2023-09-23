# Q2. Spearman's rank correlation is a measure of the monotonic relationship between two variables.
# Suppose you have collected data on the amount of sleep individuals get each night and their overall job
# satisfaction level on a scale of 1 to 10. Calculate the Spearman's rank correlation between these two
# variables and interpret the result.

import pandas as pd
import numpy as np

df1 = pd.DataFrame([2,4,3,4,9,9,7,1,9,10],columns=["Job Satisfaction Level"])
df2 = pd.DataFrame([2,3,3,3,9,9,5,10,9,10],columns=["Person's sleep individuals"])
df = pd.concat([df1,df2],axis=1)

# Pearson Correlation Coefficient 

print(df.corr(method='pearson'))