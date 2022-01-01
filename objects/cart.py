import pyglet

from config import (
    CART_POS,
    CART_LENGTH,
    CART_MASS,
    CART_DT,
    FRICTION,
    GRAVITY,
)


class Cart:

    def __init__(self):
        self.x, self.y = CART_POS
        self.length = CART_LENGTH
        self.mass = CART_MASS
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

    def left(self, ):
        self.cart.x -= CART_DT

    def right(self, ):
        self.cart.x += CART_DT

    def draw(self, ):
        self.cart.draw()
