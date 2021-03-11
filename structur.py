"""a=int(input("enter a num: "))
i=0
j=0
while(i<=a):
 j=0
 while(j<=i):
  print("*",end=("."))
  j=j+1
 k=i
 while(k<(a-1)):
     print(" \n")
     k=k+1
 i=i+1
"""

"""n=int(input())
for i in range(1,n+1):
 print("*"*i)
n=n-1
for i in range(n,0,-1):
 print("*"*i)
"""


n=int(input())

for i in range(0,n):
 s=""
 for j in range(0,i+1):
  s=s+"*"
 print(s)
