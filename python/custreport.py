# William Payne
# Prog Purpose: Read in a list of customers and display a report that will
#   increase the amount they own by 10% if payment is late
#   DATA FILE is .csv (comma separated values)
#      Four data fields: last nam, first name, amount owed, days payment is late

infile = "customer_data_file.csv"

cust_in_data_block_list = []
cust = []

LATE_FEE_RATE = .10
grand_total = 0


def main():
    read_in_cust_file()
    perform_calculations()
    display_cust_report()

def read_in_cust_file():
    cust_data_file = open(infile, "r")
    
    #read ALL lines in the file into one big list
    cust_in_data_block_list = cust_data_file.readlines()
    cust_data_file.close()

    #split the data into the fields
    for i in cust_in_data_block_list:
        cust.append(i.split(","))


def perform_calculations():
    global grand_total
    
    for i in range(len(cust)):
        amt_owed = float(cust[i][2])
        days_late = int(cust[i][3])
        
        if days_late > 0:
            late_fee = amt_owed * LATE_FEE_RATE
        else:
            late_fee = 0
        
        amt_owed += late_fee
        grand_total += amt_owed
        cust[i][2] = amt_owed

def display_cust_report():

    currency = "8,.2f"
    line = "-----------------------------------"
    tab = "\t"

    print(line)
    print("***** CUSTOMER BALANCE REPORT *****")
    print(" NAME               NEW AMOUNT OWED")
    print(line)

    for i in range(len(cust)):
        print(cust[i][1] + "  " + tab + cust[i][0] + tab + format(cust[i][2],currency))

    print(line)
    print("**** GRAND TOTAL:\t$" + format(grand_total, currency))

main()