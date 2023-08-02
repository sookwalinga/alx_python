"""
Module: 4-base_geometry

Contains a class definition for BaseGeometry
with a public instance method.
"""


class BaseGeometry:
    """
    A class representing the base geometry.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: This method is not implemented.

        """
        raise Exception("area() is not implemented")

    def __dir__(self):
        """
        Customize the list of attributes and methods returned by dir().

        Returns:
            A list of attributes and methods including 'area'.
        """
        return sorted(dir(type(self)) + list(self.__dict__) + ['area'])
