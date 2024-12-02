def fibonacciSeries():
    # 1,1,2,3,5,8
    num1 = 0
    num2 = 1
    num3 = 0
    for n in range(10):
        num3 = num1 + num2
        print(num3)
        num1 = num2
        num2 = num3
fibonacciSeries()