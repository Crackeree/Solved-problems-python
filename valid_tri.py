x=int(input("side1: "))
y=int(input("side2: "))
z=int(input("side3: "))
if x+y>z and y+z>x and z+x>y:
    print("this is a valid triangle")
    if x==y and y==z:
      print("equilateral")
    elif x!=y and y!=z and z!=x:
      print("SCLENE")
    else:
      print("isotriangle")

else:
    print("this is not a valid triangle")
