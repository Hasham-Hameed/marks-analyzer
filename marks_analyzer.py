numbers = []

for i in range(5):
    number = int(input("Enter your marks:"))
    numbers.append(number)

def calculate_total(numbers):
    total = 0
    for mark in numbers:
        total = total + mark
    return total
result1 = calculate_total(numbers)

def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
result2 = find_largest(numbers)

print(f"List:{numbers}")
print(f"Total:{result1}")
print(f"Largest number:{result2}")