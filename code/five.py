# Function with additional operation in inner loop
def enhanced_nested_counter(size):
    primary_count = 1
    for outer in range(1, size + 1):
        for inner in range(1, size + 1):
            primary_count += 1
            secondary_sum = outer + inner  # Additional operation
    return primary_count

# Function without additional operation in inner loop
def basic_nested_counter(size):
    total = 1
    for outer in range(1, size + 1):
        for inner in range(1, size + 1):
            total += 1
    return total

# Test both functions with a sample input
sample_size = 3
output_enhanced = enhanced_nested_counter(sample_size)
output_basic = basic_nested_counter(sample_size)

# Display the results
print(f"Enhanced nested counter result: {output_enhanced}")
print(f"Basic nested counter result: {output_basic}")

# Analysis prompt
print("\nQuestion: Does the additional operation in the enhanced function affect the final count?")
print("Compare the outputs to determine if there's any difference in the results.")


"""OUTPUT:
Enhanced nested counter result: 10
Basic nested counter result: 10"""