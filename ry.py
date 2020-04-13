points = { 1: ["A","I","L","N","O","R","S","T","U"]  , 2: ['D','G'], 3:["B","C","M","P"], 4:["F","H","V","W","Y"], 

5:"K",8:["J","X"],10:["Q","Z"]}
alphabet = []
new_dict = {}



def word_score(score):
    
    
    count = 0
    while count <= 15:
        
        alphabets = input("Enter the alphabet   ")
        
        
        alphabets = alphabets.upper()
        alphabet.append(alphabets)
        for alphabe in alphabet:
            for key,value  in points.items():
                if alphabe in value:
                    new_dict.update({key:value})
            count+=1
    print(new_dict)
    print(sum(new_dict.keys()))
                
                    
                    
                    

                    
        


                

                
                    
            

word_score(new_dict)

