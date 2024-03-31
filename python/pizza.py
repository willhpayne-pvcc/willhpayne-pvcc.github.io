# Name: William Payne, Tanner Jenkins
# Purpose: Pizza calc

import datetime 

# Define global variables
SALES_TAX_RATE = 0.055
PIZZA_PRICES = {'s': 9.99, 'm': 12.99, 'l': 14.99, 'xl': 17.99}
DRINK_PRICE = 3.99
BREADSTICK_PRICE = 6.99

# Initialize order counts
order_counts = {'s': 0, 'm': 0, 'l': 0, 'xl': 0}
num_drinks = 0
num_breadsticks = 0
num_pizzas = 0  # Add this line to initialize the number of pizzas

def main():
    global order_counts, num_drinks, num_breadsticks, num_pizzas
    another_order = True
    display_menu()
    
    while another_order:
        get_user_data()
        perform_calculations()
        display_results()
        response = input("Would you like to place another order? (y/n): ")
        if response.lower() != 'y':
            break

def get_user_data():
    global order_counts, num_drinks, num_breadsticks, num_pizzas, size
    size = input("Enter pizza size (S, M, L, XL): ").lower()
    if size in order_counts:
        order_counts[size] += 1
    else:
        print("Invalid pizza size entered.")
    
    num_pizzas += int(input("How many pizzas do you want? "))  # Ask for the number of pizzas
    num_drinks += int(input("How many drinks do you want? "))
    num_breadsticks += int(input("How many breadsticks do you want? "))

def perform_calculations():
    global subtotal, sales_tax, total, order_counts, num_drinks, num_breadsticks, num_pizzas, subtotal_pizza
    subtotal_pizza = sum(order_counts[size] * PIZZA_PRICES[size] for size in order_counts)
    subtotal = sum(order_counts[size] * PIZZA_PRICES[size] for size in order_counts)
    subtotal += num_drinks * DRINK_PRICE + num_breadsticks * BREADSTICK_PRICE
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('------------------------------')
    print('****** Gaias Pizzeria ******')
    print('Your delicious local pizza place')
    print('-------------------------------')
    print(f"{size.upper()} Pizza   \t$ {subtotal_pizza}")
    print('Drinks       \t$', num_drinks * DRINK_PRICE)
    print('Breadsticks  \t$', num_breadsticks * BREADSTICK_PRICE)
    print('------------------------------')
    print(f'Subtotal     \t${subtotal:,.2f}')
    print(f'Sales Tax    \t${sales_tax:,.2f}')
    print(f'Total        \t${total:,.2f}')
    print('-------------------------------')
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %I:%M %p")
    print(formatted_time)

def display_menu():
    print('''
    ****** Welcome Gaias Pizzeria ******
    ******        Menu            ******
    s: Small \t$9.99
    m: Medium\t$12.99
    l: Large \t$14.99
    xl: Extra-Large \t$17.99

    Drink: \t$3.99
    Breadsticks: \t$6.99
    Sales Tax:\t5.5%
    ''')

if __name__ == "__main__":
    main()
