


ini=int(input())
ter=int(input())



d=0


c=0
for j in range(ini,ter+1):
  c=j
  i=1
  s=0
  while i:
    d=int(c%10)
    s=s+d**len(str(j))
    c=int(c/10)
    if c==0:
        i=0
  if s == j:
    print(j,"is a armstrong")
    
