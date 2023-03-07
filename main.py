# function testing whether or not a particular value is in the mandelbrot set

def is_in_mandelbrot(c, max_iterations=100):
    z = 0
    for i in range(max_iterations):
        z = z*z + c
        if abs(z) > 2:
            return False
    return True


print(is_in_mandelbrot(0.11 + 0j))
