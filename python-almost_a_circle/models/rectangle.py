from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base and represents a rectangle with width, height, and position.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate position of the rectangle.
        __y (int): The y-coordinate position of the rectangle.
        id (int): The unique identifier of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Initializes a new Rectangle instance.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate position of the rectangle.
            y (int, optional): The y-coordinate position of the rectangle.
            id (int, optional): The identifier for the instance.

        Attributes:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate position of the rectangle.
            y (int): The y-coordinate position of the rectangle.
            id (int): The unique identifier of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getters and setters for width, height, x, y...
