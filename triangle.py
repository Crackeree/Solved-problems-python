x=int(input())
y=int(input())
z=int(input())
if x==y and y==z:
 print("equilateral")
elif x!=y and y!=z and z!=x:
    print("SCLENE")
else:
    print("isotriangle")
