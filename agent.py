import pygame
import math
from collections import namedtuple


class Agent:

    def __init__(self, game_display, color: tuple = (255, 0, 0),
                 x: int = 200, y: int = 200, size: int = 10,
                 speed: int = 1, direction: int = 0):

        self.pos = pygame.math.Vector2(x, y)
        self.size = size
        self.color = color
        self.speed = speed
        self.direction = direction % 360
        self.dir_indicator = pygame.math.Vector2(self.size * math.cos(math.radians(self.direction)),
                                                 self.size * math.sin(math.radians(self.direction)))
        self.game_display = game_display

    def move(self):
        self.direction = (self.direction % 360) + 1
        self.pos.x += self.speed * math.cos(math.radians(self.direction))
        self.pos.y += self.speed * math.sin(math.radians(self.direction))
        self.dir_indicator.x = self.size * math.cos(math.radians(self.direction))
        self.dir_indicator.y = self.size * math.sin(math.radians(self.direction))

    def update(self):
        print(self.direction)
        self.move()
        pygame.draw.circle(self.game_display, self.color, self.pos, self.size)
        pygame.draw.line(self.game_display, (0, 0, 0), self.pos,
                         self.pos + self.dir_indicator)


def main():
    print("No main function")


if __name__ == "__main__":
    main()