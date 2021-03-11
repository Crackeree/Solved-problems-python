import sys

d=list(map(int,input().split())  )
i=0
while i<len(d):
    c=0
    j=1+i
    while j <len(d):
        if d[i]==d[j]:
            c+=1
            del d[j]
            j-=1
        j+=1
    print("%d %d"%(d[i],c+1))
    i+=1
    
    



