fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Printing numbers from 0 to 4
for i in range(5):
    print(i)


word = "Python"
for char in word:
    print(char)


# Printing numbers from 1 to 10 with a step of 2
for i in range(1, 11, 2):
    print(i)


for i in range(5):
    print(i)
else:
    print("Loop completed!")



# Stop the loop when the number is 3
for i in range(5):
    if i == 3:
        break
    print(i)


person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
