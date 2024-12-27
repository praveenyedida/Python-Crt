n=int(input("enter the integer value:"))
digitcount=0
while(n!=0):
    n//=10
    digitcount+=1
print(digitcount,"digits")