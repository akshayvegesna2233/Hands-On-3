def calculate_quadratic_plus_one(count):
    return count * count + 1

user_input = int(input("Please enter a number for processing: "))
result = calculate_quadratic_plus_one(user_input)
print(f"The computed result is: {result}")

"""OUTPUT:
Please enter a number for processing: 5
The computed result is: 26"""