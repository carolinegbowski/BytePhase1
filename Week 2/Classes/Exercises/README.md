# Introduction to Python

**All work must be contained in the [introduction_to_python.py](...) file. Any work done outside will not be considered unless explicity stated by the student to the instructor**

## Question 1 

The ``id`` function helps us determine the memory address of a particular variable. Python dynamically creates memory each time we create a variable. For example, if you type the following code into a Python command prompt, you will see the memory address of where x and y are stored. Notice how they change upon changing the variables - this is Python's dynamic nature of memory creation. **Note: Do not type this in an editor - reasons beyond the scope of this lesson** 
```Python
>>> x = 1
>>> y = 1
>>> id(x)
10914496
>>> id(y)
10914496
>>> x = 1234
>>> id(x)
1400159191253392
>>> y = 1234
>>> id(y)
1400159191254216
```

You will notice that when x and y are 1, they are stored in the same memory address while when x and y are 1234, they are stored in separate memory addresses. This is due to the idea that Python only dynically creates integers above a certain range and stores small integers in memory as they are commonly used in a developers code. This improves the performance of Python code as dynamically creating memory is expensive. Your goal is to determine what range of integers Python saves in memory. 

* Implement a function called ```range```
  * Input is nothing
  * Returns the tuple ```(lower, upper)``` where lower and upper are integers representing the respective bounds.

## Question 2



* The [Collections](https://docs.python.org/3.7/library/collections.html) contains high performance replacements for ....


