

def binaryfunction(arr,value):
    left = 0
    right = len(arr)
    mid = 1 + (right - left)//2

    while left <= right:
        if arr[mid] == value:
            return mid
        # right pointer
        elif arr[mid] > value:
            right = mid - 1
        #left pointer
        else:
            left = mid + 1

    return -1


    
arr =[2, 4, 6, 7, 8, 9, 10]
value = 5
print(binaryfunction(arr, value))
