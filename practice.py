try:
    print(1/0)
except:
    print("Exception")

try:
    print(1/0)
except ZeroDivisionError:
    print("zerodivisionerror")

try:
    print(1/0)
except Exception:
    print("zerodivisionerror")
try:
    print(1/3)
except RuntimeError:
    print("zerodivisionerror")
else:
    print("Inside else block") #if there is no exception then else block will be executed
try:
    arr=[1,2,3,4]
    if len(arr)<=4:
        raise ValueError("Length Exceeded")
    else:
        print("OK")
except ValueError as err:
    print(err)


class CustomException(Exception):
    pass
try:
    raise CustomException
except CustomException as err:
    print("veera")
    
    
    

    