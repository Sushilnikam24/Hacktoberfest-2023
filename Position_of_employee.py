# Asking the manager for the employee position and the monthly hours worked
employee_position = input("Please enter the employee position (chef, waiter or deliver): ").lower()
monthly_hours_worked = float(input("Please enter the number of monthly hours worked: "))

# pay rate based on the employee position
if employee_position == "chef":
    pay_rate = 50
elif employee_position == "waiter":
    pay_rate = 40
elif employee_position == "deliver":
    pay_rate = 35
else:
    print("Invalid employee position. Please enter chef, waiter or deliver.")
    pay_rate = 0

# gross income, income tax and net income based on the pay rate and monthly hours worked
gross_income = pay_rate * monthly_hours_worked
income_tax = gross_income * 0.2
net_income = gross_income - income_tax

# monthly income of the employee after tax is deducted
if pay_rate != 0:
    print(f"Net monthly income of the employee after tax is deducted: ${net_income:.2f}")
