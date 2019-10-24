## Phase 1 Week 1 Day 2 Lesson Plan

### Mutable types

* Difference between reference types and value types (mutable types such as list & dictionary)

```
a = 7
b = a
a = a + 1
# a = 8
# b still == 7

but

a = [1,2,3,4]
b = a
a.append(5)
b == a == [1,2,3,4,5]

# variable stores a memory location, not a fixed value like with an int or float
```

* lists, dictionaries, sets & common methods of them

```
### Lists
a = [3,2,1]
a.sort()
a[0] # = 1
a.append(4) # a is now [1,2,3,4]
a.pop() # returns 4, a is now [1,2,3]

### Dictionaries
b = {"first":1, "second":2, "third":3}
b["first"] # = 1, access a value
b["forth"] = 4 # add a key
b["fifth"] # raises a KeyError b/c doesn't have that key
b.get("fifth") # returns None
b.get("sixth", 6) # returns 6 b/c b["sixth"] isn't defined
del b["second"] # gets rid of this key
list(b.keys()) # ["first", "third", "forth"]

### Sets

c = set([1,2,3])
d = set([3,4,5])
c & d # {3}
c | d # {1, 2, 3, 4, 5}
c ^ d == (c | d) - (c & d) # True, c^d = {1, 2, 4, 5}
```

* constructing lists using for loops.
```
result = []
for i in range(10):
  result.append(i+1)
# now result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

* slice indexing
```
# array[start:non-inclusive-end:stepsize] 
result[3] # 4
result[:3] # [1, 2, 3]
result[3:7] # [4, 5, 6, 7]
result[7:] # [8, 9, 10]
result[2::3] # [3, 6, 9]
# handy
result[::-1] # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

* for element in list
```
for a in [1,2,3]:
  print("a is now {0}".format(a))
```

* list comprehensions
```
odds = [x for x in range(10) if x%2 == 1]
```

* for key, value in dictionary.items()
```
for k,v in b.items():
  print("b['{0}'] = {1}".format(k,v))
```

### Functions, continued

* variable scope & the global keyword

* object.method() syntax (like list.sort(), what it means)

* named parameters, `*args`, & `**kwargs`

* return vs. print. function arguments vs. input

* functions should rarely print and rarely input unless the sole purpose is to output text or recieve user input.

* a mutable type passed as an argument can be altered by a function. if a is a list, a.sort() alters the contents of a.

* python functions *generally* return something or modify data but not both. functions that modify the state of the program communicate failure with raised exceptions.

    * introduce try, except, raise here

* the concept of map & filter. how python accomplishes those with list comprehensions
