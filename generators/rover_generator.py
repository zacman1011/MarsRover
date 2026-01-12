import random

from constants.direction import Direction
from rovers.insomniac import Insomniac
from rovers.jumper import Jumper
from rovers.madman import Madman
from rovers.octopus import Octopus
from rovers.rover import Rover

ROVER_TYPE_OPTIONS = [Rover, Insomniac, Jumper, Madman, Octopus]


def generate_rovers(board, num_rovers=1, rover_types=None):
    if rover_types is None:
        rover_types = ROVER_TYPE_OPTIONS

    min_x = board.min_coord[0]
    min_y = board.min_coord[1]
    max_x = board.max_coord[0]
    max_y = board.max_coord[1]

    rovers = []
    for rid in range(num_rovers):
        rover_type = random.choice(rover_types)
        direction = generate_direction()
        rover = rover_type(
            x=random.randint(min_x, max_x),
            y=random.randint(min_y, max_y),
            direction=direction,
            board=board,
            rid=rid
        )
        rovers.append(rover)
    return rovers


def generate_direction():
    return random.choice(list(Direction))
