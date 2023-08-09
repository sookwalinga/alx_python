"""
models.base

This module defines the Base class that serves as the foundation for managing id attributes in the project.
"""


class Base:
    """
    Base class to manage the id attribute for all future classes.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of the number of objects created.

    Methods:
        __init__(self, id=None): Initializes a new instance of the Base class.
            If `id` is provided, assigns it to the instance's `id` attribute.
            Otherwise, increments the __nb_objects counter and assigns the new value to the instance's `id` attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): An identifier for the instance. If not provided, a unique id is generated.

        Attributes:
            id (int): The identifier for the instance. Unique if not provided during instantiation.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
