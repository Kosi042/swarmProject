import numpy as np
import random


m = np.zeros((10,20))
print(m.shape)
print(m.size)
for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if i== 0 or i == m.shape[0]-1 or j == m.shape[1]-1 or j == 0:
            m[i][j] = 1
        elif i % 5 == 3 and j % 5 == 3:
            m[i][j] = 7
            # m[i][j] = random.randint(1, 25) * 10
print(m)

