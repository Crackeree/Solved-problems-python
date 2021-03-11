import sys
a=sys.stdin.readline()
b=list()
b=a.split()
c=list()
for i in b:
 c.append(int(i))
z=2*c[1]
d=list()
d.append(1)
for i in range(1,c[0]):
    count=0
    for j in range(2,i):
        if i%j!=0:
            count+=1
        else:
            break
    if count==i-2:
        d.append(i)
if len(d)%2!=0:
    x=(len(d)-z+1)//2
    y=(len(d)+z-1)//2
    print(c[0],c[1],":",end=(" "))
    for i in d[x:y]:
        print(i,end=(" "))
else :
    x=(len(d)-z)//2
    y=(len(d)+z)//2
    print(c[0],c[1],":",end=(" "))
    for i in d[x:y]:
        print(i,end=(" "))
    
        
