num=int(input("enter the integer value:"))
odddigitcount=0
rem=0
while(num!=0):
    rem=num%10
    if(rem%2!=0):
        odddigitcount+=1
    num//=10
print("number of odd digits are:",odddigitcount)