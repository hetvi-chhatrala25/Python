# NumPy Analyzer

## 📌 Project Overview

NumPy Analyzer is a menu-driven Python project developed using the **NumPy** library.

This project is created inside the **Project-8** folder and allows users to create and work with **1D, 2D, and 3D NumPy arrays** through a simple command-line menu.

It demonstrates important NumPy concepts such as:

* Array creation
* Array properties
* Indexing
* Slicing
* Mathematical operations
* Dot product
* Matrix multiplication
* Combining arrays
* Splitting arrays
* Searching values
* Sorting arrays
* Filtering values
* Aggregate functions
* Statistical functions
* Percentile
* Correlation
* Object-Oriented Programming
* Menu-driven programming

---

## 🎯 Objectives

* To understand the basics of NumPy.
* To create 1D, 2D, and 3D arrays.
* To perform operations on NumPy arrays.
* To understand indexing and slicing.
* To perform mathematical and matrix operations.
* To combine and split arrays.
* To search, sort, and filter array values.
* To calculate aggregate and statistical values.
* To apply basic Object-Oriented Programming concepts.
* To create a menu-driven NumPy application.

---

## 🛠️ Technologies Used

* **Python**
* **NumPy**
* **Object-Oriented Programming (OOP)**

---

## 📚 NumPy Concepts Used

### 1. Array Creation

The program supports:

* 1D Array
* 2D Array
* 3D Array

```python
np.array([10, 20, 30])
```

For 2D arrays:

```python
np.array([10, 20, 30, 40]).reshape(2, 2)
```

For 3D arrays:

```python
np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(2, 2, 2)
```

---

### 2. Array Properties

The project works with important array properties.

#### Shape

```python
self.array.shape
```

Returns the size of the array along each dimension.

#### Size

```python
self.array.size
```

Returns the total number of elements in the array.

#### Number of Dimensions

```python
self.array.ndim
```

Returns the number of dimensions of the array.

---

# 🔍 Indexing and Slicing

The project supports indexing and slicing for **1D, 2D, and 3D arrays**.

### 1D Indexing

```python
self.array[index]
```

Accesses an element using its index.

### 2D Indexing

```python
self.array[row, col]
```

Accesses an element using row and column indexes.

### 3D Indexing

```python
self.array[layer, row, col]
```

Accesses an element using layer, row, and column indexes.

### 1D Slicing

```python
self.array[start:stop:step]
```

Extracts a portion of a 1D array.

### 2D Slicing

```python
self.array[row_start:row_stop, col_start:col_stop]
```

Extracts selected rows and columns from a 2D array.

### 3D Slicing

```python
self.array[
    layer_start:layer_stop,
    row_start:row_stop,
    col_start:col_stop
]
```

Extracts selected layers, rows, and columns from a 3D array.

---

# ➕ Mathematical Operations

The project provides the following mathematical operations.

### Addition

```python
self.array + second_array
```

Adds corresponding elements of two arrays.

### Subtraction

```python
self.array - second_array
```

Subtracts corresponding elements of two arrays.

### Multiplication

```python
self.array * second_array
```

Performs element-wise multiplication.

### Division

```python
self.array / second_array
```

Performs element-wise division.

### Dot Product

```python
np.dot(self.array, second_array)
```

Calculates the dot product of two arrays.

### Matrix Multiplication

```python
np.matmul(self.array, second_array)
```

Performs matrix multiplication.

---

# 🔗 Combining Arrays

The project supports three methods for combining arrays.

### Concatenate

```python
np.concatenate((self.array, second_array))
```

Combines arrays along an existing axis.

### Vertical Stack

```python
np.vstack((self.array, second_array))
```

Stacks arrays vertically.

### Horizontal Stack

```python
np.hstack((self.array, second_array))
```

Stacks arrays horizontally.

---

# ✂️ Splitting Arrays

The project uses `np.split()` to divide an array into multiple parts.

