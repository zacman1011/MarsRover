import random
import uuid

from constants.direction import Direction
from constants.instructions import Instruction


class Rover:
    def __init__(self, x, y, direction, board, rid=None, log_level=1):
        if rid is None:
            rid = uuid.uuid4()

        self.id = rid
        self.x = x
        self.y = y
        self.direction = direction
        self.board = board
        self.lost = False
        self.log_level = log_level

        r = random.randint(0, 255)
        g = random.randint(0, 255 - r)
        b = 255 - g - r
        self.colour = (r, g, b)

        # Add to the board
        self.board.add_rover(self)

    @staticmethod
    def rover_type(abbr=False):
        if abbr:
            return "R"
        return "Rover"

    def process(self, instruction):
        if self.lost:
            self.print_message("Rover cannot process instruction as it is lost", 1)
            return

        if instruction == Instruction.F:
            self._forward()
        elif instruction == Instruction.R:
            self._rotate_right()
        elif instruction == Instruction.L:
            self._rotate_left()
        elif instruction == Instruction.SKIP:
            return
        else:
            self.print_message(f"Invalid instruction {instruction} - cannot process", 2)
            return

        self.__check_lost()
        self.board.update_rover_position(self)

    def _forward(self):
        new_x = self.x
        new_y = self.y
        if self.direction == Direction.N:
            new_y += 1
        elif self.direction == Direction.S:
            new_y -= 1
        elif self.direction == Direction.E:
            new_x += 1
        elif self.direction == Direction.W:
            new_x -= 1
        else:
            self.print_message(f"Invalid direction {self.direction} - cannot move forward", 2)
            return

        if self.board.free_space(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def _rotate_left(self):
        if self.direction == Direction.N:
            self.direction = Direction.W
        elif self.direction == Direction.W:
            self.direction = Direction.S
        elif self.direction == Direction.S:
            self.direction = Direction.E
        elif self.direction == Direction.E:
            self.direction = Direction.N
        else:
            self.print_message(f"Invalid direction {self.direction} - cannot move rotate left", 2)

    def _rotate_right(self):
        if self.direction == Direction.N:
            self.direction = Direction.E
        elif self.direction == Direction.E:
            self.direction = Direction.S
        elif self.direction == Direction.S:
            self.direction = Direction.W
        elif self.direction == Direction.W:
            self.direction = Direction.N
        else:
            self.print_message(f"Invalid direction {self.direction} - cannot move rotate right", 2)

    def __check_lost(self):
        self.lost = not self.board.on_board(self.x, self.y)
        if self.lost: self.print_message(f"{self.rover_type()} {self.id} lost", 1)

    def location(self):
        return self.x, self.y

    def __str__(self):
        if self.lost: return f"{self.rover_type()} {self.id}: LOST"

        return f"{self.rover_type()} {self.id}: ({self.x}, {self.y}) {self.direction}"

    def print_message(self, content, min_level=0):
        if self.log_level >= min_level:
            print(f"{self.rover_type()} {self.id}: {content}")
