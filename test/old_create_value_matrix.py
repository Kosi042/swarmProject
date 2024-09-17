def create_value_matrix(self):
    print(self.value_matrix.shape)
    print(self.value_matrix.size)
    rects = []
    orientations = ((1, 0), (0, 1), (-1, 0), (0, -1))

    # Create boarder with value -10
    for i in range(self.value_matrix.shape[0]):
        for j in range(self.value_matrix.shape[1]):
            g = self.value_color_green
            g += random.randint(-1, 1) * 10
            g = pygame.math.clamp(g, 0, 255)
            self.value_color_green = g
            if i == 0 or j == 0 or i == self.value_matrix.shape[0] - 1 or j == self.value_matrix.shape[1] - 1:
                self.value_matrix[i][j] = -10
            elif (i + j) % 2 == 0 and i % 2 == 0 and j % 2 == 0:
                self.value_matrix[i][j] = g

    for i in range(1, self.value_matrix.shape[0] - 1):
        for j in range(1, self.value_matrix.shape[1] - 1):
            if (i + j) % 2 == 1:
                temp = 0
                number_of_adds = 0

                for orientation in orientations:
                    if self.value_matrix[i + orientation[0]][j + orientation[1]] > 0:
                        temp += self.value_matrix[i + orientation[0]][j + orientation[1]]
                        number_of_adds += 1
                if number_of_adds != 0:
                    sum_div = int(temp / number_of_adds)
                    self.value_matrix[i][j] = sum_div
                else:
                    self.value_matrix[i][j] = int(temp / 2)

    for i in range(1, self.value_matrix.shape[0] - 1):
        for j in range(1, self.value_matrix.shape[1] - 1):
            if self.value_matrix[i][j] == 0:
                temp = 0
                number_of_adds = 0

                for orientation in orientations:
                    if self.value_matrix[i + orientation[0]][j + orientation[1]] > 0:
                        temp += self.value_matrix[i + orientation[0]][j + orientation[1]]
                        number_of_adds += 1
                if number_of_adds != 0:
                    self.value_matrix[i][j] = int(temp / number_of_adds)
                else:
                    self.value_matrix[i][j] = temp
            # print(f"i: {i} j: {j} Vl: {self.value_matrix[i][j]}")

    for i in range(self.value_matrix.shape[0]):
        for j in range(self.value_matrix.shape[1]):
            if self.value_matrix[i][j] > 0:
                print(self.value_matrix[i][j])
                rects.append(((255, int(self.value_matrix[i][j]), 0)
                              , pygame.rect.Rect((i * self.tile_size, j * self.tile_size),
                                                 (self.tile_size, self.tile_size))))
            else:
                rects.append(((0, 0, 0), pygame.rect.Rect((i * self.tile_size, j * self.tile_size),
                                                          (self.tile_size, self.tile_size))))

    return rects