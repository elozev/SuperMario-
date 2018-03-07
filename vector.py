import math


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # get tuple of vector
    def getP(self):
        return (self.x, self.y)

    # point vector to opposite direction
    def negate(self):
        self.multiply(-1)
        return self

    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def substract(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def multiply(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

    def divide(self, scalar):
        self.multiply(1 / scalar)
        return self

    def copy(self):
        return Vector(self.x, self.y)

    def __str__(self):
        return "(" + str(self.x) + " : " + str(self.y) + ")"

    def normalize(self):
        return self.divide(self.length())

    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def reflect(self, n):
        new_vec = (2 * self.dot(n.normalize()) * n).substract(self.copy())
        self.x = new_vec.x
        self.y = new_vec.y
        return self

    def dot(self, other):
        return self.x * other.x + self.y * other.y
