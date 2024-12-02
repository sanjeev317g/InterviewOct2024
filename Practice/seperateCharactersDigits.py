def charDigits():
    str = "Test123"
    str1 = []
    str2 = []
    for n in str:
        if(n.isalpha()):
            str1.append(n)
            
        else:
            str2.append(n)
    print(str2)    
    
charDigits()