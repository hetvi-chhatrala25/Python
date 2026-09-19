# Sales Data Analysis and Visualization Tool

## 📌 Project Overview

The **Sales Data Analysis and Visualization Tool** is a menu-driven Python application developed using **Pandas, NumPy, Matplotlib, Seaborn, and Object-Oriented Programming (OOP)** principles.

This project uses a **Coffee Sales CSV dataset** to perform data loading, exploration, cleaning, mathematical operations, searching, sorting, filtering, aggregation, statistical analysis, pivot tables, grouping, data combining, data splitting, re-indexing, and visualization.

The complete functionality is encapsulated inside the **`SalesDataAnalyzer`** class.

---

## 🎯 Objective

Develop a comprehensive **Sales Data Analysis and Visualization Tool** using Python.

The application allows users to:

* Load sales data from a CSV file
* Explore the dataset
* Check rows, columns, data types, and missing values
* Clean and prepare the data
* Perform NumPy operations
* Perform mathematical operations
* Combine DataFrames using concatenation, merge, and join
* Split data using groupby
* Search, sort, and filter data
* Calculate aggregate functions
* Perform statistical analysis
* Create pivot tables
* Perform GroupBy and Transform operations
* Re-index the DataFrame
* Perform date and time operations
* Create Matplotlib visualizations
* Create Seaborn visualizations
* Save visualizations
* Export processed data to CSV
* Display a final sales analysis conclusion
* Operate the application through a menu-driven interface

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Jupyter Notebook**

---

## 📊 Dataset

The project uses a **Coffee Sales Dataset** stored in:

```text
coffe_sales.csv
```

The dataset contains coffee sales information that can be analyzed using different Pandas, NumPy, Matplotlib, and Seaborn operations.

Important columns used by the program include:

```text
coffee_name
money
cash_type
```

The program also automatically searches for a date/time-related column such as:

```text
datetime
date
date_time
timestamp
```

The actual available columns depend on the CSV dataset.

---

# 📚 Pandas Concepts Used

## 1. Reading CSV Data

The dataset is loaded using:

```python
pd.read_csv(file_path)
```

Example:

```python
self.data = pd.read_csv(file_path)
```

This reads the CSV file and stores the data inside a Pandas DataFrame.

---

## 2. DataFrame

The sales dataset is stored as a Pandas DataFrame:

```python
self.data = pd.DataFrame()
```

A DataFrame is a two-dimensional table containing rows and columns.

---

## 3. First and Last Rows

The program displays the first five rows using:

```python
self.data.head()
```

The last five rows are displayed using:

```python
self.data.tail()
```

---

## 4. Column Names

Column names are displayed using:

```python
self.data.columns
```

The program also removes unnecessary spaces from column names:

```python
self.data.columns = self.data.columns.str.strip()
```

---

## 5. Data Types

Data types are displayed using:

```python
self.data.dtypes
```

This helps identify whether a column contains integers, floating-point values, strings, dates, etc.

---

## 6. Dataset Information

The program uses:

```python
self.data.info()
```

This displays information about:

* Number of rows
* Number of columns
* Column names
* Data types
* Non-null values
* Memory usage

---

## 7. Statistical Description

The program uses:

```python
self.data.describe(include="all")
```

This provides statistical information about the dataset.

---

## 8. Dataset Shape

The shape of the DataFrame is obtained using:

```python
self.data.shape
```

It returns:

```text
(rows, columns)
```

---

## 9. DataFrame Index

The current DataFrame index is displayed using:

```python
self.data.index
```

---

## 10. Unique Values

Unique values from a selected column are displayed using:

```python
self.data[column].unique()
```

This helps identify different categories present in a column.

---

## 11. Missing Values

Missing values are checked using:

```python
self.data.isnull().sum()
```

This displays the number of missing values in each column.

---

# 🧹 Data Cleaning

The project provides several data-cleaning operations.

## 1. Display Missing Values

The program checks missing values using:

```python
self.data.isnull().sum()
```

---

## 2. Fill Missing Numeric Values

Numeric columns are selected using:

```python
self.data.select_dtypes(include=np.number)
```

Missing numeric values can be filled with the column mean:

```python
self.data[column] = self.data[column].fillna(
    self.data[column].mean()
)
```

---

## 3. Drop Missing Rows

Rows containing missing values can be removed using:

