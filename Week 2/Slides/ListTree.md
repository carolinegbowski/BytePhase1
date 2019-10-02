## Linked List

* Understand the [Stack](https://www.geeksforgeeks.org/stack-data-structure/) and [Queue](https://www.geeksforgeeks.org/queue-data-structure/) data structures.  There is supplimentary links in the provided link for further information about these data structures.
  * Provide an application when you would want to use a stack vs a queue vs a normal linked list
* You are provided with the basic code for a Linked List with \_\_init\_\_, \_\_len\_\_, \_\_eq\_\_, and insert already implemented. Your goal is to implement the methods listed below in the specified runtime. Tests are provided for each implementation. You may assume duplicates are not allowed in the list.
  * Implement delete, search and traverse all in O(n) runtime
  * Implement add_to_end in O(1) runtime. This method simply adds an element to the end of the list
    * Hint: Need to modify \_\_init\_\_ and possibly other methods as well


```Python
class Node:
  def __init__(self, first, next = None):
    self.first = first
    self.next = next
  def __len__(self):
    if self.next == None:
      return 1
    else:
      return 1 + len(self.next)
   def __eq__(self, other):
    while self != None or other != None:
      if self.first != other.first:
        return False
      self = self.next
      other = other.next
    return True if self == None and other == None else False
      
  def insert(self, index, num):
    if index == 0:
      new_node = Node(num)
      new_node.next = self
      self = new_node
    elif index == 1:
      new_node = Node(num)
      new_node.next = self.next
      self.next = new_node
    else:
      self.next.insert(index - 1, num)
      
  def delete(self, num):
    pass
  def search(self, num):
    pass
  def traverse(self):
    pass
```

* Initialization
```Python
lst = Node(1, Node(9, Node(2, Node(10, Node(5, None)))))
```

* Deletion - delete the number from the list, or do nothing if the list doesn't contain the number
```Python
lst.delete(2)
lst == Node(1, Node(9, Node(10, Node(5, None))))

lst.delete(20) == lst
```

* Search - return the index where element is found, or -1 if it doesn't exist(Assuming delete did not happen)
```Python
lst.search(1) == 0
lst.search(9) == 1
lst.search(100) == -1
```

* Traverse (Assuming delete did not happen)
```Python
lst.traverse() == '[1, 9, 2, 10, 5]' # This function outputs a list in string format
```

* Add_to_end (Assuming delete did not happen)
```Python
lst.add_to_end(20) == Node(1, Node(9, Node(2, Node(10, Node(5, Node(20, None)))))
```


# Tree

* You are provided with the basic code for a Binary Search Tree (BST) with \_\_init\_\_, and insert already implemented. Your goal is to implement the methods listed below in the specified runtime. Tests are provided for each implementation 
  * Implement \_\_len\_\_ in O(n) runtime
  * Implement search in O(logn) and traverse all in O(n) runtime
  * Implement \_\_len\_\_ in O(1) runtime.
    * Hint: Need to modify \_\_init\_\_ and possibly other methods as well

```Python
class Node:
  def __init__(self, num, left = None, right = None):
    self.num = num
    self.left = left
    self.right = right
    
  def __lt__(self, other):
    return self.num < other.num
    
  def __len__(self):
    pass
    
  def insert(self, num):
    new_node = Node(num)
    if new_node < self:
      if self.left == None:
        self.left = new_node
      else:
        self.left.insert(num)
    else:
      if self.right == None:
        self.right = new_node
      else:
        self.right.insert(num)
        
  def traverse(self, num):
    pass
  def search(self, num):
    pass
```

* Initialization
```Python
t = Node(10,
         Node(5,
              Node(0,
                   None,
                   Node(2, None, None)),
              Node(8,
                   None,
                   None)),
         Node(20,
              Node(15,
                   None,
                   None),
              Node(30,
                   None,
                   Node(70,
                        None,
                        None))))             

```

* Length
```Python
len(t) == 9
```

* Search - return True if num exists, False otherwise
```Python
t.search(40) == False
t.search(70) == True
```

* Traverse - return a list of all the numbers in sorted order
```Python
t.traverse() == [0, 5, 8, 10, 15, 20, 30, 70]
```