```python
np.split(self.array, number)
```

Example:

```python
array = np.array([10, 20, 30, 40])

np.split(array, 2)
```

Output:

```text
[array([10, 20]), array([30, 40])]
```

---

# 🔎 Searching Values

The project uses `np.where()` to search for a particular value.

```python
np.where(self.array == value)
```

It supports searching in:

* 1D arrays
* 2D arrays
* 3D arrays

Example:

```text
Array:
[[10 20]
 [30 20]]

Search value: 20

Index:
(0, 1)
(1, 1)
```

---

# 🔃 Sorting Arrays

The project supports:

* Ascending order
* Descending order

### Ascending

```python
np.sort(self.array)
```

Sorts the array in ascending order.

### Descending

For a 1D array:

```python
sorted_array[::-1]
```

For a 2D array:

```python
sorted_array[:, ::-1]
```

For a 3D array:

```python
sorted_array[:, :, ::-1]
```

---

# 🔍 Filtering Values

The project uses Boolean indexing to filter values.

### Greater Than

```python
self.array[self.array > value]
```

### Less Than

```python
self.array[self.array < value]
```

### Equal To

```python
self.array[self.array == value]
```

### Greater Than or Equal To

```python
self.array[self.array >= value]
```

### Less Than or Equal To

```python
self.array[self.array <= value]
```

---

# 📊 Aggregates and Statistics

The project provides the following statistical operations.

### Sum

```python
np.sum(self.array)
```

Calculates the sum of all elements.

### Mean

```python
np.mean(self.array)
```

Calculates the average of the elements.

### Median

```python
np.median(self.array)
```

Calculates the middle value.

### Standard Deviation

```python
np.std(self.array)
```

Calculates the standard deviation.

### Variance

```python
np.var(self.array)
```

Calculates the variance.

### Minimum

```python
np.min(self.array)
```

Returns the smallest value.

### Maximum

```python
np.max(self.array)
```

Returns the largest value.

### Percentile

```python
np.percentile(self.array, percentile)
```

Calculates the specified percentile.

### Correlation

```python
np.corrcoef(
    self.array.reshape(-1),
    second_array.reshape(-1)
)
```

Calculates the correlation between two arrays.

---

# 📋 Main Menu

The program provides the following main menu:

```text
Welcome to the NumPy Analyzer!

Choose an option:
1. Create a NumPy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
```

---

# 🧩 Class and Methods

The project uses a class named `NumPy`.

```python
class NumPy:
```

| Method                     | Description                                   |
| -------------------------- | --------------------------------------------- |
| `__init__()`               | Initializes the NumPy array                   |
| `CheckArray()`             | Checks whether an array has been created      |
| `CreateArray()`            | Creates 1D, 2D, or 3D arrays                  |
| `IndexingSlicing()`        | Performs indexing and slicing                 |
| `MathematicalOperations()` | Performs mathematical operations              |
| `CombineSplit()`           | Combines or splits arrays                     |
| `SearchSortFilter()`       | Searches, sorts, and filters arrays           |
| `AggregatesStatistics()`   | Performs aggregate and statistical operations |
| `MainMenu()`               | Controls the main menu                        |

---

# 🛡️ Input Validation

The project performs basic input validation.

While creating an array, the program checks whether the number of entered values matches the required number of elements.

```python
if len(values) != n:
    print("Number of values does not match.")
    return
```

The same validation is used for 2D and 3D arrays.

The program also checks whether an array has been created before performing operations.

```python
if self.array.size == 0:
    print("\nNo array has been created yet.")
    return False
```

---

# 🧠 Object-Oriented Programming

The project uses basic Object-Oriented Programming concepts.

### Class

The `NumPy` class groups related NumPy operations together.

```python
class NumPy:
```

### Constructor

The `__init__()` method initializes the array when an object is created.

```python
def __init__(self):
    self.array = np.array([])
```

### Object

An object of the class is created using:

```python
analyzer = NumPy()
```

