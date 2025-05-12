def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

var1 = int(input('Enter a number : '))
print(f'Factorial of {var1} is: {factorial(var1)}.')
