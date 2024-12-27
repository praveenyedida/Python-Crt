num=int(input("enter the value:"))
rem=0
reversed_num=0
temp=num
while(num!=0):
    rem=num%10
    reversed_num=reversed_num*10+rem
    num//=10
if(reversed_num==temp):
    print("the given number is a palindrome")
else:
    print("the given number is not a palindrome")