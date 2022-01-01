import math


class Vector2:
    """
    @params:
        x: float
        y: float
    
    @methods:
        changeofbases(Vector2 : other) -> Vector2 : returns a new vector with the change of bases
        angle() -> float : returns the angle of the vector with the x axis
        translate(Vector2 : other) -> Vector2 : returns a new vector with the translation
        magnitude() -> float : returns the magnitude of the vector
        normalize() -> Vector2 : returns a new vector with unit length
        extend(float : length) -> Vector2 : extends a copy of the vector to the given length
        dot(Vector2 : other) -> float : returns the dot product of the vector
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mag = self.magnitude()

    def changeofbases(self, other1, other2):
        return Vector2(self.x * other1.x + self.y * other1.y,
                       self.x * other2.x + self.y * other2.y)

    def angle(self):
        return math.atan2(self.y, self.x)

    def translate(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        return Vector2(self.x / self.mag, self.y / self.mag)

    def extend(self, length):
        return Vector2(self.x * length, self.y * length)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)

    def _changeofbases(self, other1, other2):
        self.x = self.x * other1.x + self.y * other1.y
        self.y = self.x * other2.x + self.y * other2.y
        return self

    def _translate(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def _normalize(self):
        self.x = self.x / self.mag
        self.y = self.y / self.mag
        self.mag = self.magnitude()
        return self

    def _extend(self, length):
        self.x = self.x * length
        self.y = self.y * length
        return self

    def _add(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def _sub(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        return self

    def _mul(self, other):
        self.x = self.x * other
        self.y = self.y * other
        return self

    def _div(self, other):
        self.x = self.x / other
        self.y = self.y / other
        return self

    def __repr__(self):
        return f"<Vector2({self.x}, {self.y})>"