def amstrongNumber():
    num = 1634
    l_length = len(str(num))
    count = 1
    total = 0
    while(num != 0):
        num1 = num % 10
        for n in range(l_length):
            count = int(num1 * count)
        num = int(num / 10)
        total = count + total
        count = 1
    print(total)
amstrongNumber()



