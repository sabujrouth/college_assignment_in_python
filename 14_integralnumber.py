# With a given integral number n, write a program to generate a dictionary that contains (i,
# i*i) such that is an integral number between 1 and n (both included). and then the
# program should print the dictionary
# Input Example : 5
n = int(input("Enter an integer: "))

squares = {}
for i in range(1, n+1):
    squares[i] = i*i

print(squares)