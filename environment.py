import pygame
import constants


class Environment:

    def __init__(self):
        self.game_display = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        pygame.display.set_caption("Swarm Sim")
        self.clock = pygame.time.Clock()

        # Background image
        self.ground_surf = pygame.image.load('graphics/background_test.png').convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))

        # Zoom
        self.zoom_scale = 1
        self.internal_surf_size = (3200, 1800)
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(center=(constants.WIDTH/2, constants.HEIGHT/2))
        self.internal_surf_size_vector = pygame.math.Vector2(self.internal_surf_size)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surf_size[0] // 2 - constants.WIDTH/2
        self.internal_offset.y = self.internal_surf_size[1] // 2 - constants.HEIGHT/2

    def zoom_keyboard_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.zoom_scale += 0.1
        if keys[pygame.K_e]:
            self.zoom_scale -= 0.1

    def update(self):
        # Ground
        # ground_offset = self.ground_rect.topleft # - self.offset + self.internal_offset
        # self.internal_surf.blit(self.ground_surf, ground_offset)

        # Zoom
        self.zoom_scale = pygame.math.clamp(self.zoom_scale,
                                            constants.WIDTH/self.internal_surf_size[0],
                                            (constants.WIDTH + self.internal_surf_size[0])/self.internal_surf_size[0])
        scaled_surf = pygame.transform.scale(self.internal_surf, self.internal_surf_size_vector * self.zoom_scale)
        print(self.internal_surf_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center= (constants.WIDTH/2, constants.HEIGHT/2))

        # Draw
        pygame.draw.circle(self.internal_surf, (255, 0, 0), (1000, 1000), 100)
        self.internal_surf.fill((255, 255, 255))
        pygame.draw.circle(self.internal_surf, (0, 255, 0), (1000, 1000), 80)
        #self.game_display.fill((255, 255, 255))
        pygame.draw.circle(self.internal_surf, (0, 255, 0), (1000, 1000), 50)
        # self.game_display.blit(scaled_surf, scaled_rect)
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