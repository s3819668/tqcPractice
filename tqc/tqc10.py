setence=input()
if len(setence)%2==1:
    print(setence[len(setence)//2])
else:
    print(setence[len(setence)//2-1]+setence[len(setence)//2])