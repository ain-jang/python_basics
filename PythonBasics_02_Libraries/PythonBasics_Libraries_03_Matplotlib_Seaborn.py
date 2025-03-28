
# Matplotlib documentation: https://matplotlib.org/stable/index.html


import matplotlib.pyplot as plt

# Input Numbers
# Enter a single list of numbers.
#   : if you pass a single list of numbers, it will be treated as y values, and x will default to [0, 1, 2, 3]
#     a python tuple or a numpy array also can be used.
# plt.show() will display the plot.
# Enter 2 lists of numbers
#   : in this case, the lists will be interpreted as x and y values, respectively.
#     the pairs (x, y) are plotted as points on the graph

plt.plot([2, 3, 4, 5])
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()


# Axis labels
# xlabel(): set the label for the x-axis
# ylabel(): set the label for the y-axis

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.show()


# Legend
# Legend describes the elements of the plot
# lengend(): to add a legend to the plot
# Set labels using the label parameter in plot()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], label = 'Square')
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.legend()
plt.show()

# How to set the axis range
# xlim([xmin, xmax]: to set the x-axis range
# ylim([ymin, ymax]: to set the y-axis range
# axis([xmin, xmax, ymin, ymax]): to set both x and y ranges
# If no values are given, the range is set automatically based on the data

plt.plot([1, 2, 3, 4], [3, 6, 9, 12])
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.xlim([0, 5])
plt.ylim([0, 15])

plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.axis([0, 6, 0, 20])
plt.show()


# Line Styles
# Customize line styles in plot() using format strings or the linestyle parameter.
# Check the official documents for available styles
# you can also use a tuple for more control

# Format strings
plt.plot([1, 2, 3], [4, 4, 4], '-', color = 'C0', label = 'Solid')
plt.plot([1, 2, 3], [3, 3, 3], '--', color = 'C0', label = 'Dashed')
# Linestyle parameter
plt.plot([1, 2, 3], [2, 2, 2], linestyle='dotted', color='C0', label='Dotted')
plt.plot([1, 2, 3], [1, 1, 1], linestyle='dashdot', color='C0', label='Dash-dot')
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.axis([0.8, 3.2, 0.5, 5.0])
plt.legend(loc='upper right', ncol=4)

plt.show()

# Tuple
plt.plot([1, 2, 3], [4, 4, 4], linestyle=(0, (1, 1)), color = 'C0', label = '(0, (1, 1)')
plt.plot([1, 2, 3], [3, 3, 3], linestyle=(0, (1, 5)), color = 'C0', label = '(0, (1, 5)')
plt.plot([1, 2, 3], [2, 2, 2], linestyle=(0, (5, 1)), color = 'C0', label = '(0, (5, 1)')
plt.plot([1, 2, 3], [1, 1, 1], linestyle=(0, (3, 5, 1, 5)), color = 'C0', label = '(0, (3, 5, 1, 5)')

plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.axis([0.8, 3.2, 0.5, 5.0])
plt.legend(loc='upper right', ncol=2)
plt.tight_layout()

plt.show()




####
# SEABORN (https://seaborn.pydata.org/)
#   : Seaborn is a library that uses Matplotlib underneath to plot graphs

import seaborn as sns

# Import titanic data from the library, using load_dataset()
titanic = sns.load_dataset('titanic')
print(titanic.head())
print(titanic.info())


# regplot(): Plot data and a linear regression model fit.
# * Linear regression model?
#   : A data analysis technique that predicts the value of unknown data by using another related and known data value.
# Parameters
#  - x, y variables
#  - data (dataframe)
#  - axes object
#  - fit_reg: if True (default), estimate and plot a regression model relating the x and y


# Create a graph object (2 subplots in the figure)
# fig = plt.figure(figsize=(15,5)) # 가로 15인치, 세로 5인치 크기의 그래프를 생성한다
# ax1 = fig.add_subplot(1, 2, 1) # 1행 2열로 구획을 나누고, 첫 번째 위치 (왼쪽)에 그래프 추가
# ax2 = fig.add_subplot(1, 2, 2) # 1행 2열의 두 번째 위치 (오른쪽)

# Case 1. fit_reg = True
sns.regplot(x = "age", y = "fare", data = titanic, ax = ax1)

#CAse 2. fit_reg = False
sns.regplot(x = "age", y = "fare", data = titanic, ax = ax2, fit_reg = False)

plt.show()


