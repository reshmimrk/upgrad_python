import numpy as np
import matplotlib.pyplot as plt 
## 1
# y = np.random.randint(1,100, 50)
# # plt.plot(y, 'ro') # ‘ro’ represents color (r) and marker (o)
# plt.plot(y, 'red', marker = 'o')
# plt.show()

##2
import numpy as np
import matplotlib.pyplot as plt

months = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
sales = np.array([241268.56, 184837.36, 263100.77, 242771.86, 288401.05, 401814.06, 258705.68, 456619.94, 481157.24, 422766.63, 555279.03, 503143.69])

plt.plot(months, sales)

# Adding and formatting title
plt.title("Sales across 2015\n", fontdict={'fontsize': 20, 'fontweight' : 5, 'color' : 'Green'})

# Labeling Axes
plt.xlabel("Months", fontdict={'fontsize': 12, 'fontweight' : 5, 'color' : 'Brown'})
plt.ylabel("Sales", fontdict={'fontsize': 12, 'fontweight' : 5, 'color' : 'Brown'} )

ticks = np.arange(0, 600000, 50000)
labels = ["{}K".format(i//1000) for i in ticks]
plt.yticks(ticks, labels)

plt.xticks(rotation=90)

for xy in zip(months, sales):
    plt.annotate(text = "{}K".format(xy[1]//1000), xy = xy,  textcoords='data')

plt.show()