import sys
while 1:
 a=sys.stdin.readline()
 b=a.split()
 for i in b:
    c=list(i)
    c.reverse()
    i=''.join(c)
    print(i,end=(' '))
 print("")
 
    
