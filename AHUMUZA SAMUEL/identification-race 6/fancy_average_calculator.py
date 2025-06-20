def calculate_average(numbers):
    sum = 0
    for number in numbers:
     sum += number
    average = sum / len(numbers)
    return average
numbers = [1, 55, 44, 14, 10]
average = calculate_average(numbers)
print("Average:", average)