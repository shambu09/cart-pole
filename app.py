import pyglet
from config import (
    WINDOW_NAME,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)

from objects import CartPole

WINDOW_CONFIG = (WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_NAME)


class App(pyglet.window.Window):

    def __init__(self):
        super(App, self).__init__(*WINDOW_CONFIG)
        self.cartpole = CartPole()

        self.keys = {}
        pyglet.clock.schedule_interval(self.update, 1 / 60.0)

        # self.frame = 0

    def update(self, dt):
        if self.keys.get(pyglet.window.key.LEFT, False):
            self.cartpole.left()

        elif self.keys.get(pyglet.window.key.RIGHT, False):
            self.cartpole.right()

        else:
            self.cartpole.force = 0

        self.cartpole.update(dt)

    def on_key_press(self, symbol, modifiers):
        super(App, self).on_key_press(symbol, modifiers)
        self.keys[symbol] = True

    def on_key_release(self, symbol, modifiers):
        self.keys[symbol] = False

    def on_draw(self):
        self.clear()
        self.cartpole.draw()

        # Download the frames.
        # pyglet.image.get_buffer_manager().get_color_buffer().save(f"res/{self.frame}.png")
        # self.frame += 1


if __name__ == '__main__':
    window = App()
    pyglet.app.run()