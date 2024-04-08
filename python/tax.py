import datetime

# Define tax rate and prices
PPT_RATE = 0.042
RELIEF_RATE = 0.33

# Define global variables
assessed_val = 0
relief_yn = "N"

def main():
    goodbye_msg = "Personal Property Taxes are Due DEC 5, 2024"
    while True:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate again (Y or N): ").lower()
        if yesno == "n":
            print("Thank you for using the tax calculator.")
            break

def get_user_data():
    global assessed_val, relief_yn
    assessed_val = int(input("What is the assessed value of the vehicle: "))
    relief_yn = input("Is the vehicle eligible for relief? (Y or N): ").upper()

def perform_calculations():
    global tax_amount, total_due
    tax_amount = assessed_val * PPT_RATE
    if relief_yn == "Y":
        tax_amount *= (1 - RELIEF_RATE)
    total_due = assessed_val - tax_amount

def display_results():
    print('------------------------------')
    print('**** PERSONAL PROPERTY TAX ****')
    print('------------------------------')
    print('Assessed Value:  ${:,.2f}'.format(assessed_val))
    print('Tax Amount:      ${:,.2f}'.format(tax_amount))
    print('Total Due:       ${:,.2f}'.format(total_due))
    print('------------------------------')
    print(datetime.datetime.now())

main()
