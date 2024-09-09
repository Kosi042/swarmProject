import pygame
from environment import Environment
from agent import Agent


def main():
    env = Environment()
    a = Agent(size= 5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        env.update()
        a.update(env.game_display)
        pygame.display.update()


if __name__ == "__main__":
    main()
