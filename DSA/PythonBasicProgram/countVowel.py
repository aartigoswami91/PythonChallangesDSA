def count_vowels(s):
    v = 'aeiou'
    count = 0
    st = s.lower()
    for char in st:
        if char in v:
            count +=1
    return count
        
print(count_vowels("aartiGoswami"))