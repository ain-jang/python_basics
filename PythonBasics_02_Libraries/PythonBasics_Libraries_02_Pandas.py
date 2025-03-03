
# Pandas documentation: https://pandas.pydata.org/docs/

import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)  # 가로 출력 폭 넓히기
pd.set_option("display.max_colwidth", None)  # 긴 문자열도 자르지 않음

# Titanic - Machine Learning from Disaster (Kaggle: www.kaggle.com/c/titanic)
#   : Predict if a passenger survived the sinking of the Titanic or not.

# Series & DataFrame
# Series: A one-dimensional array holding data of any type (like a column)
# DataFrame: a multi-dimensional table (like the whole table)

# Series
dict_data = {'a':1, "b":2, "c":3}
series_dict_data = pd.Series(dict_data)

print(type(series_dict_data))
print(series_dict_data)

list_data = ["2025-05-12", 3.14, "ABC", 100, True]
series_list_data = pd.Series(list_data)

print(type(series_list_data))
print(series_list_data)

# DataFrame
dict_data_2 = {"c0": [1,2,3], "c1": [4,5,6], "c3": [10,11,12], "c4": [13,14,15]}
df = pd.DataFrame(dict_data_2)

print(type(df))
print(df)


# Read & To Functions to read or write external files
# read_(file type), to_(file type)
# .columns: name of the columns
# .head(n): the first n rows (default == 5)
# .tail(n): the last n rows (default == 5)
# .shape: shape of the data set (rows x columns)
# .info(): general information of the data
#               e.g. numbers of the rows / columns, column names, data type, etc.
# type(dataset name): shows the data type

# Practice!
titanic = pd.read_csv("C:/Users/sarah/Desktop/CZ/Study/FC/Python_basics/titanic.csv")

# print(titanic.columns)
# print(titanic.head())
# print(titanic.tail())
# print(titanic.shape)
# print(titanic.info())
# print(type(titanic))


# Selecting specific columns
# 1. To grab a single column - Extracted as a series object
#       1) Use square brackets([]) with the column name in quotes.
#       2) Use dot notation(.) followed by the column name.
# These will return a series.
# IF you want to extract a single column as a dataframe instead of a series,
# use double square brackets ([[]]).
# 2. To pull multiple columns - Extracted as a dataframe object
#       1) Use double square brackets([[]]) with the column names in quotes("").


# Grab one column
print("Name column")
names = titanic['Name']  # == names = titanic.Name
print(names.head())
print(type(names))
print(names.shape)
print("It returned a Series.")

# Grab two columns
print("DataFrame 'passenger' - Sex and Age")
passenger = titanic[["Sex", "Age"]]
print(passenger.head())
print(type(passenger))
print(passenger.shape)
print("It returned a DataFrame.")


# Filtering data
# 1. Boolean Indexing: Selecting rows with True values
# Extract the data where age is over 35 (T/F)
print("Extract the data where age is over 35 (T/F).")
print(passenger["Age"] > 35)
print("Now extract only the data where age is over 35.")
above35 = passenger[passenger["Age"] > 35]
print(above35.head())
print("Now it's filtered!")

# 2. .isin(): Check if each element exists in a DataFrame or Series and return True/False
# 3. Boolean Indexing + .isin(): Extract a specific range of data
print(titanic.head(2))
print("1. Filter rows where Pclass is 1.")
# [titanic['Pclass'].isin([1])] -> p클래스가 1인 애들만 true로, 나머지는 false로 변환됨
class1 = titanic[titanic['Pclass'].isin([1])]
# 이제 p클래스가 true인 애들만 추출됨
print(class1.head(3))

print("2.Filter passengers whose age is between 20 and 40.")
age2040 = titanic[titanic['Age'].isin(np.arange(20, 41))]
print(age2040.head(3))

