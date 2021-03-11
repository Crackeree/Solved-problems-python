lenth=int(input())
x=list()
for i in range(lenth):
 a=int(input())
 x.append(a)
x.sort() 
for i in range(len(x)):
    count=0
    if i>0:
     if x[i-1]==x[i]:
        continue 
    for j in range(1+i,len(x)):
     if x[i]==x[j]:
        count+=1
     if i==len(x)-2:
        break
    print(x[i],count+1)
