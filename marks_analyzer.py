numbers = []

for i in range(5):
    mark = int(input("Enter your marks(out of 100): "))
    numbers.append(mark)

def calculate_total(numbers):
    total = 0
    for marks in numbers:
        total += marks
    return total
calculated_total = calculate_total(numbers)

def calculate_average(calculated_total):
    average = calculated_total / 5
    return average
calculated_average = calculate_average(calculated_total)

def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
found_largest = find_largest(numbers)

def count_passed(numbers):
    count = 0
    for number in numbers:
        if number >= 50:
            count += 1
    return count
counted_subjects = count_passed(numbers)

print(f"The numbers you obtained are: {numbers}")
print(f"The total obtained marks are: {calculated_total}")
print(f"The average of your marks is: {calculated_average:.2f}")
print(f"The maximum marks you have obtained in a subject are: {found_largest}")
print(f"The number of subjects in which you have passed are: {counted_subjects}")