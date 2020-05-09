def wedding_chow(chow):
    '''This programme returns a tuple of two elements where the first element is an integer representing the maximum number of guests that can recieve complete chow and the second is the left over chow as astring arranged in order (rsmfd)'''
    base = ['r','s','m','f','d']
    b = []
    
    for i in chow:
        b.append(i)
        for j in b:
            n = b.count(j)
            
            if j in base:
                sol = len(b)//5
                n = len(b)%5
                
           
                

    

            
            
    return (sol,chow[0:n])
print(wedding_chow('rsmfdrsmfdrsmd'))