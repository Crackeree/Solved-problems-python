def p(n):
    m=list(n)
    m.reverse()
    z=''.join(m)
    if n==z:
        return 1
    else:
        return 0

def m(n):
    x=['A','H','I','M','O','0','T','U','V','W','X','Y','1','8']
    y=['E','J','L','S','Z','0']
    z=['3','L','J','2','5','O']
    m=list(n)
    for i in range(len(m)):
        for j in range(14):
         if m[i]==x[j] and m[len(m)-1-i]==x[j]:
             c=1
             break
         elif j<6 and m[i]==y[j] and m[len(m)-1-i]==z[j] :
             c=1
             break
         elif j<6 and m[i]==z[j] and m[len(m)-1-i]==y[j]:
             c=1
             break
         else:
            c=0
        if c==0:
            break
    return c
             
x=input()
if p(x)==0 and m(x)==0:
    print(x,"-- is not a palindrom")
elif p(x)==1 and m(x)==0:
    print(x,"-- is a regular palindrom")

elif p(x)==0 and m(x)==1:
    print(x,"-- is a mirrored string")
elif p(x)==1 and m(x)==1:
    print(x,"-- is a mirrored palindrom")



