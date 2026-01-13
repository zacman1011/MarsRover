import numpy as np


class Board:
    def __init__(self, min_coord, max_coord, obstacles=None):
        if obstacles is None:
            obstacles = []

        self.min_coord = min_coord
        self.max_coord = max_coord
        self.obstacles = list(set(obstacles))
        self.rovers = {}
        self.rover_types = {}

    def on_board(self, x, y):
        return self.min_coord[0] <= x <= self.max_coord[0] and self.min_coord[1] <= y <= self.max_coord[1]

    def free_space(self, x, y):
        return (x, y) not in self.obstacles and (x, y) not in self.rovers.values()

    def update_rover_position(self, rover):
        if rover.lost:
            self.rovers.pop(rover.id, None)
            return

        self.rover_types[rover.id] = rover.rover_type(abbr=True)
        self.rovers[rover.id] = rover.location()

    def np_array(self):
        output = []
        rovers = {}
        for rid in self.rovers:
            location = self.rovers[rid]
            rovers[location] = rid

        for y in range(self.min_coord[1], self.max_coord[1] + 1):
            row = []
            for x in range(self.min_coord[0], self.max_coord[0] + 1):
                if (x, y) in self.obstacles:
                    row.append(1)
                elif (x, y) in rovers:
                    rid = rovers[(x, y)]
                    row.append(2 + rid)
                else:
                    row.append(0)
            output.append(row)
        output.reverse()
        return np.array(output)

    def __str__(self):
        output = []
        rovers = {}
        for rid in self.rovers:
            location = self.rovers[rid]
            abbr = self.rover_types[rid]
            rovers[location] = abbr

        for y in range(self.min_coord[1], self.max_coord[1] + 1):
            row = ""
            for x in range(self.min_coord[0], self.max_coord[0] + 1):
                if (x, y) in self.obstacles:
                    row += "X"
                elif (x, y) in rovers:
                    abbr = rovers[(x, y)]
                    row += abbr
                else:
                    row += "-"
            output.append(row)
        output.reverse()
        return "\n".join(output)
