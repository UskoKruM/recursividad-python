def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


number = 3
number2 = 5

print(f"El factorial de {number} es: {factorial(number)}")
print(f"El factorial de {number2} es: {factorial(number2)}")
