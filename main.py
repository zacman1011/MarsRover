from board import Board
from constants.direction import Direction
from constants.instructions import Instruction
from rover import Rover
from runners.runner import Runner


def run():
    board = Board((0, 0), (10, 10), obstacles=[(1, 3)])

    rover1 = Rover(x=1, y=1, direction=Direction.N, board=board)

    runner = Runner(board=board, rovers=[rover1])

    instructions = [
        [Instruction.F, Instruction.F, Instruction.R, Instruction.F, "BAD", Instruction.F],
    ]

    runner.run(instructions_list=instructions)


if __name__ == '__main__':
    run()
