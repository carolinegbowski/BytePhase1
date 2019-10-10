# Functions

## Basics
### Python Memory Manipulation
```Python
a = 1
def f(x):
 return x + 1
b = f(a)
```

### Formal Definition
![bla(/Images/test.png)
* keywords
* function name
* parameters and arguments
* body

## Scope
### Leaky
### LEGB (global/nonlocal)

## Functional Programming
### Lambda functions
### Map and Filter

## Advanced Functions
### First class functions
```Python
 def adder(n):
  def add_n(x):
   return n+x
  return add_n
 add5 = adder(5)
 add10 = adder(10)
 print(add5(3)); print(add5(10))
 print(add10(3)); print(add10(3))
 ```
 
### Args/Kwargs
### Decorators