```python
self.data.dropna(inplace=True)
```

---

## 4. Remove Duplicate Rows

Duplicate rows are removed using:

```python
self.data.drop_duplicates(inplace=True)
```

---

# 📅 Date and Time Operations

The program provides several date and time operations.

The program first searches for a suitable date/time column.

Date/time conversion is performed using:

```python
pd.to_datetime()
```

Example:

```python
self.data[column] = pd.to_datetime(
    self.data[column],
    errors="coerce"
)
```

The `errors="coerce"` option converts invalid date values into missing values instead of stopping the program.

---

## Date Extraction

The date can be extracted using:

```python
self.data["Date"] = self.data[column].dt.date
```

---

## Time Extraction

The time can be extracted using:

```python
self.data["Time"] = self.data[column].dt.time
```

---

## Hour Extraction

The hour is extracted using:

```python
self.data["Hour"] = self.data[column].dt.hour
```

---

## Day Extraction

The day is extracted using:

```python
self.data["Day"] = self.data[column].dt.day
```

---

## Month Extraction

The month is extracted using:

```python
self.data["Month"] = self.data[column].dt.month
```

---

## Weekday Extraction

The weekday name is extracted using:

```python
self.data["Weekday"] = self.data[column].dt.day_name()
```

---

# 🔢 NumPy Operations

The project uses NumPy to perform numerical operations on selected sales columns.

A Pandas column is converted into a NumPy array using:

```python
array = self.data[column].dropna().to_numpy()
```

---

## 1. NumPy Array

The selected column is converted into a NumPy array.

```python
array = self.data[column].to_numpy()
```

---

## 2. Array Type

The program displays the type of the array:

```python
type(array)
```

---

## 3. Array Shape

The shape is obtained using:

```python
array.shape
```

---

## 4. Array Size

The number of elements is obtained using:

```python
array.size
```

---

## 5. Array Indexing

Individual values can be accessed using:

```python
array[0]
```

---

## 6. Array Slicing

The program supports slicing such as:

```python
array[:5]
```

and:

```python
array[5:10]
```

---

## 7. Minimum and Maximum

Minimum:

```python
np.min(array)
```

Maximum:

```python
np.max(array)
```

---

## 8. Mean

The average is calculated using:

```python
np.mean(array)
```

---

## 9. Standard Deviation

Standard deviation is calculated using:

```python
np.std(array)
```

---

## 10. Element-wise Operations

The program performs operations such as:

```python
array + 10
```

```python
array - 10
```

```python
array * 2
```

```python
array // 2
```

These operations are performed on every element of the NumPy array.

---

## 11. Combining Arrays

The program combines parts of an array using:

```python
np.concatenate()
```

Example:

```python
np.concatenate((first_part, second_part))
```

---

## 12. Splitting Arrays

The array is divided into multiple parts using:

```python
np.array_split()
```

Example:

```python
np.array_split(array, 2)
```

---

# ➕ Mathematical Operations

The project provides mathematical operations on the **`money`** column of the Coffee Sales dataset.

The column is converted into numeric values using:

```python
pd.to_numeric(
    self.data["money"],
    errors="coerce"
)
```

---

## Double Money

```python
self.data["Double_Money"] = self.data["money"] * 2
```

---

## Half Money

```python
self.data["Half_Money"] = self.data["money"] / 2
```

---

## Add 10

```python
self.data["Money_Plus_10"] = self.data["money"] + 10
```

---

## Subtract 10

```python
self.data["Money_Minus_10"] = self.data["money"] - 10
```

---

## Square

```python
self.data["Money_Squared"] = self.data["money"] ** 2
```

---

# 🔗 Combining DataFrames

The project provides three ways to combine DataFrames.

## 1. Concatenation

Concatenation is performed using:

```python
pd.concat()
```

Example:

```python
self.data = pd.concat(
    [self.data, other_dataframe],
    ignore_index=True
)
```

This combines DataFrames row-wise.

---

## 2. Merge

DataFrames can be merged using:

```python
pd.merge()
```

Example:

```python
pd.merge(
    self.data,
    other_dataframe,
    on=common_column,
    how="outer"
)
```

The program asks the user to enter a common column.

---

## 3. Join

The project also supports DataFrame joining.

The common column is first set as an index:

```python
self.data.set_index(common_column)
```

Then the DataFrames are joined using:

```python
.join()
```

