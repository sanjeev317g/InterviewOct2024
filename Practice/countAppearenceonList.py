def countApperance():
    l_list = [10,20,30,50,60,10,20]
    l1_list = {}
    for n in l_list:
        if n in l1_list:
            l1_list[n] += 1
        else:
            l1_list[n] = 1
    print(l1_list)
countApperance()