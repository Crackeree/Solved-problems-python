a=list()
i=0
while 1:
    a.append(int(input()))
    if a[i]==-1:
        del a[i]
        break
    
    i+=1
for i in range(len(a)):
    if i%2==0:
        print(a[i//2])
    else:
        print((a[i//2]+a[(i//2)+1])//2)

