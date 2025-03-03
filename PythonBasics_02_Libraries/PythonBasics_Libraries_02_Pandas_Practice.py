# Import pandas package as pd, numpy package as np

import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)  # 가로 출력 폭 넓히기
pd.set_option("display.max_colwidth", None)  # 긴 문자열도 자르지 않음

# Import titanic.csv
titanic = pd.read_csv("C:/Users/sarah/Desktop/CZ/Study/FC/Python_basics/titanic.csv")

# Print first 9 rows of the dataset.
print(titanic.head(9))

# Print the size and general information of the dataset.
print(titanic.shape)
print(titanic.info())

# Pull and print the first few lines of "Age" column as titanic_age.
titanic_age = titanic[["Age"]]
print(titanic_age.head())

# Is titanic_age a series object? or is it a dataframe?
print(type(titanic_age))

# Print the size of titanic_age
print(titanic_age.shape)

# Grab "Fare" and "Cabin" columns and print the first few rows, and then check the data type.
titanic_fare_cabin = titanic[["Fare", "Cabin"]]
print(titanic_fare_cabin.head())

# Print the datatype and size of titanic_fare_cabin.
print(type(titanic_fare_cabin))
print(titanic_fare_cabin.shape)

# Filter the data from 'titanic_fare_cabin'.
#   - print 'True' if fare is greater than 50, otherwise print 'False'.
print(titanic_fare_cabin["Fare"] > 50)

#   - print rows where 'fare' > 50.
above_50 = titanic_fare_cabin[titanic_fare_cabin["Fare"] > 50]
print(above_50)

# Check for any missing values across columns, drop them if any, and print the 'titanic' dataset to verify.
print(titanic.notna())
print(titanic.dropna(axis=1))

# In the titanic_fare_cabin dataset, change the values in the third row, first column to 1000.
# And then print the first 5 rows to verify.
print(titanic_fare_cabin.head(3))
titanic_fare_cabin.iloc[2, 0] = 1000
print(titanic_fare_cabin.head(3))

# Print the statistical description of 'Fare' in 'titanic_fare_cabin'.
print(" ")
print(titanic_fare_cabin['Fare'].describe())

# Group by 'Survived' and 'Pclass' in the 'titanic' dataset, then calculate the mean of 'Age' and 'Fare'
print(titanic.head(3))
print(titanic.groupby(['Survived', 'Pclass'])[['Age', 'Fare']].mean())

# How many unique values are there in each category of 'Survived'?
print(titanic['Survived'].value_counts())

# Add a new column (Pclass * 10) called '10Pclass'
titanic['10Pclass'] = titanic['Pclass'] * 10
print(titanic.head(3))



#END