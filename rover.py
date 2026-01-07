class Rover:
    def __init__(self, x, y, direction, board):
        self.x = x
        self.y = y
        self.direction = direction
        self.board = board
        self.lost = False

    def process(self, instruction):
        if self.lost:
            print("Rover cannot process instruction as it is lost")
            return

        if instruction == "F":
            self.__forward()
        elif instruction == "R":
            self.__rotate_right()
        elif instruction == "L":
            self.__rotate_left()
        else:
            print(f"Invalid instruction {instruction} - cannot process")
            return

        self.__check_lost()

    def __forward(self):
        new_x = self.x
        new_y = self.y
        if self.direction == "N":
            new_y += 1
        elif self.direction == "S":
            new_y -= 1
        elif self.direction == "E":
            new_x += 1
        elif self.direction == "W":
            new_x -= 1
        else:
            print(f"Invalid direction {self.direction} - cannot move forward")
            return

        if self.board.free_space(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def __rotate_left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"
        elif self.direction == "W":
            self.direction = "S"
        else:
            print(f"Invalid direction{self.direction} - cannot move rotate left")

    def __rotate_right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "W":
            self.direction = "N"
        else:
            print(f"Invalid direction{self.direction} - cannot move rotate right")

    def __check_lost(self):
        self.lost = not self.board.on_board(self.x, self.y)
        if self.lost: print("Rover lost")

    def __str__(self):
        if self.lost: return "LOST"

        return f"{self.x}, {self.y}, {self.direction}"
