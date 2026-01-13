import random

from constants.instructions import Instruction
from rovers.rover import Rover


class Madman(Rover):

    @staticmethod
    def rover_type(abbr=False):
        if abbr:
            return "M"
        return "Madman"

    def process(self, instruction):
        next_instruction = random.choice(list(Instruction))
        self.print_message(f"Ignoring instruction: {instruction} and doing {next_instruction} instead", 1)
        super().process(next_instruction)
