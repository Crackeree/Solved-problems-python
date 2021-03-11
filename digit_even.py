a=100

count=0
while a<=400:
 temp=a
 j=1
 while j:
    d=temp%10
    if d%2==0:
     count = count+1
    temp=(temp/10)-(temp%10)/10
    if temp==0:
     j=0
 if count==3:
   b=list(str(a))
   for k in range(3):
    print(b[k],end=(" "))
   print("\n")
 count=0
 a=a+1
 
  

 
 
