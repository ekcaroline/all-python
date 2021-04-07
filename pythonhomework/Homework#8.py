def makeStr(string1, string2):
    
    condition = "YES"
    
    for char in string2:
        if string1.find(char) == -1:
            condition = "NO"
    return condition
