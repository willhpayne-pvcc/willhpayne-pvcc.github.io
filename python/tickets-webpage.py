# Name: William Payne
# Prog Purpose: This program finds the cost of movie tickets, popcorn, & drinks
#   The output is sent to an .html file

import datetime

##############  define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .055
PRICE_TICKET = 10.99
PRICE_POPCORN = 12.99
PRICE_DRINK = 3.99

# define global variables
num_tickets = 0
num_popcorn = 0
num_drinks = 0

cost_tickets = 0
cost_popcorn = 0
cost_drinks = 0

subtotal = 0
sales_tax = 0
total = 0

# create output file
outfile = 'tickets-receipt.html'

##############  define program functions ################
def main():
    
    open_outfile()
    more = True
    
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        
        askAgain = input('\nWould you like to buy more tickets (Y or N)? ' )
        if askAgain.upper() == 'N':
            more = False
            f.write('</body></html>')
            f.close()
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            
def get_user_data():
    global num_tickets,num_popcorn, num_drinks
    num_tickets = int(input('Number of movie tickets: '))
    num_popcorn = int(input('Number of buckets of popcorn: '))
    num_drinks =  int(input('Number of drinks: '))    

def perform_calculations():
    global cost_tickets, cost_popcorn, cost_drinks, subtotal, sales_tax, total
    cost_tickets = num_tickets * PRICE_TICKET
    cost_popcorn= num_popcorn * PRICE_POPCORN
    cost_drinks = num_drinks * PRICE_DRINK

    subtotal = cost_tickets + cost_popcorn + cost_drinks
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax
            
def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('''
            <html>
            <head>
            <title>Cinema House Movies </title>
            <style>
                body {background-color: #985b45; background-image: url(wp-cinema.png); color: #f8dd61;}
                td {text-align: right; font-family: courier;}
            </style>
            </head>
            <body>
            ''')
    
def display_results():
    global f
    currency = '8,.2f'
    dt_full = str(datetime.datetime.now())
    dt_short = dt_full[0:16]

    startrow = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    f.write('''
            <table border=1 style ="background-color:#47161a;font-family: arial; margin: auto;">
            <tr><td colspan = 2>
            <h1 style = "text-align: center;" >CINEMA HOUSE MOVIES</h1></td></tr>
            <tr><td colspan = 2">
            *** Your Neighborhood Movie House ***
            <tr><td colspan = 2">Date/Time:
            ''')
    
    f.write(dt_short)
    f.write(endtr)
    f.write(startrow + 'Tickets'   + endtd + "$" + format(cost_tickets,currency) + endtr)
    f.write(startrow + 'Popcorn'   + endtd + "$" + format(cost_popcorn,currency) + endtr)
    f.write(startrow + 'Drinks'    + endtd + "$" + format(cost_drinks,currency)  + endtr)
    f.write(startrow + 'Subtotal'  + endtd + "$" + format(subtotal,currency)     + endtr)
    f.write(startrow + 'Sales Tax' + endtd + "$" + format(sales_tax,currency)    + endtr)
    f.write(startrow + 'TOTAL'     + endtd + "$" + format(total,currency)        + endtr)
    f.write('</table><br />')

############ Call on Prog to Do thing ###################
main()