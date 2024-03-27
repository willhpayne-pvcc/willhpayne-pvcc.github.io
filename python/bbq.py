# Name: Will Payne
# Prog Purpose: This program find the cost of a meal at Branch BBQ
# Price for an adult meal: $19.95
# Price of a child meal: $11.95
# Service fee: 10%
# Sales tax rate: 6.2%

import datetime

# define goal variables #
# define tax rate, service fee, and prices
ADULT_MEAL = 19.95
CHILD_MEAL = 11.95
SALES_TAX_RATE = .062
SERVICE_FEE = .10

# define global variables
num_adult_meals = 0
num_child_meals = 0
sales_tax = 0
service_fee = 0
subtotal_adult_meals = 0
subtotal_child_meals = 0
subtotal = 0
total = 0

# define program funcitons
def main():

    more_meals = True
    while more_meals:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again? (Y or N)")
        if yesno == "N" or yesno =="n":
            more_meals = False
            print("Thank you for your order. Enjoy your meal!")

def get_user_data():
    global num_adult_meals, num_child_meals
    num_adult_meals = int(input("How many adult meals?: "))
    num_child_meals = int(input("How many children meals?: "))

def perform_calculations():
    global subtotal, sales_tax, total, subtotal_adult_meals, subtotal_child_meals, service_fee,num_adult_meals, num_child_meals
    subtotal_adult_meals = num_adult_meals*ADULT_MEAL
    subtotal_child_meals = num_child_meals*CHILD_MEAL
    subtotal= subtotal_adult_meals + subtotal_child_meals
    service_fee = subtotal*SERVICE_FEE
    sales_tax= subtotal*SALES_TAX_RATE
    total = subtotal + service_fee + sales_tax

def display_results():
    currency = '8,.2f'
    print('-------------------------------')
    print('-----Branch Barbeque Buffet----')
    print('-------------------------------')
    print('Adult Meals     $ ' + format(subtotal_adult_meals,currency))
    print('Children meals  $ ' + format(subtotal_child_meals,currency))
    print('Meal total      $ ' + format(subtotal,currency))
    print('service fee     $ ' + format(service_fee,currency))
    print('Sales Tax       $ ' + format(sales_tax,currency))
    print('Total           $ ' + format(total,currency))
    print('------------------------------')
    print(str(datetime.datetime.now()))


#### Call on main program to execute
main()