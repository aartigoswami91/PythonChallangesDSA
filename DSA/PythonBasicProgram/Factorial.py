def factorial_number(n):
    if n == 0:
        return 1
    else:
        return n * factorial_number(n-1)
    #factorial need to call self function

print(factorial_number(3))