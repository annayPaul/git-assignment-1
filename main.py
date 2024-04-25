n = int(input())

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)

# number is the offset, starts at 0, eg: 0th fibonacci is 1, 1st fibonacci is 1, etc
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number-1) + fibonacci(number)

print(f'Factorial of the number {n} is {factorial(n)}')
print(f'The {n}th Fibonacci number is {factorial(n)}')

# Comment 1
# Comment 2