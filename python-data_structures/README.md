## Python - Data Structures: Lists, Tuples

1. **What are lists and how to use them:**
   Lists are a data structure in Python used to store multiple items in a single variable. They are ordered, mutable (can be changed), and can contain elements of different data types. To create a list, you enclose comma-separated elements in square brackets. Example: `my_list = [1, 2, 3, 'apple', 'banana']`. Lists support indexing, slicing, and various methods for manipulation.

2. **Differences and similarities between strings and lists:**
   Strings are sequences of characters, while lists are sequences of elements. Both are ordered and support indexing and slicing. However, strings are immutable, meaning their contents cannot be changed after creation, while lists are mutable and can be modified. Lists can contain various data types, whereas strings are limited to characters.

3. **Most common methods of lists and how to use them:**
   Some common methods for lists in Python include `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `index()`, `count()`, `sort()`, and `reverse()`. These methods allow you to add elements, remove elements, find the index of an element, sort the list, and more. Example: `my_list.append(4)` adds the element `4` to the end of the list.

4. **How to use lists as stacks and queues:**
   You can use a list as a stack (Last-In, First-Out) by using `append()` to push elements onto the stack and `pop()` to remove elements from the top of the stack. For queues (First-In, First-Out), you can use `append()` to enqueue elements and `pop(0)` or use the `deque` class from the `collections` module for more efficient dequeueing.

5. **What are list comprehensions and how to use them:**
   List comprehensions provide a concise way to create lists in Python. They allow you to generate a new list by specifying an expression and an iterable, along with optional conditions. Example: `[x**2 for x in range(1, 5)]` generates the list `[1, 4, 9, 16]`, containing the squares of numbers from 1 to 4.

6. **What are tuples and how to use them:**
   Tuples are similar to lists, but they are immutable, meaning their elements cannot be changed after creation. They are created by enclosing comma-separated elements in parentheses. Example: `my_tuple = (1, 'apple', 3.14)`. Tuples are typically used for fixed collections of items, such as coordinates or database records.

7. **When to use tuples versus lists:**
   Use tuples when you need an immutable collection of items that shouldn't change, like the coordinates of a point. Lists, on the other hand, are suitable when you need a mutable collection to add, remove, or modify elements during the program's execution.

8. **What is a sequence:**
   In Python, a sequence is an ordered collection of elements. Lists, strings, and tuples are all examples of sequences. Sequences support common operations like indexing, slicing, and iteration.

9. **What is tuple packing:**
   Tuple packing refers to the process of creating a tuple by packing multiple values or variables together. For example: `my_tuple = 1, 2, 'hello'`. Here, the values `1`, `2`, and `'hello'` are automatically packed into a tuple.

10. **What is sequence unpacking:**
    Sequence unpacking is the opposite of tuple packing. It involves assigning the individual elements of a sequence (like a tuple) to separate variables. Example: `x, y, z = my_tuple` will assign the first element of `my_tuple` to `x`, the second to `y`, and the third to `z`.

11. **What is the del statement and how to use it:**
    The `del` statement is used to delete elements from a list or variables from memory. For lists, you can use it to remove an element by index: `del my_list[2]` will remove the third element from the list. For variables, `del variable_name` will remove the variable from memory, freeing up its space.
