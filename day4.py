def bits_of_gray(gray):
    '''This programme returns a list of gray codes in which every succesive pair of numbers differs in only one bit'''
    if gray == 0:
        return ['']
    
    conv = bits_of_gray(gray-1)
    print(conv)
    conv_2 = conv.copy()
    print(conv_2)
    
    
    
    
    
    conv = ['0'+ i for i in conv ]
    conv_2 = ['1'+ i for i in reversed(conv_2)]
    return conv + conv_2
print(bits_of_gray(3))