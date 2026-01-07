from board import Board
from rover import Rover
from runners.runner import Runner


def run():
    board = Board((0, 0), (10, 10))

    rover1 = Rover(x=1, y=1, direction="N", board=board)

    runner = Runner(board=board, rovers=[rover1])

    instructions = [["F", "F", "R", "F", "BAD", "F"]]

    runner.run(instructions_list=instructions)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
