def patterns_rombus(n):
    for a in range(1,n+1):
        print(' ' * (n-a) + '*' * (2*a-1))
    for b in range(n-1,0,-1):
        print(' ' *(n-b) + '*' * (2*b-1))
        
print(patterns_rombus(6))