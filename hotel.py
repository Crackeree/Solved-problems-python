while 1:
    
 a=int(input())
 b=int(input())
 if a==0 and b==0:
     break
 s=0
 while 1:
    s=s+a
    a+=1
    if s>=b:
        print(a-1)
        break
