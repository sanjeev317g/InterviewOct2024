def IPC(func):
    def cal():
        func()
        print("second")
    return cal

@IPC
def test1():
    print("here is the test1 decorator function")
    return test1

# test1()


def ipc(func):
    def rtos():
        func()
        print("this is in queue for second")
    return rtos

@ipc
def testdec():
    print("Here the decorator first")

# testdec()
def ipc(func):
    def abc():
        func()
        print("will print later")
    return abc


@ipc
def myFunction():
    print("Here is the decorator")

myFunction()