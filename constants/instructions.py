from enum import Enum


class Instruction(Enum):
    F = "Forward",
    R = "Right rotation",
    L = "Left rotation",
    SKIP = "Skip"
