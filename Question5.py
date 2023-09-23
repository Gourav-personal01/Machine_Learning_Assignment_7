# Q5. A survey was conducted to examine the relationship between age and preference for a particular
# brand of soft drink. The survey results are shown below:
import pandas as pd
df = pd.DataFrame({
    'age' : [25, 42, 37, 19, 31, 28],
    'prefernce' : ['Coke', 'Pepsi', 'Mountain dew', 'Coke', 'Pepsi', 'Coke']
})

from sklearn.preprocessing import LabelEncoder

label = LabelEncoder()
pref = pd.DataFrame(label.fit_transform(df['prefernce']), columns=['encoded_pref'])
print(pref)

# Corrected line to drop 'prefernce' column
df = df.drop('prefernce', axis=1)

df1 = pd.concat([df, pref], axis=1)

# Pearson Correlation Coefficient
print(df1.corr(method='pearson'))
