**# NumPy Analyzer**

**## 📌 Project Overview**

The **NumPy Analyzer** is a menu-driven Python application developed using **NumPy** and **Object-Oriented Programming (OOP)** principles.

This project allows users to create and analyze **1D, 2D, and 3D NumPy arrays** and perform various mathematical, statistical, searching, sorting, filtering, combining, and splitting operations.

The complete functionality is encapsulated inside the **`DataAnalytics`** class.

**---**

**## 🎯 Objective**

Develop a **NumPy Analyzer** that integrates NumPy functionalities and OOP principles.

The application allows users to:

* Create 1D, 2D, and 3D arrays
* Perform indexing and slicing
* Perform mathematical operations
* Calculate dot product and matrix multiplication
* Combine and split arrays
* Search for values
* Sort arrays in ascending and descending order
* Filter values using conditions
* Calculate aggregate functions
* Calculate statistical functions
* Calculate correlation coefficients
* Use constructors, encapsulation, private methods, class methods, and static methods
* Operate the application through a menu-driven interface

**---**

**## 🛠️ Technologies Used**

* **Python**
* **NumPy**
* **Jupyter Notebook**

**---**

**## 📚 NumPy Concepts Used**

### **1. Array Creation**

The program allows users to create:

* **1D Array**
* **2D Array**
* **3D Array**

Arrays are created using:

```python
np.array()
```

For 2D and 3D arrays, the `reshape()` function is used to give the array the required dimensions.

```python
np.array(values).reshape(rows, columns)
```

```python
np.array(values).reshape(layers, rows, columns)
```

### **2. Array Properties**

The program uses NumPy array properties such as:

```python
self.array.size
```

to check the number of elements in the array.

```python
self.array.ndim
```

is used to identify whether the array is 1D, 2D, or 3D.

```python
self.array.shape
```

is used to obtain the dimensions of the array.

**---**

**## 🔢 Indexing and Slicing**

The program supports indexing and slicing for **1D, 2D, and 3D arrays**.

### **Indexing**

For a 1D array:

```python
self.array[index]
```

For a 2D array:

```python
self.array[row, column]
```

For a 3D array:

```python
self.array[layer, row, column]
```

### **Slicing**

The program allows users to enter ranges such as:

```text
0:2
```

For 2D arrays:

```python
self.array[row_start:row_end, column_start:column_end]
```

For 3D arrays:

```python
self.array[
    layer_start:layer_end,
    row_start:row_end,
    column_start:column_end
]
```

**---**

**## ➕ Mathematical Operations**

The program performs the following mathematical operations:

* Addition
* Subtraction
* Multiplication
* Division
* Dot Product
* Matrix Multiplication

### **Element-wise Operations**

Element-wise operations are performed using:

```python
self.array + second
```

```python
self.array - second
```

```python
self.array * second
```

```python
self.array / second
```

The program also checks for division by zero before performing division.

### **Dot Product**

The dot product is calculated using:

```python
np.dot()
```

### **Matrix Multiplication**

Matrix multiplication is performed using:

```python
np.matmul()
```

Matrix multiplication is supported for **2D arrays**.

**---**

**## 🔗 Combining Arrays**

The program provides three methods for combining arrays:

### **1. Vertical Stack**

```python
np.vstack()
```

### **2. Horizontal Stack**

```python
np.hstack()
```

### **3. Concatenation**

```python
np.concatenate()
```

The user provides another array with the required shape before combining.

**---**

**## ✂️ Splitting Arrays**

The program allows users to divide an array into multiple smaller arrays.

It uses:

```python
np.array_split()
```

The user can specify the number of parts into which the array should be divided.

The program then displays each part separately.

**---**

**## 🔎 Searching Values**

The program allows users to search for a specific value in an array.

It uses:

```python
np.where()
```

Example:

```python
indexes = np.where(self.array == value)
```

If the value exists, its index or indexes are displayed.

If the value does not exist, the program displays:

```text
Value not found.
```

**---**

**## 🔢 Sorting Arrays**

The program supports:

* Ascending sorting
* Descending sorting

It uses:

```python
np.sort()
```

The sorting is applied along the last axis of the array.

For descending order, the sorted result is reversed using:

```python
np.flip()
```

**---**

**## 🎯 Filtering Values**

The program allows users to filter array values according to different conditions.

Available conditions are:

* Greater than
* Less than
* Equal to
* Greater than or equal to
* Less than or equal to

Examples:

```python
self.array > value
```

```python
self.array < value
```

```python
self.array == value
```

```python
self.array >= value
```

```python
self.array <= value
```

Boolean indexing is used to display the filtered values.

**---**

**## 📊 Aggregates and Statistics**

The program calculates different aggregate and statistical values.

### **1. Sum**

```python
np.sum()
```

Calculates the total of all array elements.

### **2. Mean**

```python
np.mean()
```

Calculates the average of the array elements.

### **3. Median**

```python
np.median()
```

Calculates the middle value of the data.

### **4. Standard Deviation**

```python
np.std()
```

Measures the amount of variation in the data.

### **5. Variance**

```python
np.var()
```

Calculates the variance of the array elements.

### **6. Minimum**

```python
np.min()
```

Finds the smallest value.

