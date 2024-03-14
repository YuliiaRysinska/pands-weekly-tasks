# Prog displayed a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

import matplotlib.pyplot as plt

import numpy as np

# Generate 1000 values from a normal distribution with mean 5 and standard deviation 2
mean = 5
std_dev = 2
data = np.random.normal(mean, std_dev, 1000)

# Define the function h(x) = x^3
def h(x):
    return x ** 3

# Generate x values for the function h(x)
x_values = np.linspace(0, 10, 100)

# Plot the histogram of the normal distribution
plt.hist(data, bins=30, density=True, alpha=0.5, color='b', label='Normal Distribution')

# Plot the function h(x) = x^3
plt.plot(x_values, h(x_values), 'r-', label='$h(x) = x^3$')

# Add labels and legend
plt.xlabel('Values')
plt.ylabel('Probability')
plt.title('Histogram of Normal Distribution and Function $h(x) = x^3$')
plt.legend()

# Display the plot
plt.show()
