def amstrongNumber():
    num = 1634
    count = 1
    amstrongNumber = 0
    l_length = len(str(num))
    while(num != 0):
        num1 = int(num % 10)
        for n in range(l_length):
            count = int(num1 * count)
        amstrongNumber = count +amstrongNumber
        count = 1
        num = num / 10
    print(amstrongNumber)

amstrongNumber()
