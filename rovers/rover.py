import uuid

from constants.direction import Direction
from constants.instructions import Instruction


class Rover:
    def __init__(self, x, y, direction, board):
        self.id = uuid.uuid4()
        self.x = x
        self.y = y
        self.direction = direction
        self.board = board
        self.lost = False

        # Add to the board
        self.board.update_rover_position(self)

    def process(self, instruction):
        if self.lost:
            print("Rover cannot process instruction as it is lost")
            return

        if instruction == Instruction.F:
            self._forward()
            self.board.update_rover_position(self)
        elif instruction == Instruction.R:
            self._rotate_right()
        elif instruction == Instruction.L:
            self._rotate_left()
        else:
            print(f"Invalid instruction {instruction} - cannot process")
            return

        self.__check_lost()

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
            print(f"Invalid direction {self.direction} - cannot move forward")
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
            print(f"Invalid direction{self.direction} - cannot move rotate left")

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
            print(f"Invalid direction{self.direction} - cannot move rotate right")

    def __check_lost(self):
        self.lost = not self.board.on_board(self.x, self.y)
        if self.lost: print("Rover lost")

    def location(self):
        return self.x, self.y

    def __str__(self):
        if self.lost: return "LOST"

        return f"{self.x}, {self.y}, {self.direction}"
