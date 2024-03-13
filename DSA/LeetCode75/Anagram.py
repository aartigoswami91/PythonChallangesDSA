#Anagram
def Anagram_check(s1,s2):
    count1 = {}
    count2 = {}
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        count1[s[i]] = 1 + count1.get(s1[i],0)
        count2[s[i]] = 1 + count2.get(s2[i],0)
    for c in count2:
        count2[c] ==count1.get(c,0)
        return True
    return False


s1 = "anagram"
s2 ="ngaramav"
print(Anagram_check(s1,s2))        