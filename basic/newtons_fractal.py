import numpy as np
import matplotlib.pyplot as plt

def newton(z):
    return z - (z**3 - 1) / (3*z**2)

def newton_fractal(f, df, roots, bounds, resolution):
    x_min, x_max, y_min, y_max = bounds
    x_vals = np.linspace(x_min, x_max, resolution)
    y_vals = np.linspace(y_min, y_max, resolution)
    fractal = np.zeros((resolution, resolution))

    for i, x in enumerate(x_vals):
        for j, y in enumerate(y_vals):
            z = x + 1j*y
            for n in range(100):
                z = f(z)
                if abs(z - roots[0]) < 1e-6:
                    fractal[j, i] = 1
                    break
                elif abs(z - roots[1]) < 1e-6:
                    fractal[j, i] = 2
                    break
                elif abs(z - roots[2]) < 1e-6:
                    fractal[j, i] = 3
                    break
    return fractal

roots = [1, -0.5 + 1j*np.sqrt(3)/2, -0.5 - 1j*np.sqrt(3)/2]
bounds = (-1.5, 1.5, -1.5, 1.5)
resolution = 1000

fractal = newton_fractal(newton, lambda z: 1 - z**2, roots, bounds, resolution)

plt.imshow(fractal, cmap='jet')
plt.axis('off')
plt.show()