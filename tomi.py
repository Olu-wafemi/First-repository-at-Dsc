def itos(integer):
    '''This programme converts an integer to a string'''
    
    s = []
    while True:
        
        s.append(chr(ord('0') + integer % 10))
        integer //= 10
    
        if integer == 0:
            break
        
                

    return ("'") + ''.join(reversed(s)) + ("'")
print(itos(12))
def stoi(string):

    '''This programme converts a string to an integer'''
    start = 0
    exp = len(string) - 1

    for i in string:
       
            
    
        value = ord(i) - ord('0')
        start += value * (10**exp)
        exp += -1
    return start
print(stoi('12'))
def ftos(float):
    if float < 1:
        return ['']
    s = ftos(float-10)
    v = []
    print(type(s))
    
    s = ['' + i for i in s]
    print(s)

        
        
    
(ftos(1.345))