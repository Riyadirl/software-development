# Taking input
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))

# if-elif-else example
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

# Nested if example
if age >= 18:
    if age >= 60:
        print("You are a senior citizen.")
    else:
        print("You are an adult and not yet a senior citizen.")
else:
    print("You are not an adult yet.")

# Grade calculation using if-elif-else
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# Short-hand if example
if marks > 50:
    print("You passed the exam.")

# Short-hand if-else example
voting_status = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(voting_status)
