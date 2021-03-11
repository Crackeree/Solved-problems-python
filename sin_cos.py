import math
a=int(input("Cos"))
x=a*(math.pi)/180
acc=100
j=1
c=0

for n in range(0,acc,2):
    s=j*x**n/math.factorial(n)
    c=c+s
    j=j*-1
print(c)
print(("%s%d")%("Sin",a))
print((1-c**2)**0.5)

    