# 4. .isna(): Returns True for missing values, returns False otherwise
# 5. .notna(): Returns False for missing values, returns True otherwise
print("Any missing values?")
print(passenger.head(7))
# print("Using .isna()...")
# print(passenger["Age"].isna()[0:7])
print("Using .notna()...")
print(passenger["Age"].notna()[0:7])

print("Filter rows where there is no missing values.")
ages = passenger[passenger["Age"].notna()]
print(ages.head(7))

# 6. .dropna(axis=0) == .dropna(): Removes ROWS with NULL values from the DataFrame
print("Null values in Cabin column")
print(titanic.head(3))
titanic_cabin_clean = titanic.dropna(axis=0).head(3)
print("What about now?")
print(titanic_cabin_clean.head(3))

# 7. .dropna(axis=1): Removes COLUMNS with NULL values from the DataFrame
titanic_cabin_removed = titanic.dropna(axis=1).head(3)
print("And now?")
print(titanic_cabin_removed)



# How to get the value(s) of the specified labels/indexes.
# dataframe.loc[row, column] - 이름 기반 선택
# dataframe.iloc[row, column] - 번호 기반 선택
#https://www.w3schools.com/python/pandas/ref_df_loc.asp

# Return the name and age of a person who is older than 35.
names35 = titanic.loc[titanic["Age"] > 35, ["Name", "Age"]]
print(names35.head())

# Update the 0th column to 'No name' for rows 1 to 3
names35.iloc[[1, 2, 3], 0] = "No name"
print(names35.head())



# Statistics in Pandas
# .mean(): the mean value 평균값
# .median(): the median value 중앙값
# .describe(): a statistical description of the data in the DataFrame 다양한 통계량 요약
#               - mean, std, min, 25%, 50%, 75%, max
# .agg():  allows you to apply a function or a list of function names to be executed along one of the axis of the DataFrame, default 0, which is the index (row) axis.
#               - 여러 개의 열에 다양한 함수를 적용
#               - 모든 열에 여러 함수를 매핑: group객체.agg([함수1, 함수2, 함수3, ...])
#               - 각 열마다 다른 함수를 매핑: group객체.agg({'열1':함수1, '열2':함수2,...}
# .groupby(): to group the data and execute functions on these groups. 그룹별 집계
# .value_counts(): to get a Series containing counts of unique values 값의 개수


# Get the mean value of the Age column
print(titanic["Age"].mean())

# Get the median value of the Age column
print(titanic["Age"].median())

# Use describe() to see the statistically description of Age and Fare data in Titanic.
print(titanic[["Age", "Fare"]].describe())

# Use .agg() to return the values you want to see.
print(titanic.agg({"Age" : ["min", "max", "median", "std"],
                     "Fare" : ["min", "max", "mean", "median"]}))

# Group by gender and class, then calculate the average age and fare
print(titanic.groupby(["Sex", "Pclass"])[["Age", "Fare"]].mean())

# Get the mean survival rate for each gender.
survive = titanic.groupby(["Sex"])["Survived"].mean()
survival_rate = survive * 100
print(survival_rate)

# How many passengers were there in each class?
print(titanic["Pclass"].value_counts())


# Adding a new row or column in existing DataFrame
# DataFrame.loc["New_row_name"] = values
# DataFrame object["New_column_name] = values

print(titanic.head(3))
print(titanic.shape)

# Copy the first row and add it as a new row at the end
newRow = titanic.iloc[0,:]
titanic.loc[891] = newRow
print(titanic)

print(titanic.shape)

# Add a new column (Pclass * 3) called '3Pclass'
titanic["3Pclass"] = titanic["Pclass"] * 3
print(titanic.head())

print(titanic.shape)

# Deleting a new row or column in existing DataFrame
# Deleting a row: DataFrame.drop(index, axis = 0)
# Deleting a column: DataFrame.drop(변수, axis = 1)

titanic = titanic.drop(np.arange(880, 890), axis = 0)
titanic = titanic.drop("3Pclass", axis = 1)

print(titanic)



#END
