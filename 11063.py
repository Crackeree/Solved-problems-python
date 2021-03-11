import sys
while 1:
  c=0
  a=int(input())
  b=sys.stdin.readline()
  z=b.split()
  c=list()
  for i in z:
      c.append(int(i))
  d=list()    
  for i in range(len(c)):
      for j in range(i,len(c)):
          d.append(c[i]+c[j])
  for i in range(len(d)):
      if i == len(d)-2 or c==1:
          break
      for j in range(i+1,len(d)):
          if d[i]==d[j]:
              print("This is not a B2 sequence")
              c=1
              break;
  if(c==0):
       print("This is a B2 sequence")
  
          
              
          




    
    
    
    

