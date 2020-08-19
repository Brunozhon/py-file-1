# Do the imports for the required stuff

import numpy
import matplotlib.pyplot as plt

# Print the topic

print("Topic: Coumputer Scince")

# Make 10000 floats bettwen 0 and 5

x = numpy.random.uniform(0.0, 5.0, 250)

# Create a plot

plt.hist(x, 100)
plt.show()

print("Note: Chart shown may be diffrent due to random numbers (in 'numpy.random.uniform()').")
print("Random gernrated numbers are: " + x)

print("Version: 0.1 alpha. More updates comming soon")
