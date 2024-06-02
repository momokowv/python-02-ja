class Vehicle:
    def move(self):
        return "This vehicle is moving"
    
class Car(Vehicle):
    def move(self):
        return "Car is driving on the road"
    
class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is being pedaled"
    
car = Car()
bicycle = Bicycle()

print(car.move())
print(bicycle.move())

class Shape:
    def draw(self):
        return

class Circle(Shape):
    def draw(self):
        return "This is circle."

class Square(Shape):
    def draw(self):
        return "This is Suqare."
    
def draw_shape(shape):
    print(shape.draw())
    
draw_shape(Circle())
draw_shape(Square())

class Cat:
    def print_info(self):
        return "This is a cat."

class Printer:
    def print_info(self):
        return "This is a printer."

def display_info(object):
    print(object.print_info())

display_info(Cat())
display_info(Printer())

class Point:
    def __init__(self,x,y) :
        self.x = x
        self.y = y
        
    def __add__(self, other) :
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Point: x={self.x}, y={self.y}"
    
    def __repr__(self):
        return f"Point({self.x},{self.y})"
p1 = Point(1,2)
p2 = Point(3,4)
p3 = p1 + p2
print(f"Point:({p3.x},{p3.y})")
print(p1 == p2)
print(p1 == p3)
print(p1)
print(repr(p1))
