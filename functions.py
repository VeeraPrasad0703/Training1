def fun():
    try:
        a=int(input())
        b=int(input())
    except ValueError as err:
        print(err)
        
    print(a+b)
fun()
def fun1():
    return 10,20,30
sum=fun1()
print(sum)