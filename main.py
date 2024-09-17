import pygame
from pygame.display import update

from environment import Environment
from agent import Agent

def match_key(env, key):
    match key:
        case pygame.K_t:
            env.draw_values = not env.draw_values
        case pygame.K_f:
            env.draw_text = not env.draw_text
        case pygame.K_p:
            env.follow_camera += 1


def main():

    env = Environment()

    #agents = [Agent(env.internal_surf, env, x= 1000 + i*100, y= 300 + i*100) for i in range(10)]
    a = Agent(env.internal_surf, env, x= 1600, y= 900)
    env.follow_camera = len(env.sprites())
    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    quit()
                case pygame.MOUSEWHEEL:
                    env.zoom_scale += event.y * 0.03
                case pygame.KEYDOWN:
                    match_key(env, event.key)

        # for a in agents: a.update()
        # a.update()
        env.update()
        pygame.display.update()


if __name__ == "__main__":
    main()