### **7. Maximum**

```python
np.max()
```

Finds the largest value.

### **8. Percentile**

```python
np.percentile()
```

Calculates the value below which a given percentage of data falls.

The user can enter a percentile between **0 and 100**.

### **9. Correlation Coefficient**

```python
np.corrcoef()
```

Calculates the correlation coefficient between two arrays.

The arrays are flattened using:

```python
reshape(-1)
```

before calculating the correlation.

**---**

**## 🧑‍💻 Class and Methods**

The project uses the following main class:

```python
class DataAnalytics:
```

The class encapsulates the complete functionality of the NumPy Analyzer.

### **Constructor**

```python
def __init__(self):
    self.array = np.array([])
```

The constructor initializes an empty NumPy array.

### **Static Method**

```python
@staticmethod
def ShowWelcome():
```

Displays the welcome message.

### **Class Method**

```python
@classmethod
def ProjectInfo(cls):
```

Displays project information and the class name.

### **Private Method**

```python
def __GetSecondArray(self, shape):
```

This private method internally creates another array with the required shape for operations such as combining, dot product, matrix multiplication, and correlation.

### **Input Validation Methods**

```python
def GetInteger(self, message):
```

Validates integer input from the user.

```python
def GetArrayValues(self, total):
```

Validates the number and type of values entered for creating an array.

### **Array Validation**

```python
def CheckArray(self):
```

Checks whether an array has been created before performing operations.

**---**

**## 🧱 Object-Oriented Programming**

The project demonstrates the following OOP concepts:

* **Class** – `DataAnalytics`
* **Object** – `analyzer`
* **Constructor** – `__init__()`
* **Encapsulation** – All functionality is contained inside the class
* **Private Method** – `__GetSecondArray()`
* **Class Method** – `ProjectInfo()`
* **Static Method** – `ShowWelcome()`

The object is created using:

```python
analyzer = DataAnalytics()
```

The main application is started using:

```python
analyzer.MainMenu()
```

**---**

**## 🖥️ Main Menu**

The program provides a menu-driven interface:

```text
Welcome to the NumPy Analyzer!

Choose an option:

1. Create a Numpy Array

2. Perform Mathematical Operations

3. Combine or Split Arrays

4. Search, Sort, or Filter Arrays

5. Compute Aggregates and Statistics

6. Exit

Enter your choice:
```

Users can select different operations from the main menu and exit the program using option **6**.

**---**

**## 📂 Project Structure**

```text
Project-8/
│
├── Numpy.ipynb
└── README.md
```

### **Numpy.ipynb**

Contains the complete Python implementation of the NumPy Analyzer.

### **README.md**

Contains the project description, objectives, features, concepts, structure, and instructions.

**---**

**## ▶️ How to Run**

### **Step 1: Open the Project**

Open the `Project-8` folder in **Jupyter Notebook** or **VS Code**.

### **Step 2: Open the Notebook**

Open:

```text
Numpy.ipynb
```

### **Step 3: Install NumPy**

If NumPy is not already installed:

```python
pip install numpy
```

### **Step 4: Run the Program**

Run the cells containing the `DataAnalytics` class and:

```python
analyzer = DataAnalytics()
analyzer.MainMenu()
```

The NumPy Analyzer menu will appear.

**---**

**## 💡 Example**

Example of creating a 2D array:

```text
Array Creation:

Select the type of array to create:

1. 1D Array

2. 2D Array

3. 3D Array

Enter your choice: 2

Enter the number of rows: 2

Enter the number of columns: 3

Enter 6 elements for the array separated by space: 10 20 30 40 50 60

Array created successfully:

[[10 20 30]
 [40 50 60]]
```

The user can then choose indexing or slicing operations.

Example of slicing:

```text
Choose an operation:

1. Indexing

2. Slicing

3. Go Back

Enter your choice: 2

Enter the row range (start:end): 0:2

Enter the column range (start:end): 1:3

Sliced Array:

[[20 30]
 [50 60]]
```

**---**

**## 🔄 Program Flow**

```text
Start
  ↓
Create DataAnalytics Object
  ↓
Display Main Menu
  ↓
Choose Operation
  ↓
Create / Analyze / Modify Array
  ↓
Display Result
  ↓
Return to Main Menu
  ↓
Choose Exit
  ↓
End
```

**---**

**## 🎓 Learning Outcomes**

Through this project, the following concepts are practiced:

* NumPy array creation and manipulation
* 1D, 2D, and 3D arrays
* Indexing and slicing
* Element-wise mathematical operations
* Dot product and matrix multiplication
* Array concatenation and stacking
* Array splitting
* Searching and sorting
* Boolean filtering
* Aggregate functions
* Statistical functions
* Correlation coefficients
* Python input validation
* Object-Oriented Programming
* Constructors and encapsulation
* Private methods
* Static methods and class methods
* Menu-driven programming

**---**

**## ✅ Conclusion**

The **NumPy Analyzer** demonstrates how NumPy can be combined with Object-Oriented Programming to create a practical, menu-driven data analysis toolkit.

The project provides hands-on practice with **array manipulation, mathematical operations, searching, sorting, filtering, aggregation, statistics, and OOP concepts** using Python and NumPy.
