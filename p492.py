import sys
a=sys.stdin.readline()
b=a.split()
k=0
for i in b:
    z=i
    c=list(z)
    if i==b[len(b)-1]:
        i=i.replace('.','')
        k=1
    if (c[0]!="a" and c[0]!="e" and c[0]!="i" and c[0]!="o"  and c[0]!= "u" and c[0]!="A" and c[0]!="E"and c[0]!="I"and c[0]!="O"and c[0]!="U" ):
      j=c[0]
      del (c[0])
      c.append(j)
      d=''.join(c)
      d=d+"ay"
      i=d
      if k==1:
          i=i+"."
    else:
        i=i+"ay"
        if k==1:
            i=i+'.'
    print(i,end=(' '))
    

