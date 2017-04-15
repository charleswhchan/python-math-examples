import matplotlib.pyplot as plt
import numpy as np

filename = "..."

# Assumes the file is a CSV file with 2 columns, fields separated by ','

data = np.genfromtxt(filename, dtype='object', delimiter=',')

identifier = data[:, 0]
value = data[:, 1]

x_coordinates = np.arange(len(identifier))

plt.bar(x_coordinates, value, width=1.0)

plt.title('title')
plt.ylabel('value')
plt.yscale('log')  # use log scale

plt.show()
# plt.savefig( ... )

