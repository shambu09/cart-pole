import math

#------------------------------------------------------------------------------
#* Window Config

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_NAME = "CartPole"

#------------------------------------------------------------------------------
#* Environment
GRAVITY = 9.81
FRICTION = 1
FORCE = 10
DT = 0.1
#------------------------------------------------------------------------------
POLE_PIVOT = (400, 300)

#* Initial pendulum parameters:

POLE_MASS = 0.3
POLE_RADIUS = 10
POLE_LENGTH = 200

POLE_ANGLE = math.radians(0)
POLE_ANGULAR_VELOCITY = 0
POLE_ANGULAR_ACCELERATION = 0
POLE_FRICTION = 5
POLE_WIDTH = 2
#------------------------------------------------------------------------------
#* Cart parameters
CART_MASS = 1
CART_LENGTH = 100

CART_POS = POLE_PIVOT
CART_VELOCITY = 0
CART_ACCELERATION = 0
CART_FRICTION = 0.2
#------------------------------------------------------------------------------
