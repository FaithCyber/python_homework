import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Vector(Point):
    def __str__(self):
        return f"Vector<{self.x}, {self.y}>"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

# Demonstrate functionality
if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    print(f"P1: {p1}")
    print(f"P1 == P2: {p1 == p2}")
    print(f"Distance: {p1.distance(p2)}")

    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    v3 = v1 + v2
    print(f"V1: {v1}")
    print(f"V1 + V2 = {v3}")