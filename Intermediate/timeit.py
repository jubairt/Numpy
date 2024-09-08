# Define the functions
import numpy as np

large_list = np.random.randint(0, 100, size=1000000)

def sum_with_loop():
    total = 0
    for number in large_list:
        total += number
    return total

def sum_with_builtin():
    return sum(large_list)

# Measure execution time
%timeit sum_with_loop()
%timeit sum_with_builtin()


# Timing for sum_with_loop()
9.78 ms ± 0.12 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)

# Timing for sum_with_builtin()
2.15 ms ± 0.05 ms per loop (mean ± std. dev. of 7 runs, 1000 loops each)


# Explanation
# 9.78 ms ± 0.12 ms per loop: This means that on average, the sum_with_loop() function takes approximately 9.78 milliseconds to execute per loop. The standard deviation is 0.12 milliseconds, which indicates variability in the timing measurements.

# 2.15 ms ± 0.05 ms per loop: This indicates that sum_with_builtin() takes approximately 2.15 milliseconds on average per loop, with a standard deviation of 0.05 milliseconds.

# Interpretation
# Performance Difference: You will typically observe that sum_with_builtin() is significantly faster than sum_with_loop(). This is because the built-in sum() function is optimized in C, making it more efficient for summing large lists compared to a Python loop.

# Standard Deviation: The standard deviation values show how much the execution times vary between different runs. A lower standard deviation indicates more consistent performance.

# Why This Happens
# sum_with_loop(): This function iterates through each element in the list using a Python loop and adds it to a total. This approach is slower because Python loops are less efficient for large-scale operations compared to optimized C code.

# sum_with_builtin(): The sum() function is implemented in C and highly optimized for performance. It benefits from lower-level optimizations that Python loops do not.