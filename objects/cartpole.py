import math
from objects import (
    Cart,
    Pole,
)

from config import (
    POLE_PIVOT,
    POLE_MASS,
    POLE_RADIUS,
    POLE_LENGTH,
    POLE_ANGLE,
    POLE_ANGULAR_VELOCITY,
    POLE_ANGULAR_ACCELERATION,
    CART_MASS,
    CART_LENGTH,
    CART_POS,
    CART_VELOCITY,
    CART_ACCELERATION,
    GRAVITY,
    FORCE,
    CART_DT,
)

from libs import Vector2


class CartPole:

    def __init__(self, ):
        self.gravity = GRAVITY
        self.masscart = CART_MASS
        self.masspole = POLE_MASS
        self.total_mass = self.masspole + self.masscart
        self.length = POLE_LENGTH // 2
        self.polemass_length = self.masspole * self.length
        self.force = FORCE
        self.dt = CART_DT

        self.init()

    def compute_x_y(self, pivot_pos: Vector2, angle: float, length: float):
        x = pivot_pos.x + length * math.sin(angle)
        y = pivot_pos.y + length * math.cos(angle)
        return x, y

    def init(self, ):
        cart_pos = Vector2(CART_POS)
        self.cart = Cart(cart_pos, CART_LENGTH)

        self.pivot_pos = Vector2(POLE_PIVOT)
        self.pole_length = POLE_LENGTH
        self.pole_radius = POLE_RADIUS
        bob_pos = Vector2((self.compute_x_y(self.pivot_pos, POLE_ANGLE,
                                            self.pole_length)))
        self.pole = Pole(self.pivot_pos, bob_pos, POLE_RADIUS)

        self.angle = POLE_ANGLE
        self.angle_vel = POLE_ANGULAR_VELOCITY
        self.angle_acc = POLE_ANGULAR_ACCELERATION

        self.x = CART_POS[0]
        self.x_vel = CART_VELOCITY
        self.x_acc = CART_ACCELERATION

    def update(self, dt: float):
        sintheta = math.sin(self.angle)
        costheta = math.cos(self.angle)
        temp = (self.force + self.polemass_length * self.angle_vel**2 *
                sintheta) / self.total_mass

        self.angle_acc = (self.gravity * sintheta - costheta * temp) / (
            self.length * (4.0 / 3.0 -
                           (self.masspole * costheta**2 / self.total_mass)))

        self.x_acc = temp - (self.polemass_length * self.angle_acc * costheta /
                             self.total_mass)

        self.x_vel = self.x_vel + self.x_acc * self.dt
        self.x = self.x + self.x_vel * self.dt

        self.angle_vel = self.angle_vel + self.angle_acc * self.dt
        self.angle = self.angle + self.angle_vel * self.dt

        self._update(self.angle, self.x)

    def _update(self, angle: float, x: float):
        cart_pos = Vector2((x, CART_POS[1]))
        bob_pos = Vector2((self.compute_x_y(cart_pos, angle,
                                            self.pole_length)))

        self.pole.update(bob_pos, cart_pos)
        self.cart.update(cart_pos)

    def left(self, ):
        self.force = -FORCE

    def right(self, ):
        self.force = FORCE

    def draw(self, ):
        self.cart.draw()
        self.pole.draw()