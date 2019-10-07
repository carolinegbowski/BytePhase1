
# Exercise on Functional programming

**You are not allowed using recursion or loops. Only use map, filter or reduce**

* Write a function ```create_matrix``` that consumes a number ```n``` and returns an NxN matrix (list of lists) with all 0 entries
```Python
create_matrix(0) # []
create_matrix(1) # [0]
create_matrix(2) # [[0, 0], [0, 0]]
create_matrix(3) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

* You are provided with a basic Student class below. Write a function ```oldest_student``` that consumes a list of students ```los``` and returns the first name of the oldest student. An example is provided below
```Python
class Student:
  def __init__(self, first, last, age):
    self.first = first
    self.last = last
    self.age = age
    
Wasif = Student("Wasif", "Khan", 27)
Greg = Student("Greg", "Smith", 25)
Jeff = Student("Jeff", "Zheng", 50)
lst_of_students = [Wasif, Greg, Jeff]

oldest_student(lst_of_students) == "Jeff"
```
