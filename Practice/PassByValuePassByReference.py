def passByValue(x):
    x = x + 10
    print(f"Check the value {x}")
x= 5
passByValue(x)
print(f"After function call {x}")

def passByReference(l_list):
    l_list.append("Mahesh Friend")
    print(f"Inside functon call {l_list}")
l_list = ["Mahesh","Prasanna"]
passByReference(l_list)
print(f"After function call {l_list}")

