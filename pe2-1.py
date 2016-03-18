def seq(n):
    
    trml = [ 0 , 1 ]
    
    a = trml[1]
    
    if n < 1:
        
        return trml[1]
        
    else:
        
         x = a + (n-1)*(trml[-1]+trml[-2])
    
    
    trml.append([x])
    
    return trml




print(seq(7))
