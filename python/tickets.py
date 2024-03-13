import datetime 

# define tax rate and prices 
SALES_TAX_RATE = 0.055
PR_TICKET = 10.99

# define global variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

def main():
    while True:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N): ").lower()
        if yesno == "n":
            print("Thanks for your order! Please Enjoy the movie!")
            break

def get_user_data(): 
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('------------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighborhood movie house')
    print('-------------------------------')
    print('Tickets.       ${:,.2f}'.format(subtotal))
    print('Sales Tax.     ${:,.2f}'.format(sales_tax))
    print('Total.         ${:,.2f}'.format(total))
    print('-------------------------------')
    print(datetime.datetime.now())

main()
