def wordcounter(string):                             #create function that takes in string arg
    
    makeString = dict()                              #create a dictionary
    
    for char in string:                              #iterates through string and sets char to lowercase
        char = char.lower()

        if char in makeString:                       #if char appears, increment char count
            makeString[char] += 1
        
        else:
            makeString[char] = 1                     #if char hasn't appeared, increments char count
    return makeString
    

print(wordcounter("pneumonoultramicroscopicsilicovolcanoconiosis"))



    
        
