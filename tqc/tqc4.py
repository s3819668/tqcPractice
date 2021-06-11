def reg(num):
    print(num,end="")
    for i in range(4-len(str(num))):
        print(" ",end="")


data=[]
setA=[]
sum=0
for i in range(2):
    data.append(int(input()))
for i in range(data[0]+1,data[1]+1):
    if  (i%4==0 or i%9==0)and i not in setA:
        reg(i)
        setA.append(i)
        sum+=i
print()
print(len(setA))
print(sum)



