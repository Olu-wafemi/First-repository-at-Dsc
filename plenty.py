def plenty_of_arguments(a,b,**kwargs,): #Declares a function that accepts a parameter a and b and kwargs
    g = [] #An emptyblist that stores the value of any a or b inputted
    g.append(a) #appends the value of a to g
    g.append(b) #appends the value of b to g
    
    if sum(g) > 100: #checks if the sum of a and   is greater than 100 and prints true if the condition is true
        print("True")
    elif sum(kwargs.values()) > 100: #checks if the sum of the values of the dictionary is greater than 100 and prints rue if the condition is correct
        print("True")
    else: #Else False is thre output
        print("False")
plenty_of_arguments(50,60) #Calls the plenty_of_arguments function