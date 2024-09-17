

import pygame
import math


# Load image

agent_img = pygame.image.load("graphics/agent_big_cyan.png")
agent_img = pygame.transform.scale(agent_img, (20, 20))

class Agent(pygame.sprite.Sprite):

    def __init__(self, game_display, group, color: tuple = (0, 255, 255),
                 x: int = 200, y: int = 200, size: int = 10,
                 speed: int = 1, direction: int = 0):

        # Inherat
        super().__init__(group)

        # Movement variables
        self.pos = pygame.math.Vector2(x, y)
        self.speed = speed
        self.size = size
        self.direction = direction % 360

        # Drawing variables
        self.image = agent_img
        self.rect = self.image.get_rect(center= self.pos)
        self.color = color
        self.game_display = game_display

    def move(self):
        self.rotate(-1)
        self.pos.x += self.speed * math.cos(math.radians(self.direction))
        self.pos.y += self.speed * math.sin(math.radians(self.direction))


    def rotate(self, angle):
        self.direction = (self.direction % 360) + angle


    def update(self, value):
        # print(value)
        self.image = pygame.transform.rotate(agent_img, -self.direction)
        self.rect = self.image.get_rect(center= self.pos)
        self.move()



def main():
    print("No main function")


if __name__ == "__main__":
    main()