### Encapsulation

The array is stored as an instance variable:

```python
self.array
```

and the different operations are handled through class methods.

---

# 📁 Project Structure

```text
Project-8/
│
├── Numpy1.py
│
└── README.md
```

### `Numpy1.py`

Contains the complete NumPy Analyzer program, including:

* NumPy array creation
* Indexing and slicing
* Mathematical operations
* Combining and splitting
* Searching
* Sorting
* Filtering
* Aggregates
* Statistics
* Menu-driven interface

### `README.md`

Contains the complete documentation and details about the NumPy Analyzer project.

---

# ▶️ How to Run

## Step 1: Install Python

Check whether Python is installed:

```bash
python --version
```

---

## Step 2: Install NumPy

Install NumPy using:

```bash
pip install numpy
```

---

## Step 3: Open the Project Folder

Open the `Project-8` folder in your terminal or command prompt.

```bash
cd Project-8
```

---

## Step 4: Run the Program

Run the Python file:

```bash
python Numpy1.py
```

---

# 💻 Example

### Creating a 2D Array

```text
Welcome to the NumPy Analyzer!

Choose an option:
1. Create a NumPy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit

Enter your choice: 1

Array Creation:

Select the type of array to create:
1. 1D Array
2. 2D Array
3. 3D Array

Enter your choice: 2

Enter number of rows: 2
Enter number of columns: 3
Enter values: 10 20 30 40 50 60
```

Output:

```text
Array Created:
[[10 20 30]
 [40 50 60]]

Array Properties:
Shape: (2, 3)
Size: 6
```

---

# 🔄 Program Flow

```text
Start
  │
  ▼
Create NumPy Analyzer Object
  │
  ▼
Display Main Menu
  │
  ├── Create NumPy Array
  │     ├── 1D Array
  │     ├── 2D Array
  │     └── 3D Array
  │
  ├── Mathematical Operations
  │     ├── Addition
  │     ├── Subtraction
  │     ├── Multiplication
  │     ├── Division
  │     ├── Dot Product
  │     └── Matrix Multiplication
  │
  ├── Combine or Split Arrays
  │     ├── Concatenate
  │     ├── Vertical Stack
  │     ├── Horizontal Stack
  │     └── Split
  │
  ├── Search, Sort, or Filter
  │     ├── Search
  │     ├── Sort
  │     └── Filter
  │
  ├── Aggregates and Statistics
  │     ├── Sum
  │     ├── Mean
  │     ├── Median
  │     ├── Standard Deviation
  │     ├── Variance
  │     ├── Minimum
  │     ├── Maximum
  │     ├── Percentile
  │     └── Correlation
  │
  └── Exit
        │
        ▼
       End
```

---

# 🎓 Learning Outcomes

Through this project, the following concepts are practiced:

* NumPy array creation
* 1D, 2D, and 3D arrays
* Array dimensions
* `shape`
* `size`
* `ndim`
* `reshape()`
* Indexing
* Slicing
* Addition
* Subtraction
* Multiplication
* Division
* `np.dot()`
* `np.matmul()`
* `np.concatenate()`
* `np.vstack()`
* `np.hstack()`
* `np.split()`
* `np.where()`
* `np.sort()`
* Boolean indexing
* `np.sum()`
* `np.mean()`
* `np.median()`
* `np.std()`
* `np.var()`
* `np.min()`
* `np.max()`
* `np.percentile()`
* `np.corrcoef()`
* Python classes
* Constructors
* Encapsulation
* Object-Oriented Programming basics
* Menu-driven programming
* Input validation

---

# 📌 Conclusion

NumPy Analyzer is a practical menu-driven Python project that combines important NumPy concepts into one application.

It provides an interactive way to create arrays and perform mathematical, array manipulation, searching, sorting, filtering, and statistical operations.

The project helps build a strong foundation in NumPy and demonstrates how NumPy can be used for numerical and array-based operations in Python.
