import math

from config import (
    CART_ACCELERATION,
    CART_FRICTION,
    CART_LENGTH,
    CART_MASS,
    CART_POS,
    CART_VELOCITY,
    DT,
    FORCE,
    GRAVITY,
    POLE_ANGLE,
    POLE_ANGULAR_ACCELERATION,
    POLE_ANGULAR_VELOCITY,
    POLE_FRICTION,
    POLE_LENGTH,
    POLE_MASS,
    POLE_PIVOT,
    POLE_RADIUS,
    POLE_WIDTH,
)
from libs import Vector2

from objects import Cart, Pole


class CartPole:

    def __init__(self, ):
        self.gravity = GRAVITY
        self.masscart = CART_MASS
        self.masspole = POLE_MASS
        self.total_mass = self.masspole + self.masscart
        self.length = POLE_LENGTH // 2
        self.polemass_length = self.masspole * self.length
        self.force = FORCE
        self.dt = DT
        self.Nc = 1

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
        self.pole = Pole(self.pivot_pos, bob_pos, POLE_RADIUS, POLE_WIDTH)

        self.angle = POLE_ANGLE
        self.angle_vel = POLE_ANGULAR_VELOCITY
        self.angle_acc = POLE_ANGULAR_ACCELERATION

        self.x = CART_POS[0]
        self.x_vel = CART_VELOCITY
        self.x_acc = CART_ACCELERATION

    def compute_angle_acc(self, ):
        sintheta = math.sin(self.angle)
        costheta = math.cos(self.angle)

        friction_1 = CART_FRICTION * costheta * self.sgn(self.x_vel * self.Nc)
        friction_2 = CART_FRICTION * GRAVITY * self.sgn(self.x_vel * self.Nc)
        friction_3 = (POLE_FRICTION * self.angle_vel) / (self.polemass_length)
        friction_4 = CART_FRICTION * self.sgn(self.x_vel * self.Nc)

        temp = (friction_2 - ((self.force +
                               (self.polemass_length * (self.angle_vel**2) *
                                (sintheta + friction_1))) / self.total_mass))

        n_angle_acc = (GRAVITY * sintheta + costheta * temp - friction_3)

        d_angle_acc = self.length * ((4.0 / 3.0) - ((
            (self.masspole * costheta) / self.total_mass) *
                                                    (costheta - friction_4)))

        return n_angle_acc / d_angle_acc

    def sgn(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

    def update(self, dt: float):
        sintheta = math.sin(self.angle)
        costheta = math.cos(self.angle)

        self.angle_acc = self.compute_angle_acc()

        Nc = (self.total_mass * GRAVITY) - (self.polemass_length *
                                            ((self.angle_acc * sintheta) +
                                             (self.angle_vel**2 * costheta)))

        if self.sgn(Nc) != self.sgn(self.Nc):
            self.angle_acc = self.compute_angle_acc()

        self.Nc = Nc
        friction_5 = CART_FRICTION * self.Nc * self.sgn(self.x_vel * self.Nc)

        n_x_acc = self.force + (self.polemass_length *
                                ((self.angle_vel**2 * sintheta) -
                                 (self.angle_acc * costheta))) - friction_5
        d_x_acc = self.total_mass

        self.x_acc = n_x_acc / d_x_acc

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
