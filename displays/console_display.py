from displays.display import Display


class ConsoleDisplay(Display):

    @staticmethod
    def start():
        print("Starting...")

    @staticmethod
    def display(board):
        print(board)

    @staticmethod
    def finish(_board):
        print("Finished")
