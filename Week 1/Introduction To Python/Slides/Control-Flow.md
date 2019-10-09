# Control Flow

## Conditionals
### Basics
```Python
a = 1
b = 2
if (a < b):
  print('{a} is less than {b}')
```
* Indentation and blocks
* Boolean expressions
* else
```Python
a = 1
b = 2
if (a < b):
  print(f'{a} is less than {b}')
else:
  print(f'{a} is greater than {b}')
```
* elif
```Python
a = 1
b = 2
if (a < b):
  print(f'{a} is less than {b}')
elif (a > b):
  print(f'{a} is greater than {b}')
else:
  print(f'{a} equals {b}')
```

### Ternary Operator
* Can write if/else in one line if expressions are relatively simple
```Python
a = 1
b = 2
# [on_true] if [expression] else [on_false]
print(f'{a} is less than {b}') if a < b else print(f'{b} is less than {a}')
```
* Can combine these, but not recommended
```Python
a = 1
b = 2
print(f'{a} is less than {b}') if a < b else print(f'{b} is less than {a}') if b < a else print(f'{a} equals {b}')
```

### If/if vs if/else


## Iteration
### Basics
### While vs For loop
### Iteration over range vs set
### Comprehensions
* Basics
* Set, dict comprehension
* Generator comprehensions
