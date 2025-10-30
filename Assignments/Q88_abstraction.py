from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):  # Implementing abstract method
        return self.width * self.height

# shape = Shape()  # This would raise TypeError: Can't instantiate abstract class
rect = Rectangle(10, 5)
print(rect.area())  # 50

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
