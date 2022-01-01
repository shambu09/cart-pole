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

        self.keys = {}
        pyglet.clock.schedule_interval(self.update, 1 / 60.0)

    def update(self, dt):
        if self.keys.get(pyglet.window.key.LEFT, False):
            self.cart.left()
        
        if self.keys.get(pyglet.window.key.RIGHT, False):
            self.cart.right()

    def on_key_press(self, symbol, modifiers):
        super(App, self).on_key_press(symbol, modifiers)
        self.keys[symbol] = True

    def on_key_release(self, symbol, modifiers):
        self.keys[symbol] = False

    def on_draw(self):
        self.clear()
        self.cart.draw()

if __name__ == '__main__':
    window = App()
    pyglet.app.run()