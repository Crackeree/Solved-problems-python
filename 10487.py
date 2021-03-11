y=1
while 1:
    a=int(input())
    if a==0:
        break
    b=list()
    for i in range(a):
        b.append(int(input()))
    c=list()
    for i in range(a-1):
        for j in range(i,a-1):
            s=b[i]+b[j+1]
            c.append(s)
    while 1:
        d=int(input())
        e=list()
        for i in range(d):
            e.append(int(input()))
        print("Case : ",y)
        for i in range(len(e)):
            f=list()
            for j in range(len(c)):
                f.append(abs(e[i]-c[j]))
            print("Closest sum of ",e[i],"is",c[f.index(min(f))])
        break
    y+=1
        