Example:

```python
self.data.join(
    other_dataframe,
    how="outer"
)
```

---

# ✂️ Splitting Data

The program allows the user to split the DataFrame according to a selected column.

It uses:

```python
self.data.groupby(column)
```

Example:

```python
groups = self.data.groupby(column)

for group_name, group_data in groups:
    print(group_name)
    print(group_data.head())
```

This displays each group separately.

---

# 🔎 Search, Sort and Filter

The project provides search, sorting, and filtering operations.

## 1. Search

Text values can be searched using:

```python
str.contains()
```

Example:

```python
self.data[
    self.data[column].astype(str).str.contains(
        value,
        case=False,
        na=False
    )
]
```

The search is case-insensitive.

---

## 2. Sort

Data can be sorted using:

```python
self.data.sort_values()
```

The user can select:

* Ascending
* Descending

Example:

```python
self.data.sort_values(
    by=column,
    ascending=True
)
```

---

## 3. Filter

Numeric columns can be filtered using conditions such as:

```text
>
<
>=
<=
==
```

Examples:

```python
self.data[column] > value
```

```python
self.data[column] < value
```

```python
self.data[column] >= value
```

```python
self.data[column] <= value
```

```python
self.data[column] == value
```

Categorical columns can also be searched using:

```python
str.contains()
```

---

# 📊 Aggregate Functions

The project calculates aggregate values for selected numeric columns.

## Sum

```python
self.data[column].sum()
```

Calculates the total value.

---

## Mean

```python
self.data[column].mean()
```

Calculates the average value.

---

## Minimum

```python
self.data[column].min()
```

Finds the smallest value.

---

## Maximum

```python
self.data[column].max()
```

Finds the largest value.

---

## Count

```python
self.data[column].count()
```

Counts non-missing values.

---

## Median

```python
self.data[column].median()
```

Calculates the middle value.

---

# 📈 Statistical Analysis

The program performs statistical analysis on numeric columns.

Numeric columns are selected using:

```python
self.data.select_dtypes(include=np.number)
```

---

## Description

```python
numeric_data.describe()
```

Provides:

* Count
* Mean
* Standard deviation
* Minimum
* Quartiles
* Maximum

---

## Standard Deviation

```python
numeric_data.std()
```

Measures the variation in the data.

---

## Variance

```python
numeric_data.var()
```

Measures the spread of the data.

---

## Quantiles

The project calculates:

```python
numeric_data.quantile(0.25)
```

```python
numeric_data.quantile(0.50)
```

```python
numeric_data.quantile(0.75)
```

These represent the 25th, 50th, and 75th percentiles.

---

# 📋 Pivot Table

The project creates pivot tables using:

```python
pd.pivot_table()
```

Example:

```python
pd.pivot_table(
    self.data,
    index=index_column,
    values=value_column,
    aggfunc=["sum", "mean", "count"]
)
```

The pivot table calculates:

* Sum
* Mean
* Count

for the selected columns.

---

# 🔄 GroupBy and Transform

The project performs grouping using:

```python
self.data.groupby(group_column)
```

For example:

```python
self.data.groupby(group_column)[value_column].sum()
```

This calculates the total value for each group.

---

## Transform

The program also creates a group-wise mean using:

```python
self.data["Group_Mean"] = (
    self.data.groupby(group_column)[value_column]
    .transform("mean")
)
```

Unlike `groupby().mean()`, `transform()` returns a value for every original row.

---

# 🔢 Re-indexing

The DataFrame can be re-indexed using:

```python
self.data.reset_index(drop=True, inplace=True)
```

This creates a new sequential index starting from:

```text
0
1
2
3
...
```

---

# 📊 Matplotlib Visualizations

The project uses **Matplotlib** to create different types of charts.

The following visualizations are included:

* Bar Chart
* Line Chart
* Scatter Plot
* Pie Chart
* Histogram
* Stack Plot
* Subplots

---

# 📊 1. Matplotlib Bar Chart

A bar chart is created using:

```python
ax.bar()
```

The program groups sales data and displays the top categories.

Example:

```python
grouped = self.data.groupby(
    x_column
)[y_column].sum()

grouped = grouped.sort_values(
    ascending=False
).head(10)

ax.bar(
    grouped.index,
    grouped.values
)
```

The chart includes:

