data=[]
for i in range(10):
    data.append(int(input()))
data.sort(reverse=True)
print(data)
print(data[0],data[1],data[2])