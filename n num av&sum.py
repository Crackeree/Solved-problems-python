list_len=int(input())
list=[]
i=0
for i in range(0,list_len):
  list.append(int(input()))
sum=0
for i in range(0,list_len):
 sum=sum+list[i]

print(sum,sum/list_len)
