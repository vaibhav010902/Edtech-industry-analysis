import pandas as pd
import numpy as np

# Reading the CSV file
coursera_file = pd.read_csv("Coursera.csv")
print(coursera_file)

# Adding the 'Category' column
coursera_file['Category'] = 0
print(coursera_file)

# Descriptive statistics
print(coursera_file.describe())

# Type casting the 'course' column to string
coursera_file["course"] = coursera_file["course"].values.astype('str')
print(np.dtype(coursera_file['course']))
print(coursera_file)

# Assigning 'Data' to 'Category' where 'course' contains 'data'
coursera_file['Category'] = np.where(coursera_file['course'].str.contains('arts and humanities', case=False, na=False), 'Art and Humanities', coursera_file['Category'])
coursera_file['Category'] = np.where(coursera_file['course'].str.contains('data analytics', case=False, na=False), 'Data', coursera_file['Category'])
coursera_file['Category'] = np.where(coursera_file['course'].str.contains('data science', case=False, na=False), 'Data', coursera_file['Category'])
coursera_file['Category'] = np.where(coursera_file['course'].str.contains('data science', case=False, na=False), 'Data', coursera_file['Category'])
coursera_file['Category'] = np.where(coursera_file['course'].str.contains('data science', case=False, na=False), 'Data', coursera_file['Category'])


print(coursera_file.dtypes)
print(coursera_file)
