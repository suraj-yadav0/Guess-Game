list = [1,2,4,6,8,9,11,12,15,22,23,25,89]



def binary_search(list, target):
    st = 0
    end = len(list) - 1
    
    while st <= end:
        mid = (st + end) // 2
        
        if(list[mid] == target):
            return mid
        elif(list[mid] < target):
            st = mid + 1
        else:
            end = mid - 1
            
    return None


print(binary_search(list, 15))