import time
import numpy as np
import matplotlib.pyplot as plt

def nested_counter(size):
    """Perform nested iterations and return a count."""
    count = 1
    for outer in range(1, size + 1):
        for inner in range(1, size + 1):
            count += 1
    return count

input_range = np.arange(1, 101)
time_measurements = np.zeros_like(input_range, dtype=float)

for index, size in enumerate(input_range):
    begin = time.time()
    nested_counter(size)
    time_measurements[index] = time.time() - begin

# Approximate the data with a quadratic function
quadratic_params = np.polyfit(input_range, time_measurements, 2)
quadratic_approximation = np.polyval(quadratic_params, input_range)

# Establish an upper limit (O-notation) using a cubic function
cubic_params = np.polyfit(input_range, time_measurements, 3)
cubic_curve = np.polyval(cubic_params, input_range)
cubic_function = np.poly1d(cubic_params)

# Define a lower limit (Ω-notation) using a linear function
linear_params = np.polyfit(input_range, time_measurements, 1)
linear_curve = np.polyval(linear_params, input_range)
linear_function = np.poly1d(linear_params)

# Display the mathematical representations
print("Quadratic Approximation:", np.poly1d(quadratic_params))
print("Upper Limit (O-notation):", cubic_function)
print("Lower Limit (Ω-notation):", linear_function)

# Visualize the results
plt.figure(figsize=(10, 6))
plt.plot(input_range, time_measurements, 'bo', label='Observed Data')
plt.plot(input_range, quadratic_approximation, 'r-', linewidth=2, label='Quadratic Fit')
plt.plot(input_range, cubic_curve, 'g--', linewidth=2, label='Upper Limit')
plt.plot(input_range, linear_curve, 'm--', linewidth=2, label='Lower Limit')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Algorithm Complexity Analysis')
plt.legend()
plt.grid(True)
plt.show()


"""OUTPUT:
Quadratic Approximation:            2
5.396e-08 x + 2.012e-07 x + 6.747e-06
Upper Limit (O-notation):            3             2
1.905e-09 x - 2.346e-07 x + 1.192e-05 x - 9.431e-05 
Lower Limit (Ω-notation):  
5.651e-06 x - 8.589e-05"""
