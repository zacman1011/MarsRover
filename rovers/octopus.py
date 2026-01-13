from constants.direction import Direction
from rovers.rover import Rover


class Octopus(Rover):

    @staticmethod
    def rover_type(abbr=False):
        if abbr:
            return "O"
        return "Octopus"

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
        elif self.direction == Direction.NE:
            new_y += 1
            new_x += 1
        elif self.direction == Direction.NW:
            new_y += 1
            new_x -= 1
        elif self.direction == Direction.SE:
            new_y -= 1
            new_x += 1
        elif self.direction == Direction.SW:
            new_y -= 1
            new_x -= 1
        else:
            self.print_message(f"Invalid direction {self.direction} - cannot move forward", 2)
            return

        if self.board.free_space(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def _rotate_left(self):
        if self.direction == Direction.N:
            self.direction = Direction.NW
        elif self.direction == Direction.NW:
            self.direction = Direction.W
        elif self.direction == Direction.W:
            self.direction = Direction.SW
        elif self.direction == Direction.SW:
            self.direction = Direction.S
        elif self.direction == Direction.S:
            self.direction = Direction.SE
        elif self.direction == Direction.SE:
            self.direction = Direction.E
        elif self.direction == Direction.E:
            self.direction = Direction.NE
        elif self.direction == Direction.NE:
            self.direction = Direction.N
        else:
            self.print_message(f"Invalid direction {self.direction} - cannot move rotate left", 2)

    def _rotate_right(self):
        if self.direction == Direction.N:
            self.direction = Direction.NE
        elif self.direction == Direction.NE:
            self.direction = Direction.E
        elif self.direction == Direction.E:
            self.direction = Direction.SE
        elif self.direction == Direction.SE:
            self.direction = Direction.S
        elif self.direction == Direction.S:
            self.direction = Direction.SW
        elif self.direction == Direction.SW:
            self.direction = Direction.W
        elif self.direction == Direction.W:
            self.direction = Direction.NW
        elif self.direction == Direction.NW:
            self.direction = Direction.N
        else:
            self.print_message(f"Invalid direction {self.direction} - cannot move rotate right", 2)
