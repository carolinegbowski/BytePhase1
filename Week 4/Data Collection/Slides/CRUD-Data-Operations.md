# CRUD Data Operations

## Introduction to Pandas and Numpy

### Pandas (Python Data Analysis Library)
* Most preferred way to work with Data in Python is using the Pandas package.
* Pandas can read data from a CSV, Excel, or a SQL Database, and create a Python object containing rows and columns called a ```DataFrame```.
* A ```DataFrame``` is a table similar to the tables found in Excel.
* Working with a ```DataFrame``` is easier and more efficient than than working with a `List` or `Dict` when doing large scale data operations. 
* Many common and complex data processing tasks are abstracted into Pandas functions.

#### Installation

* One easy way to install pandas is through Pip. In your terminal, you can run the following command:

##### Pip
```pip install pandas```

#### Import 

* To leverage pandas in your code, simply import the `pandas` module:

```python
import pandas as pd
```

### Numpy (Numerical Python)
* Provides efficient mathematical computation on arrays and matrices. 
* The core functionality of Numpy is its "ndarray", which stands for *n*-dimensional array data structure. 
* The numpy package contains a large collection of mathematical functions to operate on these arrays. 
* ndarray's are homogenously typed: all elements of a single array must be of the same type.
* Numpy coupled with Pandas gives you a very powerful set of tools to work with datasets in Python.

#### Installation

* One easy ways to install Numpy is through Pip. In your terminal, you can run the following commands:

##### Pip
```pip install numpy```

#### Import 

* To leverage numpy in your code, simply import the `numpy` module:

```python
import numpy as np
```

## Creating a Dataset

* Two primary components of pandas are the ```Series``` and ```DataFrame```. 
* A ```Series``` is a column. A ```DataFrame``` is a two-dimensional data structure storing a collection of Series.
* Most data operations done on a ```Series``` can be done on a ```DataFrame```. 
* There are many ways to create a Pandas ```DataFrame```. We will cover three methods: Dictionaries, Lists, and Series.

### Creating DataFrames from Dictionaries

* A simple way to create a Pandas ```DataFrame``` is using a Python dictionary.
* Each *(key, value)* pair in the Python Dictionary corresponds to a *column* in the resulting ```DataFrame```.
* Let's create a ```DataFrame``` that summarizes monthly sales from a tech store for January to May:

```python
sales_data_dict = {
    'Laptops' : [17, 12, 9, 14, 20],
    'Headphones' : [10, 13, 6, 8, 14],
    'Monitors': [6, 8, 10, 9, 15]
}

sales_df = pd.DataFrame(data=sales_data_dict)

print(sales_df)
   Laptops  Headphones  Monitors
0       17          10      6
1       12          13      8
2        9           6     10
3       14           8      9
4       20          14     15
```

#### Notes
* The length of each array in ```sales_data_dict``` must be the same or Pandas will raise a ```ValueError```.

#### Indexing
* The ```sales_df``` ```DataFrame``` does not display the months for the sales. We can fix this by adding a new column ```Month``` to the DataFrame from a list:

```python

months = ['January', 'February', 'March', 'April', 'May']
sales_df['Month'] = months

print(sales_df)
   Laptops  Headphones  Mouse     Month
0       17          10      6   January
1       12          13      8  February
2        9           6     10     March
3       14           8      9     April
4       20          14     15       May
```

* Another option is to set the ```index``` values of the ```DataFrame``` to be the specific months:

```python
sales_data_dict = {
    'Laptops' : [17, 12, 9, 14, 20],
    'Headphones' : [10, 13, 6, 8, 14],
    'Monitors': [6, 8, 10, 9, 15]
}
months = ['January', 'February', 'March', 'April', 'May']

sales_df = pd.DataFrame(data=sales_data_dict, index=months)

print(sales_df)
          Laptops  Headphones  Mouse
January        17          10      6
February       12          13      8
March           9           6     10
April          14           8      9
May            20          14     15
```

### Creating DataFrames from Lists

* Another method to create a Pandas ```DataFrame``` is from lists. For multi-dimensional data, this would require a list of lists.
* Each list in the list set corresponds to a row in the Pandas ```DataFrame```.
```python
sales_data_list = [
    [14, 10, 6],
    [12, 13, 8],
    [9, 6, 10],
    [14, 8, 9],
    [20, 14, 15]
]
sales_data_columns = ['Laptops', 'Headphones', 'Monitors']
months = ['January', 'February', 'March', 'April', 'May']

sales_df = pd.DataFrame(data=sales_data_list, columns=sales_data_columns, index=months)

print(sales_df)
          Laptops  Headphones  Mouse
January        17          10      6
February       12          13      8
March           9           6     10
April          14           8      9
May            20          14     15
```
* Here we need to explicitly specify the columns of the Pandas ```DatFrame``` and pass that in as an argument.

