emp_name=str(input("enter employee name:"))
emp_dsg=str(input("enter the employee designation:"))
emp_salary=int(input("enter the employee salary:"))
spcl_allowance=int(input("enter the employee special allowance:"))
emp_bonus=int(input("enter the employee bonus:"))
#gross monthly salary
grs_mnth_slry=emp_salary+spcl_allowance
#gross annual salary
grs_annual_slry=(grs_mnth_slry*12)+emp_bonus
#taxable income
if(grs_annual_slry>500000):
    taxable_amount=grs_annual_slry*0.15
elif(grs_annual_slry>400000):
    taxable_amount=grs_annual_slry*0.10
else:
    taxable_amount=grs_annual_slry*0.02
taxable_income=grs_annual_slry-taxable_amount
print("--------------------------------------------------")
print("employee name:",emp_name)
print("employee designation:",emp_dsg)
print("employee salary:",emp_salary)
print("gross monthly salary of the employee:",grs_mnth_slry)
print("the gross annual salary of the employee is:",grs_annual_slry)
print("the taxable income of the employee:",taxable_income)
