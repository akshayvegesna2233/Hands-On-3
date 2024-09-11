import time
import numpy as np
import matplotlib.pyplot as plt

def nested_loop_operation(size):
    """Perform a nested loop operation and return the result."""
    result = 1
    for outer in range(1, size + 1):
        for inner in range(1, size + 1):
            result += 1
    return result

# Generate a range of input sizes
input_sizes = np.arange(1, 101)
timing_results = np.zeros_like(input_sizes, dtype=float)

# Measure execution time for each input size
for index, size in enumerate(input_sizes):
    start = time.time()
    nested_loop_operation(size)
    timing_results[index] = time.time() - start

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, timing_results, 'go', label='Measured Times')

# Fit a quadratic curve to the data
quadratic_fit = np.polyfit(input_sizes, timing_results, 2)
fitted_values = np.polyval(quadratic_fit, input_sizes)

plt.plot(input_sizes, fitted_values, 'r-', linewidth=2, label='Quadratic Fit')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Performance Analysis of Nested Loop Operation')
plt.legend()
plt.grid(True)
plt.show()