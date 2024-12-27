num=int(input("enter the number:"))
if(num%3==0 and num%5==0):
    print("divisible by 3")
else:
    print("not divisible by 3 & 5")
result=" it is divisible by 3"if(num%3==0 and num%5==0) else "it is not divisible by 3 & 5"
print(result)