from abc import ABC, abstractmethod
import math

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    

class Rectangle(shape):
    def __init__(self, h, v):
        self.h=h
        self.v=v
    def area(self):
        return self.h*self.v
    def perimeter(self):
        return (self.h+self.v)*2

class Triangle(shape):
    def __init__(self, h, v, w):
        self.h=h
        self.v=v
        self.w=w
    def area(self):
        s=(self.h+self.v+self.w)/2
        return (math.sqrt(s*(s-self.h)*(s-self.v)*(s-self.w)))
    def perimeter(self):
        return self.h+self.v+self.w

class Circle(shape):
    def __init__(self, r):
        self.r=r
    def area(self):
        return self.r*self.r*math.pi
    def perimeter(self):
        return 2*self.r*math.pi

class RegularHexagon(shape):
    def __init__(self, r):
        self.r=r
    def area(self):
        return math.sqrt(3)/4*self.r*self.r*6
    def perimeter(self):
        return 6*self.r


def main():
    shapes=[]
    shapes.append(Rectangle(5,2))
    shapes.append(Triangle(3,4,5))
    shapes.append(Circle(5))
    shapes.append(RegularHexagon(3))

    for shape in shapes:
        print(shape)
        print(f"넓이는 {shape.area():.1f}입니다.")
        print(f"둘레는 {shape.perimeter():.1f}입니다.")

if __name__ == "__main__":
    main()