```python
ax.set_title()
ax.set_xlabel()
ax.set_ylabel()
```

The x-axis labels can also be rotated.

---

# 📈 2. Matplotlib Line Chart

The line chart displays daily coffee sales.

The program groups sales by date and uses:

```python
ax.plot()
```

Example:

```python
ax.plot(
    daily_sales.index,
    daily_sales.values,
    marker="o"
)
```

The chart is titled:

```text
Daily Coffee Sales
```

---

# 🔵 3. Matplotlib Scatter Plot

A scatter plot is created using:

```python
ax.scatter()
```

It displays the relationship between two numeric columns.

Example:

```python
ax.scatter(
    self.data[x_column],
    self.data[y_column]
)
```

---

# 🥧 4. Matplotlib Pie Chart

A pie chart displays the distribution of a selected categorical column.

It uses:

```python
ax.pie()
```

Example:

```python
ax.pie(
    values,
    labels=labels,
    autopct="%1.1f%%"
)
```

The `autopct` parameter displays percentages on the chart.

---

# 📊 5. Matplotlib Histogram

A histogram displays the distribution of a numeric column.

It uses:

```python
ax.hist()
```

Example:

```python
ax.hist(
    self.data[column].dropna(),
    bins=10,
    edgecolor="black"
)
```

The `bins` parameter controls the number of intervals.

---

# 📚 6. Matplotlib Stack Plot

The stack plot displays coffee sales according to weekdays.

It uses:

```python
ax.stackplot()
```

The program creates weekday-based sales data and orders the weekdays as:

```text
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
```

This allows sales of different coffee types to be compared across weekdays.

---

# 🖼️ 7. Matplotlib Subplots

The project creates multiple charts in one figure using:

```python
fig, axes = plt.subplots(1, 2)
```

One subplot displays coffee sales by coffee name, while the other displays hourly sales.

This demonstrates how multiple plots can be displayed in a single figure.

---

# 🎨 Seaborn Visualizations

The project also uses **Seaborn** for statistical data visualization.

The following Seaborn charts are included:

* Box Plot
* Heatmap
* Count Plot
* Bar Plot
* Histogram
* Line Plot
* Scatter Plot

The project applies Seaborn styling using:

```python
sns.set_theme(style="whitegrid")
```

---

# 📦 1. Seaborn Box Plot

A box plot is created using:

```python
sns.boxplot()
```

Example:

```python
sns.boxplot(
    data=self.data,
    y=column,
    linewidth=2,
    fliersize=5
)
```

A box plot helps display the distribution and possible outliers of numerical data.

---

# 🔥 2. Seaborn Heatmap

The correlation between numeric columns is calculated using:

```python
numeric_data.corr()
```

The result is displayed using:

```python
sns.heatmap()
```

Example:

```python
sns.heatmap(
    correlation,
    annot=True,
    cmap="viridis",
    linewidths=1,
    linecolor="black",
    fmt=".2f"
)
```

The heatmap displays correlation values between numerical variables.

---

# 🔢 3. Seaborn Count Plot

A count plot displays the number of records in each category.

It uses:

```python
sns.countplot()
```

Example:

```python
sns.countplot(
    data=self.data,
    x=column
)
```

---

# 📊 4. Seaborn Bar Plot

A Seaborn bar plot is created using:

```python
sns.barplot()
```

Example:

```python
sns.barplot(
    data=self.data,
    x=x_column,
    y=y_column,
    errorbar=None
)
```

The program converts the selected y-column into numeric values before creating the chart.

---

# 📈 5. Seaborn Histogram

A histogram is created using:

```python
sns.histplot()
```

Example:

```python
sns.histplot(
    data=self.data,
    x=column,
    bins=10,
    kde=True
)
```

The `kde=True` option displays a smooth distribution curve.

---

# 📈 6. Seaborn Line Plot

The Seaborn line plot displays daily sales.

It uses:

```python
sns.lineplot()
```

Example:

```python
sns.lineplot(
    data=daily_sales,
    x="Date",
    y="money",
    marker="o"
)
```

---

# 🔵 7. Seaborn Scatter Plot

A scatter plot is created using:

```python
sns.scatterplot()
```

Example:

```python
sns.scatterplot(
    data=self.data,
    x=x_column,
    y=y_column
)
```

This displays the relationship between two numeric variables.

---

# 💾 Saving Visualizations

The current visualization can be saved using:

