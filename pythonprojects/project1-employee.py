"""This program will take an employee's work information, calculate the hours worked and hourly wage, and finally give a new payment."""

print(__doc__)

employee_name = input("Enter a name: ")
total_hours = float(input("Enter hours worked: "))
hour_rate = float(input("Enter hourly rate: "))

if total_hours >= 40:
    max_pay = hour_rate * 40
    extra_hours = total_hours - 40
    payment = (1.5 * hour_rate * extra_hours) + max_pay

else:
    payment = hour_rate * total_hours
    
print(employee_name, "should be paid ${:,.2f}".format(payment))

