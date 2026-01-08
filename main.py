from board import Board
from constants.direction import Direction
from constants.instructions import Instruction
from rovers.jumper import Jumper
from rovers.octopus import Octopus
from rovers.rover import Rover
from runners.runner import Runner


def run():
    board = Board((0, 0), (20, 20), obstacles=[])

    rover1 = Rover(x=1, y=1, direction=Direction.N, board=board)
    rover2 = Jumper(x=1, y=1, direction=Direction.N, board=board)
    rover3 = Octopus(x=1, y=1, direction=Direction.N, board=board)

    runner = Runner(board=board, rovers=[rover1, rover2, rover3])

    instructions = [
        [Instruction.F, Instruction.F, Instruction.R, Instruction.F, "BAD", Instruction.F],
    ]

    runner.run(instructions_list=instructions)


if __name__ == '__main__':
    run()
