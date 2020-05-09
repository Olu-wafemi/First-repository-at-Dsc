
def order(array):
    size = []
    array.sort()
    
    for i in range(len(array)-1):
        if array[i+1] - array[i] >= 1:
            size.append(array[i])
            
    return size
print(order([100,4,200,1,3,2]))


