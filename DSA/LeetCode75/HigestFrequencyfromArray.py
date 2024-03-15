def bucket_sort(num,k):
    # create buccket for num length
    # collect hash Map repeated count {1:3,2:2,3:1,4:5}
    # bucket array m dalna h index match karke
    #lenth k=2
    
    count={}
    bucket = [[] for s in range(len(num)+1)]
    
    for i in num:
        count[i] = 1 + count.get(i,0)
        
    for s,v in count.items():
        bucket[v].append(s)
        
        
    arr = []    
    for n in range(len(bucket)-1,0,-1):
        for i in bucket[n]:
            arr.append(i)
            if len(arr) == k:
                return arr
        
        


num = [1,1,1,2,2,3]
print(bucket_sort(num,2))