"""This program will take (number) employees work information,
calculate the hours worked and hourly wage, and finally give a new payment.
Then it will take the cumulative total and average pay of all the employees
entered."""

print(__doc__)


def get_input() -> None:
    """This function takes the user's input and returns the name, hours worked, and hourly rate for one employee"""
    name = input("\nEnter a name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))
    return name, hours, rate

def calc_pay(hours: float, rate: float) -> float:
    
    """This function takes the user's work info and calculates them to see if they are eligible for a bonus"""
    if hours >= 40:
        max_pay = rate * 40
        extra = hours - 40
        payment = (1.5 * rate * extra) + max_pay
        return payment
    else:
        payment = rate * hours
        return payment


if __name__ == "__main__":

    employee_count = int(input("How many employees do you want to enter? "))

    total = 0
    average = 0

    for i in range(employee_count):
        n, h, r = get_input()
        print(n, "should be paid ${:,.2f}".format(calc_pay(h, r)))
        
        total += calc_pay(h,r)
        average = total / employee_count

    print("\nThe total amount to be paid is ${:,.2f}".format(total))
    print("The average employee is paid ${:,.2f}".format(average))
        
        
        
        
        
