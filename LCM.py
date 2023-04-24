def lcm(a,b):
    if(a>b):
        count=a
    else:
        count=b
    while(True):
        if(count%a==0 and count%b==0):
            res=count
            break
        count+=1
    return res
n1=int(input())
n2=int(input())
print(lcm(n1,n2))

        
        
        