# distplot()
#   - plot a histogram or kernel density estimation
# Parameters
#  - data
#  - kind
#    hist: if True, histogram displayed, if False, no histogram
#    kde: if True, shows kernel density estimation
#  - axes object
# hisplot()
#   - histogram (to visualize the distribution of a single variable)
# kdeplot()
#   - kernel density estimate (the area under the curve equals 1)


fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

# distplot
sns.distplot(titanic["fare"], ax = ax1)

# histplot
sns.histplot(x = "fare", data = titanic, ax = ax2) # == sns.distplot(titanic["fare"], kde = False, ax = ax2)

#kdeplot
sns.kdeplot(x = "fare", data = titanic, ax = ax3) # == sns.distplot(titanic["fare"], hist = False, ax = ax3

ax1.set_title("Titanic fare - distplot")
ax2.set_title("Titanic fare - histplot")
ax3.set_title("Titanic fare - kdeplot")

plt.show()


# Scatterplots
# stripplot() : 데이터 포인트가 중복되어 범주별 분포를 시각화
# Stripplots are a special form of scatter plots and can be used to display the distribution of a numeric variable by a specific category
# Parameters
#  - x, y variables
#  - data
#  - axes
#  - hue


# swarmplot() :Draw a categorical scatterplot with points adjusted to be non-overlapping
# 데이터의 분산까지 고려하여 데이터 포인트가 서로 중복되지 않도록 시각화 (데이터가 퍼져있는 정도를 입체적으로 파악 가능)
# Parameters
#  - x, y variables
#  - data
#  - axes
#  - hue

fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# # 이산형 변수의 분포 - 데이터 분산 미고려
sns.stripplot(x = "class", y = "age", data = titanic, ax = ax1)

# # 이산형 변수의 분포 = 데이터 분산 고려 (겹치지 않게 표시됨)
sns.swarmplot(x = "class", y = "age", data=titanic, ax = ax2, hue = 'sex')

ax1.set_title("Strip Plot")
ax2.set_title("Swarm Plot")

plt.show()


# Frequency Plot
# countplot(): Show the counts of observations in each categorical bin using bars.
#               각 범주에 속하는 데이터의 개수를 막대 그래프로 시각화
# Parameters
#  - x variable
#  - palette: (colors to use for the different levels of the hue variable)
#  - data
#  - axes
#  - hue

fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

# # class 별 인원 파악
sns.countplot(x="class", palette="Set1", data=titanic, ax=ax1)

# hue 옵션에 'who' 추가
sns.countplot(x="class", hue="who", palette="Set2", data=titanic, ax=ax2)

# dodge=False 옵션 추가 (축 방향으로 분리하지 않고 누적 그래프 출력)
sns.countplot(x="class", hue="who", palette="Set3", dodge=False, data=titanic, ax=ax3)

ax1.set_title("Titanic Class")
ax2.set_title("Titanic Class - Who")
ax3.set_title("Titanic Class - Who (stacked)")

plt.show()


# Joint Plot
# jointplot(): Draw a plot of two variables with bivariate and univariate graphs.
# Parameters
#  - x, y variable
#  - data
#  - kind = 'reg' (add a linear regression)
#  - kind = 'hex' (add a hexbin)
#  - kind = 'kde' (add a kernel density estimate)

j1 = sns.jointplot(x = "fare", y='age', data=titanic)
j1.fig.suptitle("Titanic Fare - Scatter", size = 15)

plt.show()


j2 = sns.jointplot(x = "fare", y="age", kind="hex", data=titanic)
j2.fig.suptitle("Titanic Fare - Hex.", size = 15)

plt.show()


# Pair plot
# pairplot(): Plot pairwise relationships in a dataset.
# Shows all pairwise combinations of numeric columns in a DataFrame.
#  인자로 전달되는 데이터프레임의 열(변수)를 두 개씩 짝지을 수 있는 모든 조합에 대해서 표현
# The columns must be numeric (int or float).
#  열은 정수/실수형이어야 함
# If there are 3 columns, it creates a 3×3 grid of plots.
#  3개 열이라면 3x3 크기로 총 9개의 그리드 생성
# Each grid cell shows the relationship between a pair of variables.
#  각 그리드의 두 변수 간 관계를 나타내는 그래프를 하나씩 그림
# Diagonal plots show histograms of individual variables.
#  같은 변수끼리 짝을 이루는 대각선 방향으로는 히스토그램 시각화
# Off-diagonal plots show scatter plots between pairs.
#  서로 다른 변수 간에는 산점도 시각화

titanic_pair = titanic[['age', 'pclass', 'fare']]
sns.pairplot(titanic_pair)
plt.show()




#END
