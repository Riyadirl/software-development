# Input values
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponentiation = num1**num2

# Comparison operations
is_equal = num1 == num2
is_greater = num1 > num2
is_smaller = num1 < num2

# Logical operation example
logical_and = (num1 > 0) and (num2 > 0)

# Output results
print("\nArithmetic Operations:")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division:.2f}")
print(f"Floor Division: {num1} // {num2} = {floor_division}")
print(f"Modulus: {num1} % {num2} = {modulus}")
print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")

print("\nComparison Operations:")
print(f"{num1} == {num2}: {is_equal}")
print(f"{num1} > {num2}: {is_greater}")
print(f"{num1} < {num2}: {is_smaller}")

print("\nLogical Operation:")
print(f"Are both numbers positive? {logical_and}")
