# Data Types

## Number (```int```, ```float```)
### Method - Initialization
```Python
x = 5
```
### Method - 6 Arithmetic Operators
```Python
3 + 2 # 5
3 + 2 # 5
3 - 2 # -1
3 * 2 # 6
3 / 2 # 1.5
3 ** 2 # 9
3 % 2 # 1
```
### Method - 6 Comparison Operators
```Python
2 > 1 # True
2 < 1 # False
2 >= 1 # True
2 <= 1 # False
2 == 1 # False
2 != 1 # True
```
### Method - 2 Type Casters
```Python
int(3 / 2) # 1
float(3 * 2) # 6.0
```
### Feature - Immutable
```Python
x = 1111
id(x)
x += 1
id(x)
y = 1112
id(y)
```

## Boolean (```bool```)
### Method - Initialization
```Python
x = True
y = False
z = 1 <= 2
```
### Method - Boolean Operators (3)
```Python
1 <= 2 and 2 >= 3 # False
1 <= 2 or 2 >= 3 # True
not(2 >= 3) # True
```
### Feature - Immutable
```Python
x = True
y = True
print(id(x))
print(id(y))
```
### Feature - Short Circuiting
```Python
True or False # True (without looking at False)
1 <= 2 or 1/0 # True (without looking at 1/0)
1 <= 2 and 1/0 # ZeroDivisionError
1 >= 2 and 1/0 # False (without looking at 1/0)
1 >= 2 or 1/0 # ZeroDivisionError
```
### Feature - Lazy Evaluation
```Python
1 or 0 # 1
1 and 0 # 0
1 or 1/0 # 1
1 and 1/0 # ZeroDivisionError
```

## String (```str```)
### Method - Initialization
```Python
x = "hello world"
```
### Method - ```len```
```Python
len("hello") # 5
```
### Feature - Immutable
```Python
x = "hello world"
y = "hello world"
print(id(x))
print(id(y))
x = "hi"
id(x)
```
### Feature - Indexable
```Python
x = "hello world"
x[1]
x[1] = 'i' # TypeError
```
### Feature - Iteration
```Python
x = "hello world"
for i in x:
 print(i)
```
### Feature - Slicing
```Python
x = "hello world"
x[1:8]
x[1:8:2]
x[1:8:-1]
x[-1:-8:1]
```
## List (```list```)
### Method - Initialization
```Python
x = [1, 2, 3]
```
### Method - ```len```
```Python
len([1, 2, 3]) # 3
```
### Method - ```append```, ```remove```, ```+```
```Python
x = [1, 2, 3]
x.append(4)
print(x)
x.remove(3)
print(x)
y = x + [1, 2, 3]
```
### Method - ```index```, ```insert```, ```pop```
```Python
x = [1, 2, 3]
x.index(2)
x.index(20) # ValueError
x.insert(4, 2) 
print(x)
x.insert(10, 100)
print(x)
```
### Feature - Mutable
```Python
x = [1, 2, 3]
print(id(x))
x.append(4)
print(id(x))
```
### Feature - Iteration
```Python
x = [1, 2, 3]
for i in x:
 print(i)
```
### Feature - Slicing
```Python
x = [1, 2, 3]
x[1:3]
x[1:3:2]
x[-1:-8:-1]
```

## Tuple (```tuple```)
  * initialization/indexing
  * comparison vs lists
## Dictionary (```dict```)
  * immutable keys
  * get/set
## Set (```set```)
  * &/|/+ operations
## Type classifications
  * Collection
  * Sequence (in, +, indexing, slicing, len, max/min, count)
  * Iteration
