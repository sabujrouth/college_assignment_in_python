# Write a program which accepts a sequence of comma separated 4 digit binary numbers as
# its input and then check whether they are divisible by 5 or not
# Input Example : 0100,0011,1010,1001

numbers = input("Enter a sequence of comma separated 4 digit binary numbers: ")
numbers = numbers.split(",")

for number in numbers:
    decimal = int(number, 2)
    if decimal % 5 == 0:
        print(number, "is divisible by 5")
    else:
        print(number, "is not divisible by 5")