def divide_and_conquer_sort(sequence):
    """Implement a divide-and-conquer sorting algorithm."""
    if len(sequence) > 1:
        midpoint = len(sequence) // 2
        left_half = sequence[:midpoint]
        right_half = sequence[midpoint:]

        # Recursively sort both halves
        divide_and_conquer_sort(left_half)
        divide_and_conquer_sort(right_half)

        left_index = right_index = merged_index = 0

        # Merge the sorted halves
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                sequence[merged_index] = left_half[left_index]
                left_index += 1
            else:
                sequence[merged_index] = right_half[right_index]
                right_index += 1
            merged_index += 1

        # Handle any remaining elements
        while left_index < len(left_half):
            sequence[merged_index] = left_half[left_index]
            left_index += 1
            merged_index += 1

        while right_index < len(right_half):
            sequence[merged_index] = right_half[right_index]
            right_index += 1
            merged_index += 1

# Test the sorting algorithm
unsorted_data = [5, 2, 4, 7, 1, 3, 2, 6]
print("Initial sequence:", unsorted_data)

divide_and_conquer_sort(unsorted_data)

print("Sorted sequence:", unsorted_data)


"""OUTPUT:
Initial sequence: [5, 2, 4, 7, 1, 3, 2, 6]
Sorted sequence: [1, 2, 2, 3, 4, 5, 6, 7]"""