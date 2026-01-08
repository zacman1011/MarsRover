import random

from board import Board
from direction import Direction
from rover import Rover


class Runner:
    def __init__(self, num_rovers=1, board=None, rovers=None):
        if board is None:
            board = Board((0, 0), (100, 100))

        self.board = board
        self.num_rovers = num_rovers

        if rovers is None:
            rovers = []
            for i in range(num_rovers):
                rovers.append(
                    Rover(
                        random.randint(board.min_coord[0], board.max_coord[0]),
                        random.randint(board.min_coord[1], board.max_coord[1]),
                        random.choice(list(Direction)),
                        self.board
                    )
                )

        self.rovers = rovers

    def run(self, instructions_list):
        print("Running...")
        num_instructions = len(instructions_list)
        for index, rover in enumerate(self.rovers):
            print(f"Start: {rover}")
            instructions = instructions_list[index % num_instructions]
            for instruction in instructions:
                rover.process(instruction)
            print(f"Finished: {rover}")
        print("Finished")
