import numpy as np

m = np.random.randint( -10, 10, size=(10+2,14+2))
n = np.zeros((10,14))
m = m*50
print(m)
print("Teil matrix")
for i in range(m.shape[0]-4):
    for j in range(m.shape[1]-4):
        print(f"i: {i}, j: {j}")
        print(m[i:i+5, j:j+5])
        scalar = int((np.array([1, 1, 1, 1, 1]).T @ (m[i:i + 5, j:j + 5] @ np.array([1, 1, 1, 1, 1]))) / 25)
        print(f"scalar: {scalar}")
        n[i, j] = scalar
print(m)
print(n)