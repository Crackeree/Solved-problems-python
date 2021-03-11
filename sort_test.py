l=int(input())
a=list()
for i in range(0,l):
 a.append(int(input()))

a.sort()
if l%2==0:
 print(int((a[l//2-1]+a[l//2])/2))
else:
 print(a[(l+1)//2-1])
