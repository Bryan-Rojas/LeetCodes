def toLowerCase(str):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(26):
        str = str.replace(upper[i], lower[i])
        
    return str    

firstStr = 'Bryan Rojas'    
secondStr = 'WOOOO'

print(toLowerCase(firstStr))
print(toLowerCase(secondStr))