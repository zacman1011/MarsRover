import random

from constants.instructions import Instruction

INSTRUCTION_OPTIONS = list(Instruction)


def generate_instructions(num_sets=1, length_of_sets=10):
    instructions_list = []
    for _ in range(num_sets):
        instructions = []
        for _ in range(length_of_sets):
            instructions.append(random.choice(INSTRUCTION_OPTIONS))
        instructions_list.append(instructions)
    return instructions_list
