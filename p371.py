import sys
def how_long(n):
    c=0
    while 1:
        if(n%2==0):
            n=n/2
            c+=1
        else:
            n=3*n+1
            c+=1
        if n==1:
            break
    return c;
while 1:
 a=sys.stdin.readline()
 b=list()
 b=a.split()
 c=list()
 for i in b:
    c.append(int(i))
 if(c[0]==0 and c[1]==0):
     break
 d=list()
 for i in range(c[0],c[1]+1):
    d.append(how_long(i))
 for i in range(len(d)):
    if d[i]==max(d):
        print("Between",c[0],"and",c[1],",",c[0]+i,"generates the longest sequence of",max(d),"values")
        break
  

