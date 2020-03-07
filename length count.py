def length_count(strings):
    sage = []
    dicts = 
    count = 1
    for i in range(len(strings)):
        for j in range(i+1,len(strings)):
            if len(strings[i]) == len(strings[j]):
                count += 1
                s = len(strings[j]), count
                sage.append(s)               
    print(sage)
    print(dicts)
            
length_count(["Argentina","Brazil","Venezuela"])