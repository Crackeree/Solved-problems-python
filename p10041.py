t=int(input())


while t:
    s=0
    b=list()
    r=int(input())
    while r:
        a=int(input())
        b.append(a)
        r-=1
    for i in range(1,len(b)):
        d=abs(b[i-1]-b[i])
        s=s+d
    t-=1
    print(s)
