def reg(num):
    for i in range(4-len(str(num))):
        print(" ",end="")
    print(num,end="")



user=int(input())

for i in range(1,user+1):
    for j in range(1,i+1):
        reg(i*j)
    print()