def tax(income):
    
    owed_tax = 0.0
    
    if income > 0 and income < 6000:
        return owed_tax
    
    elif income > 6001 and income < 37000:
        owed_tax = .15 * (income - 6000)
        return owed_tax
    
    elif income > 37001 and income < 80000:
        owed_tax = 4650 + .30 * (income - 37000)
        return owed_tax

    else:
        owed_tax = 17550 + .37 * (income - 80000)
        return owed_tax
    
