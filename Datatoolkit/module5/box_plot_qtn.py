import numpy as np
import matplotlib.pyplot as plt

list_1 = [48.49, 67.54, 57.47, 68.17, 51.18, 68.31, 50.33, 66.7, 45.62, 43.59, 53.64, 70.08, 47.69, 61.27, 44.14, 51.62, 48.72, 65.11]
list_arr = np.array(list_1)

Q1 = np.percentile(list_arr, 25)
Q2 = np.percentile(list_arr, 75) 

print(f"[{Q1} {Q2}]")
plt.boxplot([list_1])
plt.show()
# np.percentile

#### Reference for box plot : https://www.geeksforgeeks.org/box-plot/