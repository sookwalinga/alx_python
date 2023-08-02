## Python - Classes and Objects

1. **OOP (Object-Oriented Programming):** A programming paradigm that organizes code around objects, combining data (attributes) and functions (methods) that operate on that data.

2. **"First-Class Everything":** A principle in some programming languages where all entities (functions, classes, etc.) are treated as objects and can be manipulated like any other data.

3. **Class:** A blueprint or template for creating objects. It defines attributes and methods that objects of that class will have.

4. **Object and Instance:** An object is a concrete realization of a class, representing a specific entity in a program. An instance is an individual occurrence of an object.

5. **Difference Between Class and Object/Instance:** A class is a blueprint, while an object/instance is a concrete manifestation created from that blueprint.

6. **Attribute:** A data field associated with a class or object that stores information about the object's state.

7. **Public, Protected, and Private Attributes:** Access modifiers in object-oriented programming. Public attributes are accessible from anywhere, protected attributes have limited access, and private attributes are meant to be accessed only within the class.

8. **Self:** A reference to the instance of a class within its methods, used to access attributes and methods of the instance.

9. **Method:** A function defined within a class, capable of performing actions on the object's data.

10. **\_\_init\_\_ Method:** A special method used for initializing object attributes when an instance of a class is created.

11. **Data Abstraction, Data Encapsulation, Information Hiding:** OOP concepts. Abstraction focuses on essential features while hiding complexities, encapsulation bundles data and methods together, and information hiding restricts access to internal details.

12. **Property:** A special attribute that allows controlled access to an object's data, often used for validation or computed values.

13. **Attribute vs Property in Python:** An attribute holds data, while a property uses methods to get, set, or delete data, providing more control.

14. **Pythonic Getters and Setters:** Use the `@property` decorator for getters and `@<attr>.setter` decorator for setters in Python.

15. **Dynamically Create Attributes:** Assign values to new attribute names using dot notation on an existing instance.

16. **Binding Attributes:** Attributes are bound by assigning them to a class or object, becoming part of their namespace.

17. **\_\_dict\_\_ of a Class/Instance:** A dictionary containing attribute names and their corresponding values for a class or instance.

18. **Attribute Lookup in Python:** Python first looks for attributes in the instance, then the class, and finally in parent classes (following the Method Resolution Order).

19. **Using getattr Function:** The `getattr()` function retrieves the value of an attribute from an object, along with an optional default value if the attribute doesn't exist.
