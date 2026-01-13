from constants.direction import Direction
from rovers.rover import Rover


class Jumper(Rover):

    @staticmethod
    def rover_type(abbr=False):
        if abbr:
            return "J"
        return "Jumper"

    def _forward(self):
        new_x = self.x
        new_y = self.y
        if self.direction == Direction.N:
            new_y += 2
        elif self.direction == Direction.S:
            new_y -= 2
        elif self.direction == Direction.E:
            new_x += 2
        elif self.direction == Direction.W:
            new_x -= 2
        else:
            self.print_message(f"Invalid direction {self.direction} - cannot move forward")
            return

        if self.board.free_space(new_x, new_y):
            self.x = new_x
            self.y = new_y
