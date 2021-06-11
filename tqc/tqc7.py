def dec(word):
   print("'",word,"'",sep="",end="")
loop=True
data=[]

while loop:
    word=input()
    if  word!="end":
        data.append(word)
    else:
        loop=False
print(data)
print("(",end="")
for i in range(len(data)):
    dec(data[i])
    if i!=len(data)-1:
        print(", ",end="")
print(")")

print("(",end="")
top=[data[0],data[1],data[2]]
last=[data[-3],data[-2],data[-1]]

for i in range(len(top)):
    dec(top[i])
    if i!=len(top)-1:
        print(", ",end="")
print(")")

print("(",end="")
for i in range(len(last)):
    dec(last[i])
    if i!=len(last)-1:
        print(", ",end="")
print(")")