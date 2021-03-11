a=int(input("enter an initial:"))
b=int(input("enter a terminal:"))

for n in range(a,b+1):
 count=0
 for i in range(2,int(n/2)+1):
     d=n%i
     if d!=0:
        count=count+1
 if count==int(n/2)-1:
  print(n)
