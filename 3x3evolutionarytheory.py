#Have to install jupyter extension to graph it
#This is the logic for the python code


# Import Libraries:

# import numpy as np: NumPy is used for numerical operations in Python, and it is imported with the alias np.
# from scipy.integrate import odeint: The odeint function from SciPy is used to solve systems of ordinary differential equations (ODEs).
# import matplotlib.pyplot as plt: Matplotlib is a plotting library in Python, and it is imported with the alias plt for creating plots.
# Define ODE Function (dx):

# dx(x, t, A): This function represents the system of ODEs. It takes the current state x, time t, and matrix A as parameters.
# Calculate f and phi:

# f = np.dot(A, x): Matrix-vector product of A and x to calculate f.
# phi = np.dot(f, x): Inner product of f and x to calculate phi.

# Import necessary libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the function dx that represents the system of ordinary differential equations (ODEs)
def dx(x, t, A):
    # Calculate f, which is the matrix-vector product of A and x
    f = np.dot(A, x)
    # Calculate phi, which is the inner product of f and x
    phi = np.dot(f, x)
    # Return the derivative of x with respect to time
    return x * (f - phi)

# Create a time array from 0 to 10 with 10 points
t = np.linspace(0, 10, 10)

# Define the matrix A that represents the coefficients in the ODEs
# The matrix A is a 3x3 matrix with specific values (in this case, a simple example)
A = np.array([[0, 1, -1], [-1, 0, 1], [1, -1, 0]])

# Solve the system of ODEs using the odeint function
# Initial conditions are given by y0=[1/2, 1/6, 1/8]
xs = odeint(func=dx, y0=[1/2, 1/6, 1/8], t=t, args=(A,))

# Plot the solutions over time
plt.plot(xs)
plt.show()