```python
self.current_plot.savefig()
```

Example:

```python
self.current_plot.savefig(
    file_name,
    dpi=300,
    bbox_inches="tight"
)
```

The user can enter a filename for the saved visualization.

---

# 📤 Exporting Data

The processed DataFrame can be exported as a CSV file using:

```python
self.data.to_csv(
    file_name,
    index=False
)
```

This allows the cleaned and analyzed data to be saved for future use.

---

# 🧑‍💻 Class and Methods

The project uses the main class:

```python
class SalesDataAnalyzer:
```

The class contains the complete functionality of the Sales Data Analysis and Visualization Tool.

---

## Constructor

```python
def __init__(self):
    self.data = pd.DataFrame()
    self.current_plot = None
```

The constructor initializes:

* An empty DataFrame
* A variable to store the current plot

It also applies Seaborn styling.

---

## Destructor

```python
def __del__(self):
```

The destructor is called when the object is destroyed.

It displays a message indicating that the object has been destroyed.

---

## Data Validation

```python
def CheckData(self):
```

This method checks whether a dataset has been loaded before performing operations.

If no data is available, the program displays:

```text
No dataset has been loaded yet.
```

---

## Datetime Detection

```python
def FindDatetimeColumn(self):
```

This method searches for a suitable date/time column in the dataset.

It checks names such as:

```text
datetime
date
date_time
timestamp
```

---

## Load Data

```python
def LoadData(self, file_path):
```

Loads the CSV dataset using:

```python
pd.read_csv()
```

It also displays:

* First five rows
* Dataset shape
* Column names

---

## Explore Data

```python
def ExploreData(self):
```

Provides options for exploring the dataset, including:

* Head
* Tail
* Columns
* Data types
* Information
* Description
* Shape
* Index
* Unique values
* Missing values

---

## Clean Data

```python
def CleanData(self):
```

Provides different data-cleaning operations such as:

* Missing value handling
* Filling numeric missing values
* Dropping missing rows
* Removing duplicates
* Datetime conversion
* Date extraction
* Time extraction
* Hour extraction
* Day extraction
* Month extraction
* Weekday extraction

---

## NumPy Operations

```python
def NumpyOperations(self):
```

Converts a selected numeric DataFrame column into a NumPy array and performs:

* Indexing
* Slicing
* Mathematical operations
* Minimum
* Maximum
* Mean
* Standard deviation
* Concatenation
* Splitting

---

## Mathematical Operations

```python
def MathematicalOperations(self):
```

Performs mathematical operations on the `money` column.

Operations include:

* Double
* Half
* Add 10
* Subtract 10
* Square

---

## Combine Data

```python
def CombineData(self, other_dataframe=None):
```

Combines DataFrames using:

* Concatenation
* Merge
* Join

---

## Split Data

```python
def SplitData(self):
```

Splits the DataFrame into groups using:

```python
groupby()
```

---

## Search, Sort and Filter

```python
def SearchSortFilter(self):
```

Allows users to:

* Search values
* Sort data
* Filter data

---

## Aggregate Functions

```python
def AggregateFunctions(self):
```

Calculates:

* Sum
* Mean
* Minimum
* Maximum
* Count
* Median

---

## Statistical Analysis

```python
def StatisticalAnalysis(self):
```

Performs:

* Descriptive statistics
* Standard deviation
* Variance
* Quantiles

---

## Pivot Table

```python
def CreatePivotTable(self):
```

Creates a Pandas pivot table using:

```python
pd.pivot_table()
```

with:

* Sum
* Mean
* Count

---

## GroupBy and Transform

```python
def GroupbyTransform(self):
```

Groups data and creates a group-wise mean using:

```python
transform("mean")
```

---

## Re-indexing

```python
def ReindexData(self):
```

Resets the DataFrame index using:

```python
reset_index()
```

---

# 🧱 Object-Oriented Programming

The project demonstrates important OOP concepts.

* **Class** – `SalesDataAnalyzer`
* **Object** – `analyzer`
* **Constructor** – `__init__()`
* **Destructor** – `__del__()`
* **Encapsulation** – Functionality is organized inside the class
* **Methods** – Different methods perform different operations

The object is created using:

```python
analyzer = SalesDataAnalyzer()
```

The application is started using:

```python
analyzer.Run()
```

---

# 🖥️ Main Menu

