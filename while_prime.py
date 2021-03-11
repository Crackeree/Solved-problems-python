n=int(input())
i=2
count=0
while i<n:
    if n%i!=0:
        count+=1
    i+=1
if count==(n-2):
    print("prime")
else:
    print("not prime")
