from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, h, v):
        pass

class Triangle(Shape):
    def __init__(self, h, v):
        pass

class Circle(Shape):
    def __init__(self, r):
        pass

class RegularHexagon(Shape):
    def __init__(self, r):
        pass

def main():
    shapes=[]
    shapes.append(Rectangle(5,2))
    shapes.append(Triangle(5,2))

    for shape in shapes:
        print(shape)
        print(shape.area())
        print(shape.perimeter())

if __name__ == "__main__":
    main()