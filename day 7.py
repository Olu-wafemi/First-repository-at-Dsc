

def my_cars(cars):
    '''This programme takes in an array of cars where the elements are arranged in order of the cars and two cars parked beside each other cannot be picked, the program returns the maximim worth of cars picked'''
    s = []
    
    
    for i in range(0,len(cars),2):
        if cars[i] != cars[i-1]:
            s.append(cars[i])
        else:
            s.append(cars[i+1])
    return sum(s)


print(my_cars([30,15,60,75,45,15,15,45]))