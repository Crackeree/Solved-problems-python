a=0
b=1
n=int(input())
print("0")
print("1")
for i in range(1,n):
    s=a+b
    a=b
    b=s
    print(s)