The application provides a menu-driven interface.

```text
==================================================
       SALES DATA ANALYSIS & VISUALIZATION
==================================================

1. Load Dataset
2. Explore Data
3. DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Export Analysis Data
9. Conclusion / Summary
10. Exit
```

Users can select an option and perform the required operation.

---

# 📋 DataFrame Operations Menu

The DataFrame Operations menu contains:

```text
1. NumPy Operations
2. Mathematical Operations
3. Combine Data
4. Split Data
5. Search / Sort / Filter
6. Aggregate Functions
7. Pivot Table
8. GroupBy / Transform
9. Re-index Data
10. Display Current Data
11. Datetime Operations
12. Back
```

This menu brings multiple data-analysis operations together in one place.

---

# 📊 Visualization Menu

The visualization section provides two choices:

```text
1. Matplotlib
2. Seaborn
3. Back
```

Matplotlib provides:

```text
Bar
Line
Scatter
Pie
Histogram
Stack Plot
Subplots
```

Seaborn provides:

```text
Box Plot
Heatmap
Count Plot
Bar Plot
Histogram
Line Plot
Scatter Plot
```

---

# 🖼️ Matplotlib Visualization Menu

```text
1. Bar Chart
2. Line Chart
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Stack Plot
7. Subplots
8. Back
```

---

# 🎨 Seaborn Visualization Menu

```text
1. Box Plot
2. Heatmap
3. Count Plot
4. Bar Plot
5. Histogram
6. Line Plot
7. Scatter Plot
8. Back
```

---

# 🔄 Program Flow

```text
Start
  ↓
Create SalesDataAnalyzer Object
  ↓
Display Main Menu
  ↓
Load Coffee Sales Dataset
  ↓
Explore / Clean / Analyze Data
  ↓
Perform DataFrame Operations
  ↓
Perform NumPy Operations
  ↓
Create Visualizations
  ↓
Save Visualization / Export Data
  ↓
Display Conclusion
  ↓
Return to Main Menu
  ↓
Choose Exit
  ↓
End
```

---

# 🗂️ Project Structure

```text
Project-9/
│
├── DataAnalysis.ipynb
├── coffe_sales.csv
└── README.md
```

### `DataAnalysis.ipynb`

Contains the complete Python implementation of the **Sales Data Analysis and Visualization Tool**.

The notebook contains:

* Imports
* `SalesDataAnalyzer` class
* Data loading
* Data exploration
* Data cleaning
* NumPy operations
* Mathematical operations
* DataFrame operations
* Statistical analysis
* Pivot tables
* GroupBy and Transform
* Matplotlib visualizations
* Seaborn visualizations
* Export functionality
* Conclusion
* Menu-driven program

### `coffe_sales.csv`

Contains the Coffee Sales dataset used for data analysis and visualization.

### `README.md`

Contains the project description, objectives, technologies, features, concepts, project structure, program flow, and instructions.

---

# ▶️ How to Run

## Step 1: Open the Project

Open the `Project-9` folder in:

* Jupyter Notebook
* JupyterLab
* VS Code

---

## Step 2: Open the Notebook

Open:

```text
DataAnalysis.ipynb
```

---

## Step 3: Keep the CSV File in the Same Folder

Make sure:

```text
coffe_sales.csv
```

is located in the same folder as the notebook.

The project structure should be:

```text
Project-9/
│
├── DataAnalysis.ipynb
├── coffe_sales.csv
└── README.md
```

---

## Step 4: Install Required Libraries

If the required libraries are not installed, run:

```python
pip install pandas numpy matplotlib seaborn
```

---

## Step 5: Load the Dataset

The CSV file is loaded using:

```python
pd.read_csv("coffe_sales.csv")
```

or through the program's file path input.

---

## Step 6: Run the Program

Run the cells containing the `SalesDataAnalyzer` class.

Then create the object:

```python
analyzer = SalesDataAnalyzer()
```

Start the application:

```python
analyzer.Run()
```

The main menu will appear.

---

# 💡 Example

## Loading the Dataset

```text
Enter CSV file path: coffe_sales.csv

Dataset loaded successfully!

First 5 Rows:

        date        cash_type        money      coffee_name
0    ...           card            ...        Latte
1    ...           card            ...        Cappuccino
2    ...           cash            ...        Americano
3    ...           card            ...        Latte
4    ...           card            ...        Espresso

Dataset Shape:

(rows, columns)
```

