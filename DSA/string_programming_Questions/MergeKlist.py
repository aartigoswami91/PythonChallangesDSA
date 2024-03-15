def mergeKLists(operations):
    count = 0

    for i in range(len(operations)):       
            if '-'in operations[i]:
                count -= 1
            if '+'in operations[i]:
                count += 1
    return count
    
operations = ["X++","++X","--X","X--", "X++"]
print(mergeKLists(operations))