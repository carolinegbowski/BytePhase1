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
* If only one block should be excuted, use if/elif
* If possibly more than 1 block should be executed, use if/if
```Python
a = 1
b = 2
if (a < b):
  print(f'{a} is less than {b}')
if (a > b):
  print(f'{a} is greater than {b}')
if (a == b):
  print(f'{a} equals {b}')
```

## Iteration
### Basics
* Iteration is the repetition of a process in order to generate a sequence of outcomes
```Python
x = 0
while x < 5:
  x = x + 1
  print(f'x is {x}')
```

### While vs For loop
* Preferred way of iteration in Python is using ```for```
```Python
for(x in range(0, 5, 1)):
  print(f'x is {x}')
for(x in range(5)):
  print(f'x is {x}')
```
* Range parameters behave the same as slicing

### Iteration over range vs set
* Both have valid use cases
```Python
L = [0, 1, 2, 3, 4]
for element in L:
  print(element)
for index in range(len(L)):
  print(L[index])
```

### Comprehensions
* An efficient way to generate lists (and other containers) using iteration
```Python
L_bad = []
for i in range(10):
  if i % 2 == 0:
    L_bad.append(i)
L_good = [i for i in range(10) if i % 2 == 0]
```
* Can also be done with dict and set
```Python
s = {i for i in range(10) if i % 2 == 0}
d = {i:i for i in range(10) if i % 2 == 0}
```
