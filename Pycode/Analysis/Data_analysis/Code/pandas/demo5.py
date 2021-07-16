import pandas as pd

f = pd.read_csv('student.csv')

# print(f.info())
# print(f)
print(f.loc[:,'height'].value_counts())