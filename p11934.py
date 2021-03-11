import sys
while 1:
 x=sys.stdin.readline()
 y=x.split()
 a=int(y[0])
 b=int(y[1])
 c=int(y[2])
 d=int(y[3])
 L=int(y[4])
 if(a==0 and b==0 and c==0 and d==0 and L==0):
     break

 count=0
 i=0
 while i<L+1:
    TOT=a*i**2+b*i+c
    if TOT%d==0:
        count+=1
    i+=1
 print(count)
