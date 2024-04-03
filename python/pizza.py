# Tanner & Will 
# Prog Purpose: This program finds the cost of a pizza meal
#   This program uses TUPLES for the pizza sizes and prices

import datetime

######################## define items and prices in tupeles and tax rate ###########################

#indexes--------> 0          1         2          3
PIZZA_SIZE =     'S',       'M',      "L",       'X',
PIZZA_PRICE =    9.99,      12.99,   17.99,      21.99,

DRINK_PRICE = 3.99
STICKS_PRICE = 6.99

SALES_TAX_RATE = .055

##################### define globals #############################

num_pizzas = 0
num_drinks = 0
num_breadsticks = 0

cost_pizza = 0
cost_drinks = 0
cost_breadsticks = 0

subtotal = 0
taxamt = 0
total = 0

####################### define prog functions ##########################

def main():

    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input('Would you like to order again (Y or N)?: ')
        if askAgain.upper() == "N" or askAgain == "n":
            more = False
            print("Thank you for your order. Emjoy your meal!")

def get_user_data():
    global type_pizza, num_pizzas, num_drinks, num_breadsticks

    part1 = "Size of pizza you would like to order: "
    part2 = "\n\tS for Small \n\tM for Medium \n\tL for Large \n\tX for Extra Large \nSize: "
    type_pizza = input(part1 + part2)
    type_pizza = type_pizza.upper()

    num_pizzas = int(input("How many pizzas would you like to order? "))
    num_drinks = int(input("Number of drinks: "))
    num_breadsticks = int(input("Number of breadsticks: "))


def perform_calculations():
    global size, cost_pizza, cost_drinks, cost_breadsticks, taxamt, total, subtotal

    for i in range(len(PIZZA_SIZE)):
        if type_pizza == PIZZA_PRICE[i]:
            cost_pizza = num_pizzas * PIZZA_PRICE[i]

    cost_drinks = num_drinks * DRINK_PRICE
    cost_breadsticks = num_breadsticks * STICKS_PRICE

    subtotal = cost_pizza + cost_drinks + cost_breadsticks
    taxamt = subtotal * SALES_TAX_RATE
    total = subtotal + taxamt

def display_results():
    currency = '8,.2f'
    dt_full = str(datetime.datetime.now())
    dt_short = dt_full[1:16]
    line =('-------------------------------------')

    print (line)
    print ('*********** PALOMA PIZZA ************')
    print ('**** Your neighborhood pizzaria! ****')
    print (               dt_short)
    print (line)
    print ("Number of pizzas: " + str(num_pizzas))
    print (line)
    print ("Pizzas:          \t $" + format(cost_pizza, currency))
    print ("Drinks:          \t $" + format(cost_drinks, currency))
    print ("Bread Sticks:    \t $" + format(cost_breadsticks, currency))
    print (line)
    print ("Subtotal:        \t $" + format(subtotal, currency))
    print ("Tax:             \t $" + format(taxamt, currency))
    print ("Total:           \t $" + format(total, currency))
    print (line)

main()