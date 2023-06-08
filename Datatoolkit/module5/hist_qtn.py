import numpy as np
import matplotlib.pyplot as plt

list_1 = [48.49, 67.54, 57.47, 68.17, 51.18, 68.31, 50.33, 66.7, 45.62, 43.59, 53.64, 70.08, 47.69, 61.27, 44.14, 51.62, 48.72, 65.11]

plt.hist(list_1, bins = 4, range =[40, 80], edgecolor = 'white')

plt.show()