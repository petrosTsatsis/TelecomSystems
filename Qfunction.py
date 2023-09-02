# import libraries to use
import numpy as np
import matplotlib.pyplot as plt
from scipy import special
from scipy.optimize import root_scalar


# Qfunction
def Qfunction(x):
    return 0.5 * special.erfc(x / np.sqrt(2))

# Values from 2 to 7 for the x-axis using 1000 points
x = np.linspace(2, 7, num =1000)
y = Qfunction(x)

# Function 1
Q1 = np.exp(-(x**2)/2)

# Function 2
Q2 = 1/4 * np.exp(-(x**2)) + 1/4 * np.exp(-(x**2)/2)

# Function 3
Q3 = 1/12 * np.exp(-(x**2)/2) + 1/4 * np.exp(-(2*x**2)/3)

# First close all plots
plt.close('all')

# Figure 1
plt.figure(1)
plt.title('Compare Q and Q1 functions')

# Convert y-axis to Logarithmic scale
plt.yscale("log")
plt.plot(x, y, label='Qfunction')
plt.plot(x, Q1, linestyle='dashed', linewidth=3, label='Q1 function')
# Labels
plt.xlabel('x')
plt.ylabel('Q(x)')
plt.legend()

# Figure 2
plt.figure(2)
plt.title('Compare Q and Q2 functions')

# Convert y-axis to Logarithmic scale
plt.yscale("log")
plt.plot(x, y, label='Qfunction')
plt.plot(x, Q2, linestyle='dashed', linewidth = 3, label='Q2 function')
# labels
plt.xlabel('x')
plt.ylabel('Q(x)')
plt.legend()

# Figure 3
plt.figure(3)
plt.title('Compare Q and Q3 functions')

# Convert y-axis to Logarithmic scale
plt.yscale("log")
plt.plot(x, y, label='Qfunction')
plt.plot(x, Q3, linestyle='dashed', linewidth=3, label='Q3 function')
# Labels
plt.xlabel('x')
plt.ylabel('Q(x)')
plt.legend()

plt.show()

# Using Q1 function to find the errors
e1 = abs(Q1-y)/abs(y)

# Trapz for the calculation of the integration
print('e1 = %f' % np.trapz(e1, x))

# Using Q2 function to find the errors
e2 = abs(Q2-y)/abs(y)

# Trapz for the calculation of the integration
print('e2 = %f' % np.trapz(e2, x))

# Using Q3 Function to find the errors
e3 = abs(Q3-y)/abs(y)

# Trapz for the calculation of the integration
print('e3 = %f' % np.trapz(e3, x) + "\n")

# Inverse of Qfunction using numerical optimization
def Qinv(y):

    # Function that finds the root
    def root_function(x):
        return Qfunction(x) - y

    # Use root_scalar to find the root
    result = root_scalar(root_function, bracket=[-10, 10])
    if result.converged:
        return result.root
    else:
        return None

# Y values and points
y_values = np.linspace(0.01, 0.10, num=10)

# Calculate and display the inverse of Qfunction using numerical optimization
total_accuracy = 0
for y in y_values:
    x_inverse = Qinv(y)
    if x_inverse is not None:
        print(f"For y = {y:.2f}, Inverse x = {x_inverse:.2f}")
    else:
        print(f"For y = {y:.2f}, No convergence")



