# Taking input from the user
name = input("Enter your name: ")  # Input is a string
age = int(input("Enter your age: "))  # Typecasting input to an integer
height = float(input("Enter your height in meters: "))  # Typecasting input to a float

# Output using print
print("\nOutput:")
print(f"Hello, {name}!")  # Using an f-string for formatted output
print(f"You are {age} years old.")
print(f"Your height is {height:.2f} meters.")  # Formatting float to 2 decimal places

# Typecasting examples
age_next_year = age + 1  # Adding 1 to integer age
print(f"Next year, you will be {age_next_year} years old.")

height_str = str(height)  # Converting float to string
print("Your height as a string:", height_str)
