import numpy as np
import random

m = np.zeros((10,20))
print(m.shape)
print(m.size)
for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if i== 0 or i == m.shape[0]-1 or j == m.shape[1]-1 or j == 0:
            m[i][j] = 4
        elif  i % 2 == 0 and j % 2 == 0:
            m[i][j] = 1
print(m)
for i in range(1, m.shape[0]-1):
    for j in range(1, m.shape[1]-1):
        if (i+j) % 2 == 1:
            temp = 0
            number_of_adds = 0
            orientations = ((1, 0), (0, 1), (-1, 0), (0, -1))
            for orientation in orientations:
                k=m[i+orientation[0]][j+orientation[1]]
                h=i+orientation[0]
                l=j+orientation[1]
                if m[i+orientation[0]][j+orientation[1]] != 4 and m[i+orientation[0]][j+orientation[1]] != 0:
                    temp += m[i+orientation[0]][j+orientation[1]]
                    number_of_adds += 1
            if number_of_adds != 0:
                m[i][j] = int(temp/number_of_adds)
            else:
                m[i][j] = temp
for i in range(1, m.shape[0] - 1):
    for j in range(1, m.shape[1] - 1):
        if m[i][j] == 0:
            temp = 0
            number_of_adds = 0
            orientations = ((1, 0), (0, 1), (-1, 0), (0, -1))
            for orientation in orientations:
                k = m[i + orientation[0]][j + orientation[1]]
                h = i + orientation[0]
                l = j + orientation[1]
                if m[i + orientation[0]][j + orientation[1]] != 4 and m[i + orientation[0]][
                    j + orientation[1]] != 0:
                    temp += m[i + orientation[0]][j + orientation[1]]
                    number_of_adds += 1
            if number_of_adds != 0:
                m[i][j] = int(temp / number_of_adds)
            else:
                m[i][j] = temp
print(f"Matrix: {m}")
