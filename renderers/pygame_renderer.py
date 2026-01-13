import pygame

from renderers.renderer import Renderer


class PygameRenderer(Renderer):
    CELL_SIZE = 10  # pixels per grid cell

    def __init__(self, grid_width, grid_height):
        pygame.init()
        self.width = grid_width * self.CELL_SIZE
        self.height = grid_height * self.CELL_SIZE
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mars Rover")
        self.clock = pygame.time.Clock()
        self.running = True

    @staticmethod
    def start():
        pass

    def display(self, board):
        grid = board.grid(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.screen.fill((0, 0, 0))  # clear screen

        for y, row in enumerate(grid):
            for x, colour in enumerate(row):
                rect = pygame.Rect(
                    x * self.CELL_SIZE,
                    y * self.CELL_SIZE,
                    self.CELL_SIZE,
                    self.CELL_SIZE
                )
                pygame.draw.rect(self.screen, colour, rect)

        pygame.display.flip()
        self.clock.tick(10)  # FPS limit (adjust speed)

    @staticmethod
    def finish():
        pygame.quit()
