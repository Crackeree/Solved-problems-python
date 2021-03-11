import sys
def avg(x):
    s=0
    j=0
    for i in x:
        s=s+i
    return s/len(x)

n=int(input())
for i in range(n,0,-1):
    a=list(map(int,input().split()))
    m=a[0]
    del a[0]
    avr=avg(a)
    count=0
    for i in a:
        if avr<i:
            count+=1
    print("%.3lf"%(100*count/m))
    
