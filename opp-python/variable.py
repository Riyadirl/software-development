age = 24
interest_rate = 3.4
name = "Mahbub"
district = "comilla"
is_single = True

print(age)
print(district)
print(age + interest_rate)

print(type(age))

# Numeric types
age = 25  # int
pi = 3.14  # float
complex_num = 2 + 3j  # complex

# Sequence types
name = "John"  # str
fruits = ["apple", "banana", "cherry"]  # list
numbers = (1, 2, 3)  # tuple
range_example = range(5)  # range

# Mapping type
person = {"name": "John", "age": 25}  # dict

# Set types
unique_numbers = {1, 2, 3, 4}  # set
frozen_set_example = frozenset([1, 2, 3, 4])  # frozenset

# Boolean type
is_active = True  # bool

# Binary types
binary_data = b"Hello"  # bytes
bytearray_data = bytearray(5)  # bytearray
memoryview_data = memoryview(bytes(5))  # memoryview

# Displaying the variables
print("Numeric Types:")
print("Integer:", age)
print("Float:", pi)
print("Complex:", complex_num)

print("\nSequence Types:")
print("String:", name)
print("List:", fruits)
print("Tuple:", numbers)
print("Range:", list(range_example))

print("\nMapping Type:")
print("Dictionary:", person)

print("\nSet Types:")
print("Set:", unique_numbers)
print("Frozen Set:", frozen_set_example)

print("\nBoolean Type:")
print("Boolean:", is_active)

print("\nBinary Types:")
print("Bytes:", binary_data)
print("Bytearray:", bytearray_data)
print("Memoryview:", memoryview_data)
