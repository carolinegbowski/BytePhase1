# Functions

# [Functions](https://github.com/ByteAcademyCo/Phase1-Python/blob/master/Week%201/Introduction%20To%20Python/Slides/Functions.md)
## Basics
### Python logic unit abstraction model
### Formally define: keywords, function name/parameters/arguments/body

## Scope
### Leaky
### LEGB (global/nonlocal)

## Functional Programming
### Lambda functions
### Map and Filter

## Advanced Functions
### First class functions
* First class citizens
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