### Creating DataFrames from Series

* A Pandas ```Series``` is a one-dimensional array capable of holding data of any type (integer, string, float, python objects, etc).
* A `Series` is a dynamic container for it's size and type.
* The benefit of ```Series``` over python arrays is you have efficient Pandas functions that can be operated on ```Series``` to do specific data calculations (ex: ```df.mean()```).
* The series object has a number of attributes. Two important attributes are the ```dtype``` and the ```name```. 
* The dtype is the type of the underlying data contained in the Series array.
* The name is the name of the Series array, which is also the name of the column in a Pandas ```DataFrame```. 
* All columns of a Pandas ```DataFrame``` are ```Series```. For example:

```python
sales_data_dict = {
    'Laptops' : [17, 12, 9, 14, 20],
    'Headphones' : [10, 13, 6, 8, 14],
    'Monitors': [6, 8, 10, 9, 15]
}
months = ['January', 'February', 'March', 'April', 'May']

sales_df = pd.DataFrame(data=sales_data_dict, index=months)

print(sales_df['Laptops'])
January    14
February   12
March       9
April      14
May        20
Name: Laptops, dtype: int64

type(sales_df['Laptops'])
<class 'pandas.core.series.Series'>
```

* We can initialize a Pandas ```Series``` from a list, and pass the ```Series``` into a ```DataFrame``` through a Dictionary:

```python

laptop_sales_list = [17, 12, 9, 14, 20]
headphone_sales_list = [10, 13, 6, 8, 14]
monitor_sales_list = [6, 8, 10, 9, 15]

laptop_sales_series = pd.Series(laptop_sales_list)
headphone_sales_series = pd.Series(headphone_sales_list)
monitor_sales_series = pd.Series(monitor_sales_list)

sales_data_dict = {
    'Laptops' : laptop_sales_series,
    'Headphones': headphone_sales_series,
    'Monitors': monitor_sales_series
}

sales_df = pd.DataFrame(data=sales_data_dict)

print(sales_df)
   Laptops  Headphones  Monitors
0       17          10         6
1       12          13         8
2        9           6        10
3       14           8         9
4       20          14        15
```

* We can modify the indices of the ```DataFrame``` post creation:
```python

months = ['January', 'February', 'March', 'April', 'May']
sales_df.index = months

print(sales_df)
          Laptops  Headphones  Monitors
January        17          10         6
February       12          13         8
March           9           6        10
April          14           8         9
May            20          14        15
```


### Testing
* Testing code on a large dataset can take multiple hours of compute time.
* It is recommended to create a Pandas ```DataFrame``` for code creation and unit testing. 

## Reading and Writing from a CSV

### Writing CSV Files with Pandas

* Pandas makes it easy to read and write data in different file formats. 
*  we can use Pandas ```to_csv()``` method to save an existing ```DataFrame``` that is already in memory.
* ```to_csv()``` is a method of a ```DataFrame``` object, so we can call it directly from our ```DataFrame```:

```python
sales_df.to_csv("./Sales Data.csv")
```

* We can specify if we would like to save the ```index``` values of our ```DataFrame``` by using the optional ```index``` argument. By default, this is set to ```True```:
```python
sales_df.to_csv("./Sales Data.csv", index=False)
```

* We can specify the list of columns we would like to save from our `DataFrame` using the `columns` argument:
```python
sales_df.to_csv("./Sales Data.csv", columns=['Laptops','Headphones'])
```

### Reading CSV Files with Pandas

* We can use Pandas ```pd.read_csv()``` method to read a ```DataFrame``` into memory.
* ```pd.read_csv()``` is **not** a method of a ```DataFrame``` object, but instead we call it through the Pandas module:

```python
sales_df = pd.read_csv("./Sales Data.csv")

print(sales_df)
  Unnamed: 0  Laptops  Headphones  Monitors
0    January       17          10         6
1   February       12          13         8
2      March        9           6        10
3      April       14           8         9
4        May       20          14        15
```

* When using ```pd.read_csv()```, Pandas does not read the index of the ```DataFrame``` by default.
* If the ```csv``` file contains indices, we need to specify this explicity through the ```index_col``` argument. 
* The ```index_col``` argument tells you which column of the ```csv``` file to use as the row labels (or indices) of the ```DataFrame```.
* Typically ```index_col``` is set to ```0``` as the first column of the csv file.

