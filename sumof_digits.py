num=int(input("enter the integer value:"))
rem=0
sumdigits=0
while(num!=0):
    rem=num%10
    num//=10
    sumdigits+=rem
print("sum of  digits are:",sumdigits)