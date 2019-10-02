## Week 2 weekend exercises

## Hash Tables

* You are provided with code for a basic HashTable as discussed in class with the ```__init__, __len__``` and ```insert, search``` methods implemented
* Your goal is to implement the ```traverse```, ```delete``` and ```most_collisions``` operations such that they pass the test below

```Python
class HashTable:

  def __init__(self, hash_size):
    self.hash_size = hash_size
    self.table = [None] * hash_size
  def __len__(self):
    count = 0
    for i in self.table:
      if not(i is None):
        count += len(i)
    return count

  def insert(self, val):
    index = id(val) % self.hash_size
    if self.table[index] == None:
      self.table[index] = [val]
    else:
      if not(val in self.table[index]):
        self.table[index].append(val)
        
  def search(self, val):
    index = id(val) % self.hash_size
    if self.table[index] == None:
      return False
    return val in self.table[index]
    
  def traverse(self):
    pass
    
  def delete(self, val):
    pass
```

* Initialization
```Python  
table = HashTable(10)
table.insert(15)
table.insert(25)
table.insert(35)
table.insert(30)
table.insert(33)
```

* Traversal - output a list containing 
```Python
table.traverse() == [10, 30, 33, 15, 25, 35]
```

* Delete - Delete an entry from the hashtable
```Python
table.delete(25)
table.traversal() == [10, 30, 33, 15, 35]
```

* most_collisions - returns the maximum number of collisions for any index in the hashtable
```Python
table.most_collisions() == 3 # Assuming the delete operation previously did not occur
```

## Graphs
* Read about [graphs](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/) and answer the following questions
  * The runtime of graphs is measured by 2 factors - what are these?
  * Understand how to do DFS and BFS on a graph
  
## Putting it all togther

* Fill out the runtime for all the cells. Understand why the runtime is what it is. Compare worst case, average case and best case

Data Structure| Linked List | Tree | Hash Table | Graph
--------------|-------------|------|------------|-----
Insert        |        x    | x    |  x         | x
Delete        |        x    | x    |  x         | x
Search        |        x    | x    |  x         | x
Traverse      |        x    | x    |  x         | x



