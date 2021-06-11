data=[]
sum=0
for i in range(2):
    data.append(int(input()))
for i in range(data[0],data[1]+1):
    sum+=i
print(sum)