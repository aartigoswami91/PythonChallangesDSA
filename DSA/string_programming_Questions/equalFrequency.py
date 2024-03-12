from collections import Counter
'sReturn true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.'

class EqualFrequency:
    def equalFrequency(self, s: str) -> bool:
        arr = list(s)
        for i in range(len(arr)):
            hashmap = {}
            temp = Counter(arr[0:i]+arr[i+1:])
            for k in temp:
                if temp[k] not in hashmap:
                    hashmap[temp[k]] = [k]
                else:
                    hashmap[temp[k]].append(k)
            maxx = max(hashmap)
            minn = min(hashmap)
            if maxx == minn:
                return True
        return False

eq = EqualFrequency()
s1 = 'abccd'
s2 = 'abcdccdd'

print(eq.equalFrequency(s1))
print(eq.equalFrequency(s2))
