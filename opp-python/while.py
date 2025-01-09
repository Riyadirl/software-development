# Keep asking for a positive number
num = -1
while num <= 0:
    num = int(input("Enter a positive number: "))
print(f"You entered: {num}")


# Print numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment the count to avoid an infinite loop
