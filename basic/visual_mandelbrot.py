import numpy as np
import matplotlib.pyplot as plt


# Define the function to generate the Mandelbrot set
def mandelbrot_set(xmin, xmax, ymin, ymax, nx, ny, max_iter):
    # Create arrays of x and y values
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymin, ymax, ny)

    # Create a grid of complex numbers from the x and y values
    c = x[:, np.newaxis] + 1j * y[np.newaxis, :]

    # Create an array to store the iteration counts for each point
    iterations = np.zeros_like(c, dtype=int)

    # Initialize the values of z to 0
    z = np.zeros_like(c)

    # Iterate the function z = z^2 + c up to max_iter times
    for i in range(max_iter):
        z = z ** 2 + c
        # Update the iteration count for points where |z| > 2
        mask = np.abs(z) > 2
        iterations[mask] = i
        z[mask] = np.nan

    # Return the iteration counts
    return iterations


# Generate the Mandelbrot set and plot it
xmin, xmax = -2, 1
ymin, ymax = -1.5, 1.5
nx, ny = 1000, 1000
max_iter = 100
iterations = mandelbrot_set(xmin, xmax, ymin, ymax, nx, ny, max_iter)
plt.imshow(iterations.T, cmap='hot', extent=(xmin, xmax, ymin, ymax))
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.show()
