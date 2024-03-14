def is_Palidrom(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] == s[right]:
            left = left +1
            right = right -1
        else:
            return False
    return True
        
        
print(is_Palidrom("kalaka")) 