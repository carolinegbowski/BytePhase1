
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
* Python memory can be accessed through the ```id``` function
* Functions in Python are called very similar to how they are called in Math
```Python
x = 1
id(x)
x = 2
id(x)
```

### Types (type)
* The type of a variable can be accessed through the ```type``` function
* ```x = 1``` declares x to reference an ```int``` type
* There also exists the ```str``` (String) type to allow us to handle text
```Python
x = 1
type(x)
x = "Hello World"
type(x)
```

## IO
### input, print
* Python provides a way for your program to take in information from the user and display information to the user
* Done through the ```input``` and ```print``` functions
```Python
x = "Please enter your name: "
y = input(x)
z = f"Hello {user_input}, nice to meet you!"
print(z)
```

### Styling your coded
* Python recommends following a specific [style guide](https://www.python.org/dev/peps/pep-0008/) for how code should "look"
* Includes naming convention for variables, spacing and indentation rules and much more
* Allows for Python code to be consistent and scallable throughout organizations
```Python
message = "Please enter your name: "
user_input = input(message)
user_output = f"Hello {user_input}, nice to meet you!"
print(user_output)
```

### Code Modularization
* We typically want to divide our code into separate parts, each conerned with independent tasks
* Code modularization can be as simple as a space between lines of code or as complex as dividing code into separate files
```Python
message = "Please enter your name: "
user_input = input(x)

user_output = f"Hello {user_input}, nice to meet you!"
print(user_output)
```
