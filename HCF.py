def hcf(a,b):
    if a>b:
        count=b
    else:
        count=a
    for i in range(1,count+1):
        if(a%i==0 and b%i==0):
            res=i
    print(res)
n1=int(input())
n2=int(input())
hcf(n1,n2)
    
    