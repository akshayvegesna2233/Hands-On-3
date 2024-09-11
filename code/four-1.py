import time
import numpy as np
import matplotlib.pyplot as plt

def double_loop_counter(size):
    """Perform a nested loop operation and return the count."""
    total = 1
    for outer in range(1, size + 1):
        for inner in range(1, size + 1):
            total += 1
    return total

input_sizes = np.arange(1, 101)
runtime_data = np.zeros_like(input_sizes, dtype=float)

for index, size in enumerate(input_sizes):
    begin = time.time()
    double_loop_counter(size)
    runtime_data[index] = time.time() - begin

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, runtime_data, 'bo', label='Measured Points')
curve_params = np.polyfit(input_sizes, runtime_data, 2)
estimated_curve = np.polyval(curve_params, input_sizes)
plt.plot(input_sizes, estimated_curve, 'r-', linewidth=2, label='Estimated Trend')

# Identify where actual runtime exceeds the estimated trend
divergence_point = np.argmax(runtime_data > estimated_curve)

# Display the results
threshold_size = input_sizes[divergence_point]
runtime_at_threshold = runtime_data[divergence_point]

print(f"Estimated threshold size: {threshold_size}")
print(f"Runtime at threshold: {runtime_at_threshold:.6f} seconds")

# Highlight the threshold point on the graph
plt.axvline(x=threshold_size, color='g', linestyle='--', label='Estimated Threshold')

plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Algorithm Performance Analysis')
plt.legend()
plt.grid(True)
plt.show()


"""OUTPUT:
Estimated threshold size: 29
Runtime at threshold: 0.000997 seconds
"""