import time
import numpy as np
import matplotlib.pyplot as plt

def baseline_nested_loop(size):
    """Perform a simple nested loop operation."""
    result = 1
    for outer in range(1, size + 1):
        for inner in range(1, size + 1):
            result += 1
    return result

def enhanced_nested_loop(size):
    """Perform a nested loop operation with an additional calculation."""
    primary_count = 1
    secondary_count = 1
    for outer in range(1, size + 1):
        for inner in range(1, size + 1):
            primary_count += 1
            secondary_count = outer + inner
    return primary_count

# Define range of input sizes to test
test_sizes = np.arange(1, 10)
baseline_timings = np.zeros_like(test_sizes, dtype=float)
enhanced_timings = np.zeros_like(test_sizes, dtype=float)

# Measure execution times for both functions
for index, size in enumerate(test_sizes):
    start = time.time()
    baseline_nested_loop(size)
    baseline_timings[index] = time.time() - start

    start = time.time()
    enhanced_nested_loop(size)
    enhanced_timings[index] = time.time() - start

    print(f'Size {size}: Baseline = {baseline_timings[index]:.6f}s, Enhanced = {enhanced_timings[index]:.6f}s')

# Visualize the results
plt.figure(figsize=(10, 6))
plt.plot(test_sizes, baseline_timings, 'bo-', label='Baseline Function')
plt.plot(test_sizes, enhanced_timings, 'go-', label='Enhanced Function')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Performance Comparison: Baseline vs Enhanced Nested Loops')
plt.legend()
plt.grid(True)
plt.show()

# Analysis prompt
print("\nQuestion: Does the enhanced function significantly increase execution time compared to the baseline?")
print("Examine the plotted results and printed timing data to draw your conclusion.")

"""OUTPUT:
Size 1: Baseline = 0.000000s, Enhanced = 0.000000s
Size 2: Baseline = 0.000000s, Enhanced = 0.000000s
Size 3: Baseline = 0.000000s, Enhanced = 0.000000s
Size 4: Baseline = 0.000000s, Enhanced = 0.000000s
Size 5: Baseline = 0.000000s, Enhanced = 0.000000s
Size 6: Baseline = 0.000000s, Enhanced = 0.000000s
Size 7: Baseline = 0.000000s, Enhanced = 0.000000s
Size 8: Baseline = 0.000000s, Enhanced = 0.000000s
Size 9: Baseline = 0.000000s, Enhanced = 0.000000s"""