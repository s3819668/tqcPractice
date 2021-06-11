word=[]
for i in range(4):
    word.append(input())

print("|",end="")
for i in range(10-len(word[0])):
    print(" ",end="")
print(word[0],end="")
for i in range(10-len(word[1])):
    print(" ",end="")
print(word[1],end="")
print("|",end="")
print()

print("|",end="")
for i in range(10-len(word[2])):
    print(" ",end="")
print(word[2],end="")
for i in range(10-len(word[3])):
    print(" ",end="")
print(word[3],end="")
print("|",end="")
print()

print("|",end="")
print(word[0],end="")
for i in range(10-len(word[0])):
    print(" ",end="")
print(word[1],end="")
for i in range(10-len(word[1])):
    print(" ",end="")
print("|",end="")
print()

print("|",end="")
print(word[2],end="")
for i in range(10-len(word[2])):
    print(" ",end="")
print(word[3],end="")
for i in range(10-len(word[3])):
    print(" ",end="")
print("|",end="")
print()