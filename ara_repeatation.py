a=[1,2,3,4,5]

i=0
while i<len(a):
    c=0
    j=1+i
    while j <len(a):
        if a[i]==a[j]:
            c+=1
            del a[j]
            j-=1
        j+=1
    print("%d %d"%(a[i],c+1))
    i+=1
