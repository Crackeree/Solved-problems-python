import math
a=int(input())
b=[]
count1=0
count2=0
count3=0
count4=0
for i in range(a):
    b.append(int(input()))
b.sort()
for i in range(a):
    if b[i]==1:
        count1+=1
    elif b[i]==2:
        count2+=1
    elif b[i]==3:
        count3+=1
    else:
        count4+=1

if count1>count3:
    count1=count1-count3
    if count2%2==0:
        z=int(count4+count3+count2/2+int(math.ceil(count1/4) ))
        print(z)

    else :
         z=int(count4+count3+math.ceil(count2/2)+int(math.ceil(  (count1-2)/4 )     )  )
         print(z)
elif count1<count3:
    z=int(count4+count3+int(math.ceil(count2/2)))
    print(z)
else:
    z=int(count4+count3+int(math.ceil(count2/2)))
    print(z)
        
