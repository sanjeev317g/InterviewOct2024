def elementApperar():
    l_list = [10,20,30,40,30,50,10]
    l_appers = {}
    for n in l_list:
        if n in l_appers:
            l_appers[n] += 1
        else:
            l_appers[n] = 1
    print(l_appers)
elementApperar()
