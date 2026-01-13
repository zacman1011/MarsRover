from board import Board
from constants.direction import Direction
from constants.instructions import Instruction
from generators.instructions_generator import generate_instructions
from generators.obstacle_generator import generate_obstacles
from generators.rover_generator import generate_rovers
from rovers.insomniac import Insomniac
from rovers.jumper import Jumper
from rovers.octopus import Octopus
from rovers.rover import Rover
from runners.runner import Runner
from runners.stepper import Stepper


def run1():
    min_coord = (0, 0)
    max_coord = (20, 20)
    obstacles = generate_obstacles(min_coord, max_coord)

    board = Board(min_coord=min_coord, max_coord=max_coord, obstacles=obstacles)

    rover1 = Rover(x=1, y=1, direction=Direction.N, board=board, rid=1)
    rover2 = Jumper(x=5, y=5, direction=Direction.N, board=board, rid=2)
    rover3 = Octopus(x=10, y=10, direction=Direction.N, board=board, rid=3)
    rover4 = Rover(x=15, y=15, direction=Direction.N, board=board, rid=4)
    rovers = [rover1, rover2, rover3, rover4]

    runner = Runner(board=board, rovers=rovers)

    instructions = generate_instructions(len(rovers), 15)

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

    rover1 = Insomniac(x=9, y=9, direction=Direction.N, board=board)

    rovers = [rover1]

    runner = Runner(board=board, rovers=rovers)

    instructions = [
        [Instruction.F, Instruction.F, Instruction.F, Instruction.F]
    ]

    runner.run(instructions_list=instructions)


def run4():
    min_coord = (0, 0)
    max_coord = (30, 15)
    obstacles = generate_obstacles(min_coord, max_coord, 30)
    board = Board(min_coord=min_coord, max_coord=max_coord, obstacles=obstacles)
    rovers = generate_rovers(board, 1)
    runner = Stepper(board=board, rovers=rovers)
    instructions = generate_instructions(len(rovers), 20)
    runner.run(instructions)


if __name__ == '__main__':
    run4()
