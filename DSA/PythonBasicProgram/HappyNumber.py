def isHappy(n: int) -> bool:
    visited = set()
    num = n

    while num not in visited:
        visited.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))

    print(visited)
    return 1 in visited

print(isHappy(13))