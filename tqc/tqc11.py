def find(setence):
    for i in range(len(setence)):
        for j in range(i + 1, len(setence)):
            if setence[i] == setence[j]:
                print(i+1)
                return 0
    print(-1)

setence=input()
find(setence)
