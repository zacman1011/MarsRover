import random


def generate_obstacles(min_coord, max_coord, num_obstacles=10):
    obstacles = []
    for _ in range(num_obstacles):
        obstacle = generate_obstacle(min_coord, max_coord)
        while obstacle in obstacles:
            obstacle = generate_obstacle(min_coord, max_coord)
        obstacles.append(obstacle)
    return obstacles


def generate_obstacle(min_coord, max_coord):
    return random.randint(min_coord[0], max_coord[0]), random.randint(min_coord[1], max_coord[1])
