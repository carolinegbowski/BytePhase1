# Creating, Reading, and Writing Data

## Introduction to Pandas and Numpy

### Pandas 
* The most preferred way to work with Data in Python is using the Pandas package, which stands for "Python Data Analysis Library".
* Pandas can read data from a CSV, Excel, or Pickle file, or an SQL Database, and create a Python object containing rows and columns called a DataFrame.
* A DataFrame is a table very similar to the tables found in Excel or R.
* Working with DataFrames is much easier and more efficient than than working with lists and dictionaries when doing large scale data operations. 
* Many common and complex data processing tasks are abstracted away into efficient Pandas functions.

#### Installation

* There are multiple ways to install Pandas. You can find the full installation document [here](https://pandas.pydata.org/pandas-docs/stable/install.html).
* Two easy ways to install pandas are through Anaconda or Pip. In your terminal, you can run the following commands:

##### Conda
```conda install pandas```

##### Pip
```pip install pandas```

#### Import 

* To import pandas, you can include the following line in your python code:

```python
import pandas as pd
```

### Numpy 
* Numpy is a module in Python that provides quick and efficient mathematical computation on arrays and matrices. Numpy stands for "Numerical Python". 
* The core functionality of Numpy is its "ndarray", which stands for _n_-dimensional array data structure. The numpy package contains a large collection of mathematical functions to operate on these arrays. 
* In constract with Python's built-in list data structure (which is a dynamic array), ndarray's are homogenously typed: all elements of a single array must be of the same type.
* Numpy coupled with Pandas gives you a very powerful set of tools to work with datasets in Python.

#### Installation

* There are multiple ways to install Numpy. You can find the full installation document [here](https://scipy.org/install.html).
* One easy ways to install Numpy is through Pip. In your terminal, you can run the following commands:

##### Pip
```pip install numpy```

#### Import 

* To import numpy, you can include the following line in your python code:

```python
import numpy as np
```

## Creating a Dataset
## Reading from CSV and Pickle
## Writing to CSV and Pickle