
# Hello World

## Running Python

### Invoking the Interpreter
* Through command prompt
```
python hello-world.py
```

### Using an editor
* Definition window
* Interaction window

## Variables
### Name bindings (=)
* This creates an object x. An object consists of 3 parts
  * A name (x)
  * A reference (the value it points at)
  * An ID (a unique identifer for the reference)
```Python
x = 1
```

### Memory (id)
* Functions and Python memory
```Python
x = 1
id(x)
x = 2
id(x)
```
### Types (type)
* Type function and the string type
```Python
x = 1
type(x)
x = "Hello World"
type(x)
```

## IO
### input, print
```Python
x = "Please enter your name: "
y = input(x)
z = f"Hello {user_input}, nice to meet you!"
print(z)
```

### Naming Conventions
```Python
message = "Please enter your name: "
user_input = input(message)
user_output = f"Hello {user_input}, nice to meet you!"
print(user_output)
```

### Code Modularization
```Python
message = "Please enter your name: "
user_input = input(x)

user_output = f"Hello {user_input}, nice to meet you!"
print(user_output)
```



