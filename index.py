fname = input('enter your first name ')
lname = input('enter last name ')
fullName = f"{fname} {lname}"

rate = float(input('Daily Rate '))
days = float(input('days present ') )

grossIncome = rate * days
pag_ibig= 100
philhealth = 300
sss = 200
deductions = pag_ibig + philhealth + sss

if grossIncome < 21000:
    grossSalary = grossIncome
elif 21000==grossIncome<=50000:
    grossSalary= 90/100 * grossIncome
elif 51000==grossIncome<=90000:
    grossSalary= 88/100 * grossIncome
elif grossIncome>= 91000:
    grossSalary= 85/100 * grossIncome
total_pay = grossSalary-deductions

print(f"Hello {fullName} below are the breakdown of your payroll for this month.Thank you.\nGross Income: {grossSalary}\nDeductions: {deductions}\nTake Home Pay: {total_pay}")







        
        


