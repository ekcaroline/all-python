def split_it_up(a_string, sep):
    newtuple = ()
    for _ in a_string:
        if a_string.find(sep):      #searches through the string to find sep
            newtuple.append(sep)
        else:
            print()
        
    
    
