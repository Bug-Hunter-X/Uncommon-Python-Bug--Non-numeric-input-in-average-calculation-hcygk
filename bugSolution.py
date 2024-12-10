def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

#Example usage:
valid_numbers = [10,20,30,40,50]
print(calculate_average(valid_numbers)) #Output: 30.0
invalid_numbers = [10, 'a', 30, 40, 50]
print(calculate_average(invalid_numbers)) #Output: 30.0
empty_numbers = []
print(calculate_average(empty_numbers)) #Output: 0