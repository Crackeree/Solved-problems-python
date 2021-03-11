import sys
a=int(input())
z=sys.stdin.readline()
b=z.split()
y=list()
for i in b:
    y.append(int(i))



x=list()

c=int(input())

s=0
for i in range(0,a-1):
 for j in range(1+i,a):
  s=y[i]+y[j]
  if c==s:
      x.append([y[i],y[j]])


low=abs(x[0][0]-x[0][1])
for i in range(1,len(x)):
    for j in range(0,1):
        d=abs(x[i][0]-x[i][1])
        if low>d:
         low=d

for i in range(len(x)):
    for j in range(0,1):
        d=abs(x[i][0]-x[i][1])
        if low==d:
            print(x[i][0],x[i][1])
            



      
      
