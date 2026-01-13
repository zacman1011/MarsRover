import matplotlib

matplotlib.use("Qt5Agg")

import matplotlib.pyplot as plt

from renderers.renderer import Renderer


class MatplotlibRenderer(Renderer):
    def __init__(self):
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.im = None

        self.fig.show()
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    @staticmethod
    def start():
        pass

    def display(self, board):
        arr = board.np_array()

        if self.im is None:
            self.im = self.ax.imshow(arr, cmap="viridis")
            self.ax.set_xticks([])
            self.ax.set_yticks([])
        else:
            self.im.set_data(arr)

        plt.draw()
        plt.pause(0.1)

    @staticmethod
    def finish(_board):
        plt.ioff()
        plt.show()
