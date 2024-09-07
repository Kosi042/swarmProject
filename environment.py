import pygame

WIDTH = 800
HEIGHT = 600


class Environment:

    def __init__(self):
        self.game_display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Swarm Sim")
        self.clock = pygame.time.Clock()

    def update(self):
        self.game_display.fill((255, 255, 255))
        pygame.display.update()
        self.clock.tick(60)


def main():
    e = Environment()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        e.update()


if __name__ == "__main__":
    main()