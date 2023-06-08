import numpy as np
import matplotlib.pyplot as plt

product_category = np.array(['Furniture', 'Technology', 'Office Supplies'])
sales = np.array ([4110451.90, 4744557.50, 3787492.52] )

plt.bar(product_category, sales, width=.4, align='center', edgecolor = 'Red', color = 'Green')

# ##for different color bar
# plt.bar(product_category, sales, width=.4, align='center', edgecolor = 'Red', color = ['green', 'blue', 'red'])

plt.title("Product Category Vs Sales", fontdict={'fontsize' :18, 'fontweight' : 0.7, 'color' : 'Blue'})
plt.xlabel("Product Category", fontdict={'fontsize' :10, 'fontweight' : 0.7, 'color' : 'Blue'})
plt.ylabel("Sales", fontdict={'fontsize' :10, 'fontweight' : 0.7, 'color' : 'Blue'})

ticks = np.arange(0, 6000000, 1000000)
yaxis_label = [f"{val//1000000}M" for val in ticks]

plt.yticks(ticks, yaxis_label)


plt.show()