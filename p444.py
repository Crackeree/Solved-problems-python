
a=input()
b=list(a)
b.reverse()
for i in b[0]:
    if ord(i)>=48 and ord(i)<=57:
        c=1
    else:
        c=2
if c==1:
    s=b[0]
    for i in b[1:]:
        s=s+i
        z=int(s)
        if z<32:
            continue
        else:
            print(chr(z),end=(''))
        s=''
    
    
    





        


elif c==2:
    for i in b:
     z=list(str(ord(i)))
     z.reverse()
     s=''.join(z)
     print(s,end=(''))
    
    





    




