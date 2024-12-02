def largestNumber():
    l_list = [10,20,90,30,40,50]
    largest = 0
    for n in range(len(l_list)):
        if(largest < l_list[n]):
            largest = l_list[n]
    print(largest)
largestNumber()