---

## Example of NumPy Operation

```text
Select numeric column: money

NumPy Array:

[2.50 3.00 2.75 4.00 3.50 ...]

Array Type:

<class 'numpy.ndarray'>

Array Shape:

(....,)

Array Size:

....

Minimum:

....

Maximum:

....

Mean:

....

Standard Deviation:

....
```

---

## Example of Filtering

```text
Select column: money

Enter condition:
1. >
2. <
3. >=
4. <=
5. ==

Enter value: 3

Filtered Data:

Rows where money > 3
```

---

## Example of Visualization

```text
Select Visualization:

1. Matplotlib
2. Seaborn
3. Back

Enter choice: 1

Select Matplotlib Visualization:

1. Bar Chart
2. Line Chart
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Stack Plot
7. Subplots
8. Back
```

The selected chart is then displayed.

---

# 🧩 Exception Handling

The project uses exception handling to prevent the application from stopping unexpectedly.

For example, while loading the CSV file:

```python
try:
    self.data = pd.read_csv(file_path)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error while loading dataset:")
    print(e)
```

This helps handle errors such as:

* File not found
* Invalid input
* Invalid column names
* Invalid operations
* Incorrect data types

---

# 📚 Python and Data Analysis Concepts

This project demonstrates:

* Python classes
* Objects
* Constructors
* Destructors
* Methods
* Encapsulation
* Exception handling
* Conditional statements
* Loops
* User input
* Pandas DataFrames
* NumPy arrays
* Data cleaning
* Data manipulation
* Data aggregation
* Statistical analysis
* GroupBy
* Transform
* Pivot tables
* DataFrame merging
* DataFrame joining
* Data concatenation
* Data splitting
* Searching
* Sorting
* Filtering
* Data visualization

---

# 📊 Visualization Concepts

The project provides practical experience with:

* Bar charts
* Line charts
* Scatter plots
* Pie charts
* Histograms
* Stack plots
* Subplots
* Box plots
* Heatmaps
* Count plots
* Seaborn bar plots
* Seaborn histograms
* Seaborn line plots
* Seaborn scatter plots
* Chart titles
* Axis labels
* Legends
* Tick labels
* Plot saving

---

# 🎓 Learning Outcomes

Through this project, the following concepts are practiced:

* Loading CSV data using Pandas
* Creating and manipulating DataFrames
* Exploring real-world sales data
* Handling missing values
* Removing duplicate records
* Converting date and time values
* Extracting date, time, day, month, hour, and weekday
* Converting Pandas data into NumPy arrays
* NumPy indexing and slicing
* NumPy mathematical operations
* Array concatenation and splitting
* Pandas mathematical operations
* DataFrame concatenation
* DataFrame merge
* DataFrame join
* Data splitting using GroupBy
* Searching data
* Sorting data
* Filtering data
* Aggregate functions
* Statistical functions
* Pivot tables
* GroupBy and Transform
* Re-indexing
* Matplotlib visualization
* Seaborn visualization
* Saving charts
* Exporting processed data
* Object-Oriented Programming
* Exception handling
* Menu-driven programming

---

# 💼 Business Analysis

The project can be used to understand coffee sales data from different perspectives.

The analysis can help identify:

* Total sales
* Average sales
* Maximum sales
* Minimum sales
* Number of transactions
* Most sold coffee
* Most frequently used payment method
* Sales by coffee type
* Daily sales patterns
* Hourly sales patterns
* Sales distribution
* Relationships between numerical variables

The final conclusion is generated from the available Coffee Sales dataset.

---

# 📝 Conclusion

The **Sales Data Analysis and Visualization Tool** demonstrates how Python can be used to analyze and visualize real-world sales data.

The project combines **Pandas, NumPy, Matplotlib, Seaborn, and Object-Oriented Programming** to create a practical menu-driven data analysis application.

It provides hands-on practice with **data loading, exploration, cleaning, manipulation, mathematical operations, statistical analysis, searching, sorting, filtering, aggregation, grouping, pivot tables, re-indexing, and data visualization**.

The project also demonstrates how analyzed sales data can be presented through different **Matplotlib and Seaborn visualizations** and exported for further use.

Overall, this project provides practical experience in building a complete **Sales Data Analysis and Visualization Tool using Python**.
