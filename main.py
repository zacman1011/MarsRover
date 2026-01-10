from board import Board
from constants.direction import Direction
from constants.instructions import Instruction
from rovers.amnesiac import Amnesiac
from rovers.jumper import Jumper
from rovers.octopus import Octopus
from rovers.rover import Rover
from runners.runner import Runner
from runners.stepper import Stepper


def run1():
    board = Board((0, 0), (20, 20), obstacles=[])

    rover1 = Rover(x=1, y=1, direction=Direction.N, board=board)
    rover2 = Jumper(x=1, y=1, direction=Direction.N, board=board)
    rover3 = Octopus(x=1, y=1, direction=Direction.N, board=board)
    rover4 = Rover(x=1, y=1, direction=Direction.N, board=board)

    runner = Runner(board=board, rovers=[rover1, rover2, rover3, rover4])

    instructions = [
        [Instruction.F, Instruction.F, Instruction.R, Instruction.F, "BAD", Instruction.F],
    ]

    runner.run(instructions_list=instructions)


def run2():
    board = Board((0, 0), (20, 20), obstacles=[])

    rover1 = Rover(x=2, y=1, direction=Direction.N, board=board)
    rover2 = Rover(x=1, y=2, direction=Direction.E, board=board)

    rovers = [rover1, rover2]

    runner = Stepper(board=board, rovers=rovers)

    instructions = [
        [Instruction.F, Instruction.F]
    ]

    runner.run(instructions_list=instructions)


def run3():
    board = Board((0, 0), (20, 20), obstacles=[])

    rover1 = Amnesiac(x=9, y=9, direction=Direction.N, board=board)

    rovers = [rover1]

    runner = Runner(board=board, rovers=rovers)

    instructions = [
        [Instruction.F, Instruction.F, Instruction.F, Instruction.F]
    ]

    runner.run(instructions_list=instructions)


if __name__ == '__main__':
    run3()
