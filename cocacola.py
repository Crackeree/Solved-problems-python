a=int(input())
i=1
s=0
while i:
    r=a%3
    a=a//3
    s=s+a
    a=r+a
    if a<=3:
     s=s+1
     i=0
print(s)
