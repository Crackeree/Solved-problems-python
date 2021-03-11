import sys
import math
def side(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

a=sys.stdin.readline()
b=a.split()

c=list()
for i in b:
    c.append(float(i))

a=side(c[0],c[1],c[2],c[3])
b=side(c[2],c[3],c[4],c[5])
c=side(c[0],c[1],c[4],c[5])
s=(a+b+c)/2
A=math.sqrt(s*(s-a)*(s-b)*(s-c))
V=a*b*c
r=V/(4*A)
print("%.2lf" %(2*math.pi*r))

