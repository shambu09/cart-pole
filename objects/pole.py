import pyglet
from libs import Vector2


class Pole:

    def __init__(self, pivot_pos: Vector2, bob_pos: Vector2, radius: int,
                 width: int):
        self.x, self.y = pivot_pos.x, pivot_pos.y
        self.x2, self.y2 = bob_pos.x, bob_pos.y
        self.radius, self.width = radius, width
        self.init()

    def init(self, ):
        self.pole = pyglet.shapes.Line(
            x=self.x,
            y=self.y,
            x2=self.x2,
            y2=self.y2,
            width=self.width,
            color=(255, 10, 10),
        )
        self.bob = pyglet.shapes.Circle(
            x=self.x2,
            y=self.y2,
            radius=self.radius,
            color=(255, 255, 255),
        )

    def update(self, bob_pos: Vector2, cart_pos: Vector2):
        self.x2, self.y2 = bob_pos.x, bob_pos.y
        self.pole.x2, self.pole.y2 = self.x2, self.y2
        self.bob.x, self.bob.y = self.x2, self.y2
        self.x, self.y = cart_pos.x, cart_pos.y
        self.pole.x, self.pole.y = self.x, self.y

    def draw(self, ):
        self.pole.draw()
        self.bob.draw()