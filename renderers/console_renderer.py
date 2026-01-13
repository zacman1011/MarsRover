from renderers.renderer import Renderer


class ConsoleRenderer(Renderer):

    @staticmethod
    def start():
        print("Starting...")

    @staticmethod
    def display(board):
        print(board)

    @staticmethod
    def finish():
        print("Finished")
