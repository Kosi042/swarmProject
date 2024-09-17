import pygame
import numpy as np
import constants
import colorsys

from agent import Agent

pygame.init()
font = pygame.font.Font(None, 30)

class Environment(pygame.sprite.Group):

    def __init__(self):
        super().__init__()

        self.follow_camera = 0
        self.draw_text = False
        self.draw_values = False
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

        # Camera Movement
        self.offset = pygame.math.Vector2()

        # Paint value matrix
        self.value_color_green = 255
        self.tile_size = 50
        # Create random value Matrix
        self.value_matrix = np.zeros((self.internal_surf_size[0] // self.tile_size,
                                      self.internal_surf_size[1] // self.tile_size))
        self.rects = self.create_value_matrix()

    def keyboard_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.zoom_scale += 0.05
        if keys[pygame.K_e]:
            self.zoom_scale -= 0.05
        if keys[pygame.K_w]:
            self.internal_offset.y += 5
        if keys[pygame.K_s]:
            self.internal_offset.y -= 5
        if keys[pygame.K_a]:
            self.internal_offset.x += 5
        if keys[pygame.K_d]:
            self.internal_offset.x -= 5
        if keys[pygame.K_p]:
            self.internal_offset.x = self.internal_surf_size[0] // 2 - constants.WIDTH / 2
            self.internal_offset.y = self.internal_surf_size[1] // 2 - constants.HEIGHT / 2
        if keys[pygame.K_c]:
            self.internal_offset.x = 0
            self.internal_offset.y = 0

        # Clamp Zoom
        self.zoom_scale = pygame.math.clamp(self.zoom_scale,
                                            constants.WIDTH / self.internal_surf_size[0],
                                            (constants.WIDTH + self.internal_surf_size[0]) * 2 /
                                            self.internal_surf_size[0])


        if self.zoom_scale == constants.WIDTH / self.internal_surf_size[0]:
            self.internal_offset.x = 0
            self.internal_offset.y = 0
        else:
            self.internal_offset.x = pygame.math.clamp(self.internal_offset.x, -1370, 1370)
            self.internal_offset.y = pygame.math.clamp(self.internal_offset.y, -770, 770)

        # x_limit = int(self.zoom_scale * 572.5 - 229)
        # y_limit = int(self.zoom_scale * 322.5 - 129)
        # self.internal_offset.x = pygame.math.clamp(self.internal_offset.x, -x_limit, x_limit)
        # self.internal_offset.y = pygame.math.clamp(self.internal_offset.y, -y_limit, y_limit)


    def create_value_matrix(self, seed= 0):
        np.random.seed(seed)
        rects = []

        # Generate random values
        random_matrix= np.random.randint(low= -10, high= 110, size= (self.internal_surf_size[0] // self.tile_size,
                                   self.internal_surf_size[1] // self.tile_size))

        # Smooth out with kernel
        for i in range(self.value_matrix.shape[0]-2):
            for j in range(self.value_matrix.shape[1]-2):

                s = random_matrix[i:i + 3, j:j + 3] @ np.array([1, 1, 1])
                s = np.array([1, 1, 1]).T @ s
                s = int(s / 9)
                self.value_matrix[i+1][j+1]= pygame.math.clamp(s, 0, 100)

        # Create rects
        for i in range(self.value_matrix.shape[0]):
            for j in range(self.value_matrix.shape[1]):
                if self.value_matrix[i][j] > 0:
                    color = colorsys.hsv_to_rgb(self.value_matrix[i][j]/360, 1., 1. )
                    color = tuple(int(c * 255) for c in color)
                    rects.append((color, (i * self.tile_size, j * self.tile_size),
                                                              (self.tile_size, self.tile_size)))
                else:
                    rects.append(((0, 0, 0), (i * self.tile_size, j * self.tile_size),
                                                              (self.tile_size, self.tile_size)))

        return rects

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - constants.WIDTH // 2
        self.offset.y = target.rect.centery - constants.HEIGHT // 2


    def update(self):
        # Keyboard
        self.keyboard_control()

        # Ground
        ground_offset = self.ground_rect.topleft  - self.offset + self.internal_offset
        self.game_display.fill((0, 0, 0))
        self.internal_surf.blit(self.ground_surf, ground_offset)

        for rect in self.rects:
            if self.draw_values or rect[0] == (0,0,0):
                rect_offset = rect[1] - self.offset + self.internal_offset
                r = pygame.rect.Rect(rect_offset, rect[2])
                pygame.draw.rect(self.internal_surf, rect[0], r)

                if self.draw_text:
                    text = font.render(f"{int(self.value_matrix[rect[1][0] // self.tile_size][rect[1][1] // self.tile_size])}"
                        , True, (255, 255, 255))
                    self.internal_surf.blit(text, rect_offset + pygame.math.Vector2(15, 15))

        self.follow_camera = self.follow_camera % (len(self.sprites()) + 1)
        # Draw
        for num, sprite in enumerate(self.sprites()):

            if isinstance(sprite, Agent):
                if num == self.follow_camera:
                    self.center_target_camera(sprite)
                sprite.update(self.value_matrix[sprite.rect.centerx // self.tile_size]
                                               [sprite.rect.centery // self.tile_size])

            offset_pos = sprite.rect.topleft - self.offset + self.internal_offset

            self.internal_surf.blit(sprite.image, offset_pos)

        # Zoom


        scaled_surf = pygame.transform.scale(self.internal_surf, self.internal_surf_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center=(constants.WIDTH / 2, constants.HEIGHT / 2))

        self.game_display.blit(scaled_surf, scaled_rect)

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