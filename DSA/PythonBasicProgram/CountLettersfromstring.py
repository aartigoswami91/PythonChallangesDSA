def count_letters(s):
    hashMap = {}
    for char in s:
        if char in hashMap:
             hashMap[char] += 1
        else:
            hashMap[char] = 1
    return hashMap
            
            
        
print(count_letters("apple"))