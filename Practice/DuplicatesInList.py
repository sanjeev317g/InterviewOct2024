def duplicateInList():
    l_list = [1,2,3,4,2,3,5,6,7,9,8,7]
    count = 0
    d_list = {}
    for n in range(len(l_list)):
        for n1 in range(1, len(l_list)):
            if(l_list[n] == l_list[n1]):
                print(l_list[n])
            


 

duplicateInList()


