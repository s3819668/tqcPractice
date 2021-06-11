def find(data):
    biggest = 0
    for i in range(len(data)):##跑每個開始
        array = []
        now=i
        array.append(i)
        while data[now] not in array:
            array.append(now)
            now=data[now]
        if  len(array)>biggest:
            biggest=len(array)
    return biggest
data=input().split(",")
for i in range(len(data)):
    data[i]=int(data[i])
print(find(data))
