import math

#------------------------------------------------------------------------------
#* Window Config

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_NAME = "Pendulum"

#------------------------------------------------------------------------------
#* Environment
GRAVITY = 9.81
FRICTION = 0.01

#------------------------------------------------------------------------------
PENDULUM_PIVOT = (400, 100)

#* Initial pendulum parameters:

PENDULUM_MASS = 1
PENDULUM_RADIUS = 10
PENDULUM_LENGTH = 200

PENDULUM_ANGLE = math.radians(90)
PENDULUM_ANGULAR_VELOCITY = 0
PENDULUM_ANGULAR_ACCELERATION = 0

#------------------------------------------------------------------------------
#* Cart parameters
CART_MASS = 1
CART_LENGTH = 100

CART_POS = PENDULUM_PIVOT
CART_DT = 5
#------------------------------------------------------------------------------
