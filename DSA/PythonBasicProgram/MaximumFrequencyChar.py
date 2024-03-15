#maximum Frequency character
def maxinum_frequency(s):
    hash_key = {}
    res = 0
    for i in range(len(s)):
        if s[i] in hash_key:
            hash_key[s[i]] += 1
        else:
            hash_key[s[i]] = 1
    res = max(hash_key,key = hash_key.get)
    return res
    
print(maxinum_frequency("missisagas"))   