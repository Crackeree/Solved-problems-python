
def bee( n):
 a=0
 b=1

 s=0
 for i in range(n):
  s=a+b+1
  a=b
  b=s
 return s

n=int(input())
if n==1:
    print("1 1")
else:
 print(bee(n-1),bee(n))
 
