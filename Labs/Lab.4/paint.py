# Q10 - paint.py module

import math

# Base Shape class (copied from earlier work)
class Shape:
    def area(self):
        raise NotImplementedError("Area method not implemented")

    def perimeter(self):
        raise NotImplementedError("Perimeter method not implemented")

    def perimeter_points(self):
        # Simple placeholder points (up to 16 points as required in Q7)
        points = []
        for i in range(16):
            points.append((i, i))
        return points

    def contains(self, x, y):
        raise NotImplementedError("Contains method not implemented")


# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width, x, y):
        self.length = length
        self.width = width
        self.x = x
        self.y = y

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def contains(self, px, py):
        # Check if point is inside rectangle boundaries
        return (self.x <= px <= self.x + self.length and
                self.y <= py <= self.y + self.width)


# Circle class
class Circle(Shape):
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def contains(self, px, py):
        dx = px - self.x
        dy = py - self.y
        return (dx**2 + dy**2) <= (self.radius**2)


# Triangle class 
class Triangle(Shape):
    def __init__(self, base, height, x, y):
        self.base = base
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        side = ((self.base / 2)**2 + self.height**2) ** 0.5
        return self.base + 2 * side

    def contains(self, px, py):
        # Simple bounding check 
        return (self.x <= px <= self.x + self.base and
                self.y <= py <= self.y + self.height)


# CompoundShape class (group of shapes)
class CompoundShape(Shape):
    def __init__(self, shapes=None):
        # This shape stores a list of other shapes
        self.shapes = shapes if shapes is not None else []

    def add_shape(self, shape):
        # Adds a new shape to the compound object
        self.shapes.append(shape)

    def area(self):
        # Total area is the sum of all shapes 
        total = 0
        for s in self.shapes:
            total += s.area()
        return total

    def perimeter(self):
        # Simple sum of perimeters 
        total = 0
        for s in self.shapes:
            total += s.perimeter()
        return total


# Simple Canvas class 
class Canvas:
    def __init__(self):
        # Stores shapes that will be drawn
        self.objects = []

    def add(self, shape):
        # Add shape to canvas
        self.objects.append(shape)

    def paint(self):
        # For this lab, we will just print shape info instead of real graphics
        print("Painting canvas with the following shapes:")
        for obj in self.objects:
            print(type(obj).__name__, 
                  "| Area:", round(obj.area(), 2), 
                  "| Perimeter:", round(obj.perimeter(), 2))
