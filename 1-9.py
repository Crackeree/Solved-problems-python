a=int(input())
count0=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
for i in range(1,a+1):
    k=i
    while 1:
        d=k%10
        k=k//10
        if d==0:
         count0+=1
        if d==1:
         count1+=1
        if d==2:
         count2+=1
        if d==3:
         count3+=1
        if d==4:
         count4+=1
        if d==5:
         count5+=1
        if d==6:
         count6+=1
        if d==7:
         count7+=1
        if d==8:
         count8+=1
        if d==9:
         count9+=1
        if k==0:
         break
print(count0,count1,count2,count3,count4,count5,count6,count7,count8,count9)
