def plenty_of_arguments(a,b,**kwargs):
    
    
    if sum(kwargs.values()) > 100:
        print("True")
    else:
        print("False")
plenty_of_arguments(20,10)
