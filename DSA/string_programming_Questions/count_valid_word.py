class CountValidWord:
    def countValidWords(self, sentence: str) -> int:
        '''
        def fn(word): 
            """Return true if word is valid."""
            seen = False 
            for i, ch in enumerate(word): 
                if ch.isdigit() or ch in "!.," and i != len(word)-1: return False
                elif ch == '-': 
                    if seen or i == 0 or i == len(word)-1 or not word[i+1].isalpha(): return False 
                    seen = True 
            return True 
        
        return sum(fn(word) for word in sentence.split())
        '''

     
        sentence_list = sentence.split()
        #1.Split sentances
        print(sentence_list)
        count = 0
        for i, word in enumerate(sentence_list):
            valid = True
            hyphen_count = 0  
            for j, letter in enumerate(word):
                print(j,letter)
                if letter.isdigit():
                    valid = False 
                    break
                if letter in ("!",".",",") and j != len(word)-1:
                    valid = False 
                    break
                if (letter == "-" and (j == len(word)-1 or j == 0)) or (letter == "-" and (not word[j-1].isalpha() or not word[j+1].isalpha())):
                    valid = False 
                    break
                if letter == "-":
                    hyphen_count +=1
                    if hyphen_count >1:
                        valid = False 
                        break
            if valid:
                count +=1
        return count

    
sol = CountValidWord()
sentence = "-cat and  8dog"
print(sol.countValidWords(sentence))