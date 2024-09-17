import colorsys
import numpy as np
test_color = colorsys.hsv_to_rgb(120, 100, 100)
print(test_color)
t2 = colorsys.hsv_to_rgb(60/360, 1., 1. )
print(np.array(t2)*255)