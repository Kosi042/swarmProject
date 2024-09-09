import pygame
import math

class Agent:

    def __init__(self, color: tuple = (255, 0, 0),
                 x: int = 200, y: int = 200, size: int = 10,
                 speed: int = 1, direction: int = 0):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        self.direction = direction

    def move(self):

        self.direction = self.direction % 360
        self.x += self.speed * math.cos(math.radians(self.direction))
        self.y += self.speed * math.sin(math.radians(self.direction))

    def update(self, game_display):
        print(self.x, self.y)
        self.move()
        pygame.draw.circle(game_display, self.color, [self.x, self.y], self.size)


def main():
    print("No main function")


if __name__ == "__main__":
    main()