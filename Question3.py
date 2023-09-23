# Q3. Suppose you are conducting a study to examine the relationship between the number of hours of
# exercise per week and body mass index (BMI) in a sample of adults. You collected data on both variables
# for 50 participants. Calculate the Pearson correlation coefficient and the Spearman's rank correlation
# between these two variables and compare the results.

# Answer - 
import numpy as np
import scipy.stats

# Sample data for exercise hours per week and BMI
exercise_hours = np.array([3, 5, 2, 4, 1, 6, 3, 2, 4, 5, 1, 3, 6, 2, 4, 5, 3, 1, 4, 2, 6, 3, 5, 2, 4, 1, 6, 3, 2, 4, 5, 1, 3, 6, 2, 4, 5, 3, 1, 4, 2, 6, 3, 5, 2, 4, 1, 6, 3])
bmi = np.array([24.3, 26.5, 28.1, 27.8, 29.2, 23.7, 25.9, 27.1, 26.8, 25.3, 30.5, 24.6, 23.8, 26.2, 25.1, 27.7, 24.4, 29.8, 25.6, 28.9, 27.0, 23.4, 24.9, 28.5, 27.2, 29.6, 23.9, 25.7, 26.3, 27.3, 26.1, 29.0, 24.2, 25.0, 28.3, 26.7, 29.4, 23.5, 25.5, 27.4, 26.4, 30.2, 23.6, 24.7, 28.7, 25.8, 27.5, 30.0, 26.0])

# Calculate Pearson correlation coefficient
pearson_corr, _ = scipy.stats.pearsonr(exercise_hours, bmi)

# Calculate Spearman's rank correlation coefficient
spearman_corr, _ = scipy.stats.spearmanr(exercise_hours, bmi)

# Print the results
print(f"Pearson Correlation Coefficient: {pearson_corr}")
print(f"Spearman's Rank Correlation: {spearman_corr}")
