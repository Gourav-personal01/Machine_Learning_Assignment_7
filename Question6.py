# Q6. A company is interested in examining the relationship between the number of sales calls made per day
# and the number of sales made per week. The company collected data on both variables from a sample of
# 30 sales representatives. Calculate the Pearson correlation coefficient between these two variables.

import numpy as np
import scipy.stats

# Sample data for the number of sales calls per day and sales per week
sales_calls_per_day = np.array([20, 25, 18, 22, 30, 28, 19, 15, 23, 27, 21, 24, 17, 26, 29, 31, 20, 22, 16, 25, 18, 19, 29, 24, 27, 21, 23, 17, 26, 30])
sales_per_week = np.array([3, 5, 2, 4, 7, 6, 3, 2, 4, 6, 4, 5, 2, 6, 7, 8, 3, 4, 2, 5, 2, 3, 7, 5, 6, 4, 4, 2, 6, 7])

# Calculate Pearson correlation coefficient
pearson_corr, _ = scipy.stats.pearsonr(sales_calls_per_day, sales_per_week)

# Print the result
print(f"Pearson Correlation Coefficient: {pearson_corr}")
