def sum_of_values(my_dict,my_list): #Declares a sum_of_values function that accepts a dictionary and a list
    g = [] #An empty list that stores the values of my_dict that appears in my_list
    for i in my_list: #Implementation of the program that checks of a string in my_list is in my_dict and then returns the sum of the value/values
        if i in my_dict.keys():
            b = my_dict.get(i)
            g.append(b)
        r = sum(g)
    print(r)
            
        
            
my_dict = {"a":2,"b":3,"c":4}
sum_of_values(my_dict,["d"])



j = [1,2,3,4,5,6]
print(j[j[0]])
