
def yy(year):
    if year%400==0:
        print(year," is a leap year.")
        return 0
    if year%100==0:
        print(year," is not a leap year.")
        return 0
    if year%4==0:
        print(year , " is a leap year.")
        return 0
    else:
        print(year + " is not a leap year.")
year=int(input())
yy(year)