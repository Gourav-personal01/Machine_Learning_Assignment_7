# Q1. Pearson correlation coefficient is a measure of the linear relationship between two variables. Suppose
# you have collected data on the amount of time students spend studying for an exam and their final exam
# scores. Calculate the Pearson correlation coefficient between these two variables and interpret the result.

import pandas as pd
import numpy as np

data = [[5,6],[50,60]]

df = pd.DataFrame(data,columns=["Study Hours","Final Marks"])

# Pearson Correlation Coefficient 

print(df.corr(method='pearson'))