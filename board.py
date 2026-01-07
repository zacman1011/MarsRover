class Board:
    def __init__(self, min_coord, max_coord, obstacles=None):
        if obstacles is None:
            obstacles = []

        self.min_coord = min_coord
        self.max_coord = max_coord
        self.obstacles = obstacles

    def on_board(self, x, y):
        return self.min_coord[0] <= x <= self.max_coord[0] and self.min_coord[1] <= y <= self.max_coord[1]

    def free_space(self, x, y):
        return (x, y) not in self.obstacles
