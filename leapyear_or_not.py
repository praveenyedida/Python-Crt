n=int(input("enter the year:"))
if((n%4==0 and n%100!=0) or n%400==0):
    print("the given year is leap year")
else:
    print("the given year is not a leap year")