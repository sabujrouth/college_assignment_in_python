# Write a python code to display Fibonacci series till n numbers using recursion

print("Sabuj Routh")

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

n = int(input("Enter the value of n: "))

if n <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci series:")
    for i in range(n):
        print(fibonacci(i), end=" ")
