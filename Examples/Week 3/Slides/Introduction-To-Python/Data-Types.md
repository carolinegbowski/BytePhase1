# Data Types

* Python memory abstraction model (formally defined as **data types**)
   * Atomic data types
     * Numbers (int, float)
     * Booleans (bool)
       * short-circuiting
       * lazy-evaluation
     * Strings (str)
       * len
       * indexing
       * slicing
       * adding
       * f-strings
   * Compound data types (sequence)
     * Lists (list), Tuples (tuple)
       * len
       * indexing
       * slicing
       * appending/adding (only to list)
   * Compound data types (associative)
     * Dictionary (dict), Sets (set)
       * len
       * selecting/adding
   * Python memory model
   ```Python
   x = 1234; id(x)
   y = 1234; id(y)

   lst1 = [x, y]
   id(lst1)
   id(lst1[0])
   ```
   
