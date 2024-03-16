def patterns_pyramid(n):
    for a in range(1,n+1):
        print(' ' * (n-a) + '*' * (2*a-1))
    
print(patterns_pyramid(5))