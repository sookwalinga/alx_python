## Python - Inheritance

1. A superclass, base class, or parent class is a class from which other classes inherit attributes and methods.

2. A subclass is a class that inherits attributes and methods from a superclass or base class.

3. To list all attributes and methods of a class or instance, you can use the `dir()` function.

4. An instance can have new attributes at any time by assigning values to them directly.

5. To inherit a class from another, define the new class with the desired superclass in its declaration, like `class NewClass(SuperClass):`.

6. To define a class with multiple base classes, separate the base classes by commas: `class NewClass(BaseClass1, BaseClass2):`.

7. The default class every class inherits from is called `object`.

8. To override a method or attribute inherited from the base class, define the same method or attribute in the subclass with the desired implementation.

9. Attributes and methods available by heritage to subclasses are those defined in the base class that are not marked as private.

10. The purpose of inheritance is to promote code reuse and establish a hierarchy of classes where subclasses can inherit and extend the behavior of their parent classes.

11. `isinstance` is used to check if an object is an instance of a specific class, `issubclass` checks if a class is a subclass of another, `type` returns the type of an object, and `super` returns a temporary object of the superclass.

Feel free to ask if you need more detailed explanations for any of these points!
