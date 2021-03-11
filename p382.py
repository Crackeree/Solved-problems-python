import sys
a=sys.stdin.readline()
b=a.split()
c=list()
for i in b:
    z=int(i)
    c.append(z)
del c[len(c)-1]
print("PERFECTION OUTPUT")
i=0   
for i in range(len(c)):
    j=1
    s=0
    while j<c[i]:
       if c[i]%j==0:
           s=s+j
       j+=1
    if s==c[i]:
        print(c[i],"PERFECT")
    elif s>c[i]:
        print(c[i],"ABUNDENT")
    else:
        print(c[i],"DEFICIENT")
print("END OF OUTPUT")
