n=int(input())
ara=list()
for i in range(n):
    s=input()
    ara.append(s)
for i in range(n):
    print(str(ara[i][0])+str(len(ara[i])-2)+str(ara[i][len(ara[i])-1]))
