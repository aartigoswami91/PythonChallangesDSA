def most_frequency(s):
    st = s.split()
    dic = {}  
    count = 1
    
    for w in st:
        if w in dic:
            dic[w]+=1
            count +=1
        else:
            dic[w] = 1
            
    result = max(dic , key = dic.get)
        
    return result,dic[result]            

print(most_frequency("thisddddd is bad boy that is good"))
