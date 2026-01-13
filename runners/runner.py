from board import Board
from generators.rover_generator import generate_rovers


class Runner:
    def __init__(self, num_rovers=1, board=None, rovers=None):
        if board is None:
            board = Board((0, 0), (100, 100))

        self.board = board
        self.num_rovers = num_rovers

        if rovers is None:
            rovers = generate_rovers(self.board, self.num_rovers)

        self.rovers = rovers

    def run(self, instructions_list):
        print("Running...")
        print(self.board)
        num_instructions = len(instructions_list)
        for index, rover in enumerate(self.rovers):
            print(f"Start: {rover}")
            instructions = instructions_list[index % num_instructions]
            for instruction in instructions:
                rover.process(instruction)
            print(f"Finished: {rover}\n")
        print("Finished")
        print(self.board)