```python
sales_df = pd.read_csv("./Sales Data.csv", index_col=0)

print(sales_df)
          Laptops  Headphones  Monitors
January        17          10         6
February       12          13         8
March           9           6        10
April          14           8         9
May            20          14        15
```

* Three important arguments to the ```pd.read_csv()``` method are the ```names```, ```sep```, and ```usecols```.
* The ```names``` arugment specifies a **list** of column names to use for the ```DataFrame```, assuming the ```csv``` file does not contain any column names.
* The ```sep``` argument specifies a **string** which represents the delimiter to use when parsing the ```csv``` file into a ```DataFrame```. 
* The ```usecols``` argument specifies a **list** of strings or integers that represent the column names or numbers you would like to import. For example:

```python
sales_df = pd.read_csv("./Sales Data.csv", sep=",", usecols=['Laptops', 'Headphones'])

print(sales_df)
   Laptops  Headphones
0       17          10
1       12          13
2        9           6
3       14           8
4       20          14
```

* The ```usecols``` argument results in much faster parsing time and lower memory usage.
* It is recommended to use the ```usecols``` argument for large datasets and only read in the columns required.

## Reading and Writing from a Pickle

### Introduction to Pickle

* Allows for (de)serialization of a Python object.
* Pickling is a way to covert a python object in memory (list, dict, etc.) into a character stream (serialization) that can be saved on to your hard-drive.
* This is useful when we want to pass large data between Python programs.
* To leverage pickle in your code, simply import the `pickle` module:

```python
import pickle
```

* You can save any Python object using the `dump` method in the `pickle` module.

```python
# Pickling the Sales list into a Pickle File
laptop_sales_list = [17, 12, 9, 14, 20]

laptop_sales_file = open("./laptop_sales.pkl", 'wb')
pickle.dump(laptop_sales_list, laptop_sales_file)
laptop_sales_file.close()
```

* You can read any Python object using the `load` method in the `pickle` module.
```python
# Loading the Sales list from a Pickle File
laptop_sales_file = open("./laptop_sales.pkl", 'r')
laptop_sales_list = pickle.load("./laptop_sales.pkl")
laptop_sales_file.close()

print(laptop_sales_list)
[17, 12, 9, 14, 20]
```

### Writing Pickle files with Pandas

* Although it is possible to read and write a `DataFrame` using the `pickle` module, Pandas offers a built in method to read and write a `DataFrame` using `pickle`.
* You can save a `DataFrame` using the `DataFrame` method `to_pickle()`.
* `to_pickle()` is a method of a `DataFrame` object, so we can call it directly from our `DataFrame` in memory:

```python
sales_data_dict = {
    'Laptops' : [17, 12, 9, 14, 20],
    'Headphones' : [10, 13, 6, 8, 14],
    'Monitors': [6, 8, 10, 9, 15]
}
months = ['January', 'February', 'March', 'April', 'May']

sales_df = pd.DataFrame(data=sales_data_dict, index=months)

sales_df.to_pickle("Sales Data.pkl")
```

* If we want to save only specific columns of the DataFrame, we can subset the data by passing in a list of column names (or column numbers) to the `DataFrame`:

```python
sales_data_dict = {
    'Laptops' : [17, 12, 9, 14, 20],
    'Headphones' : [10, 13, 6, 8, 14],
    'Monitors': [6, 8, 10, 9, 15]
}
months = ['January', 'February', 'March', 'April', 'May']

sales_df = pd.DataFrame(data=sales_data_dict, index=months)

sales_df[['Laptops','Headphones']].to_pickle("Sales Data Subset.pkl")
```

* Pickling a `DataFrame` serliazes the object, so we save the object exactly how it was in memory.

### Reading Pickle files with Pandas

* We can use Pandas ```pd.read_pickle()``` method to read a ```DataFrame``` into memory.
* ```python pd.read_pickle()``` is **not** a method of a ```DataFrame``` object, but instead we call it through the Pandas module:

```python

sales_df = pd.read_pickle("Sales Data.pkl")

print(sales_df)
          Laptops  Headphones  Monitors
January        17          10         6
February       12          13         8
March           9           6        10
April          14           8         9
May            20          14        15
```

* One advantage of pickling is that it has significantly faster read and write times than working with CSV files.
* One disadvantage of pickling is that it takes more disk space to save the `DataFrame` in comparison with saving a `csv` file.
