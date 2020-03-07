def common_elements(my_dict): #Declares a function that accepts a dictionary as an argument
    g = [] #An empty list that stores a common element that appears as a key and value
    for i in my_dict: #Implementation of the program that checks if an element appears as a key and a value then prints the element/elements

        if i in my_dict.keys() and i in my_dict.values(): #Checks if an element appears in the key and value side

            g.append(i) #If True this appends such element to the element g
    print(g) #Outputs g
my_dict = {
    "A":"K",
    "B": "D",
    "C": "A",
    "D": "Z"
}
common_elements(my_dict)
