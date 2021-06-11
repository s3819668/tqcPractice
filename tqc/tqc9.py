f=open(file="file.txt")
data=f.read()


user=[]
for i in range(5):
    user.append(input())
print(data)
for i in user:
    print(i)