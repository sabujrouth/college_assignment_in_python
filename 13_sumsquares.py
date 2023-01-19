print("Sabuj Routh")
def sum_of_squares(numbers):
    total = 0
    for number in numbers:
        total += number ** 2
    return total

numbers = [1, 2, 3, 4, 5, 6]
result = sum_of_squares(numbers)
print(result)