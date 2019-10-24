Create the following classes:

Animal

Animal has a property called "species" and a property called "name". "species" is initialized to None, "name" is set by an argument to the constructor.

```
mike = Animal("Mike")
mike.species # None
mike.name    # Mike
```

Animal also has a method called "make_noise()" that prints out a blank line.

Create the following subclasses of Animal:

* Tiger

Tiger's species property is "tiger" and its "make_noise()" method prints out "Roar!"

* Dog

Dog's species property is "dog" and its "make_noise()" method prints out "Bark!"

* Cow

Cow' species property is "cow" and its "make_noise()" method prints out "Moo!"

Now create a class called Zoo. It has a property called "animals" that is initialized to a blank list

Zoo has a method called "add(animal)" that appends an instance of Animal or one of its subclasses to the animals list. If the argument to add is not an instance of Animal or a subclass, it should raise an error.

Zoo has a method called "show_animals()." For each animal in the animals property, print that animal's name and species and then call its "make_noise" method.

```
mike = Tiger("Mike")
molly = Dog("Molly")
bessie = Cow("Bessie")

zoo = Zoo()
zoo.add(mike)
zoo.add(molly)
zoo.add(bessie)

zoo.show_animals()
Mike the tiger
Roar!
Molly the dog
Bark!
Bessie the cow
Moo!

zoo.add("bad value") # should raise an exception
```

### QuickSort vs MergeSort

Explain why bubblesort is O(n^2), while mergesort is O(log n). 

