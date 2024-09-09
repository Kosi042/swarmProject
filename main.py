import pygame
from environment import Environment
from agent import Agent

#cam = pygame.camera.Camera()

def main():
    env = Environment()
    a = Agent(env.internal_surf, x= 1000, y= 1000)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEWHEEL:
                env.zoom_scale += event.y * 0.03
        env.update()
        a.update()
        #pygame.display.update()


if __name__ == "__main__":
    main()
