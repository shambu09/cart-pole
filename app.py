import pyglet
from config import (
    WINDOW_NAME,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)

from objects import (
    Pole,
    Cart,
)

WINDOW_CONFIG = (WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_NAME)


class App(pyglet.window.Window):

    def __init__(self):
        super(App, self).__init__(*WINDOW_CONFIG)
        self.pole = Pole()
        self.cart = Cart()

        self.freefall = True

        pyglet.clock.schedule_interval(self.update, 0.025)

    def update(self, dt):
        if self.freefall:
            self.pendulum.update(dt)

    def on_key_press(self, symbol, modifiers):
        super(App, self).on_key_press(symbol, modifiers)
        if symbol == pyglet.window.key.SPACE:
            self.freefall = False

    def on_key_release(self, symbol, modifiers):
        super(App, self).on_key_press(symbol, modifiers)
        if symbol == pyglet.window.key.SPACE:
            self.freefall = True

    def on_mouse_press(self, x, y, button, modifiers):
        self.freefall = False

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.pendulum.reset(x, y)

    def on_mouse_release(self, x, y, button, modifiers):
        self.freefall = True

    def on_draw(self):
        self.clear()
        self.pendulum.draw()


if __name__ == '__main__':
    window = App()
    pyglet.app.run()