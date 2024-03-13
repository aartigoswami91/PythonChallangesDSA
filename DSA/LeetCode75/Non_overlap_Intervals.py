#Non Overlapping Intervala
def non_overlaping_Interval(intervals):
    intervals.sort()
    res = 0
    preEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= preEnd :
            preEnd = end
        else:
            res += 1
            preEnd = min(preEnd, end)
    return res
            
            
        

intervals = [(1,2),(2,3),(3,4),(1,3)]
print(non_overlaping_Interval(intervals))