gallons = float(input("Enter gallons used (-1 to quit): "))

total_gal = 0
total_mil = 0
total_avg = 0

while gallons > 0:
    
    miles = float(input("Enter miles driven: "))
    avg = miles / gallons
    print("MPG: {:.2f}".format(avg))

    total_gal = total_gal + gallons
    total_mil = total_mil + miles
    total_avg = total_mil / total_gal
    
    gallons = float(input("\nEnter gallons used (-1 to quit): "))
        
print("\nAverage MPG: {:.2f}".format(total_avg))
        
