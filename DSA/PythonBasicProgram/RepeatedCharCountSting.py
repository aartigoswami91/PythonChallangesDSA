def count_repeated_char(s):
    arr = []
    res = ''
    count = 1
    for char in range(1,len(s)):
        if s[char] == s[char-1]:
            count +=1
            
        else:
            res = res + s[char-1]+ str(count)
            count = 1
    res += s[-1] + str(count)
    return res
        
print(count_repeated_char("abbcccdddd"))