# Stacks and Queues

* You are provided with a template for a ```Stack``` and ```Queue```. You're goal is to implement the ```push```, ```pop``` and ```peek``` operations such that the tests below pass
  * Keep in mind the ```peek``` operation returns the next item to be popped without actually popping it (kind of like search).

```Python
class Stack:
     def __init__(self):
         self.items = []

     def is_empty(self):
         return self.items == []
         
     def size(self):
         return len(self.items)

     def push(self, item):
         pass

     def pop(self):
         pass

     def peek(self):
         pass

s = Stack()
s.push(5)
s.push(10)
s.push("hi")
s.peek() == "hi"
s.pop()
s.peek() == 10
s.push(20)
s.peek() == 20

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
        
    def push(self, item):
        pass

    def pop(self):
        pass
        
    def peek(self):
        pass

q = Stack()
q.push(5)
q.push(10)
q.push("hi")
q.peek() == 5
q.pop()
q.peek() == 10
q.push(20)
q.peek() == "hi"        
 ```
