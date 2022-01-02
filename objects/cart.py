import pyglet
from libs import Vector2


class Cart:

    def __init__(self, cart_pos: Vector2, cart_length: float):
        self.x, self.y = cart_pos.x, cart_pos.y
        self.length = cart_length
        self.init()

    def init(self, ):
        self.cart = pyglet.shapes.Rectangle(
            x=self.x,
            y=self.y,
            width=self.length,
            height=self.length // 2,
            color=(255, 255, 255),
        )
        self.cart.anchor_position = (self.length // 2, self.length // 2)

    def update(self, cart_pos: Vector2):
        self.x, self.y = cart_pos.x, cart_pos.y
        self.cart.x, self.cart.y = self.x, self.y

    def draw(self, ):
        self.cart.draw()
