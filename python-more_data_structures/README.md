### Python - More Data Structures: Set, Dictionary

1. What are sets and how to use them?
   Sets are unordered collections of unique elements. They are used to store distinct items and perform operations like intersection, union, and difference. To create a set in Python, use curly braces {} or the `set()` constructor, and to add elements, use the `add()` method or direct assignment.

2. What are the most common methods of sets and how to use them?
   Common methods for sets include `add()`, `remove()`, `discard()`, `pop()`, `clear()`, `union()`, `intersection()`, `difference()`, `issubset()`, `issuperset()`, and `symmetric_difference()`. Use these methods to manipulate and perform set operations.

3. When to use sets versus lists?
   Use sets when you need to store unique elements and don't require ordering or duplicates. Lists allow duplicates and maintain the order of elements, whereas sets do not.

4. How to iterate into a set?
   You can iterate through a set using a loop (e.g., `for item in my_set:`) to access each element in the set.

5. What are dictionaries and how to use them?
   Dictionaries are unordered collections of key-value pairs. Each key must be unique and immutable. To create a dictionary in Python, use curly braces {} with key-value pairs, or use the `dict()` constructor.

6. When to use dictionaries versus lists or sets?
   Use dictionaries when you need to associate values with unique keys for efficient lookup and retrieval. Lists and sets are used when you simply need to store elements in a specific order or unique items, respectively.

7. What is a key in a dictionary?
   A key in a dictionary is a unique identifier used to access a specific value associated with it. It acts as a label for the corresponding value.

8. How to iterate into a dictionary?
   You can iterate through a dictionary using a loop (e.g., `for key, value in my_dict.items():`) to access both keys and their corresponding values.

9. What is a lambda function?
   A lambda function is an anonymous function in Python that can have any number of arguments but can only have one expression. It is created using the `lambda` keyword.

10. What are map, reduce, and filter functions?
    - `map()` is a higher-order function that applies a given function to each item of an iterable and returns an iterator with the results.
    - `reduce()` is a higher-order function from the `functools` module used to cumulatively apply a function to the elements of an iterable, reducing it to a single value.
    - `filter()` is a higher-order function that creates an iterator containing elements from an iterable that satisfy a given condition (specified by a function).
