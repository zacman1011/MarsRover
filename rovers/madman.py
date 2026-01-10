import random

from constants.instructions import Instruction
from rovers.rover import Rover


class Madman(Rover):
    def process(self, instruction):
        next_instruction = random.choice(list(Instruction))
        print(f"Ignoring instruction: {instruction} and doing {next_instruction} instead")
        super().process(next_instruction)
