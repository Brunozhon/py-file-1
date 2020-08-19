# Do the imports for the required stuff

import numpy
import matplotlib.pyplot as plt
from scipy import stats

# Print the topic

print("Topic: Coumputer Scince")

# Make 10000 floats bettwen 0 and 5

x = numpy.random.uniform(0.0, 5.0, 250)

# Create a plot

plt.hist(x, 100)
plt.show()

print("Note: Chart shown may be diffrent due to random numbers (in 'numpy.random.uniform()').")
print("Random gernrated numbers are: " + x)

ages = [6, 8, 10, 16, 20, 38, 46, 50, 51, 52, 53, 54, 100, 102, 108]
mean = numpy.mean(ages)
print(mean)
print("Version 0.2 alpha. More updates comming soon.")
median = numpy.median(ages)

ages = [6, 8, 10, 10, 16, 20, 38, 46, 46, 50, 51, 52, 53, 54, 100, 100, 102, 108]
mode = stats.mode(ages)
