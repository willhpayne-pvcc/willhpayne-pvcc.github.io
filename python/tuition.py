# Name: William Payne, Xinnan Wei
# PROG PURP: Computes college tuition & fees based on course credits as of 2024



import datetime

#define rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL = 23.50
RATE_INSTITUTION = 1.75
RATE_ACTIVITY = 2.90

#define global
inout = 1
numcredits = 0
scholarshipamt = 0
tuitionfee = 0
capitalfee = 0
institutionfee = 0
activityfee = 0
totalowed = 0
balance = 0

## Define Functions
def main():
    another_student = True
    while another_student:
        get_user_data()
        perform_calculations()
        display_results()
    yesno = input("\nWould you like to calculate for another student? (Y/N): ")
    if yesno.upper() != "Y":
        another_student = False

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter 1 for IN-STATE; Enter 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered: "))
    scholarshipamt = int(input("Scholarship amount (0 if none): "))

def perform_calculations():
    global tuitionfee, capitalfee, institutionfee, activityfee, totalowed, balance
    if inout == 1:
        tuitionfee = numcredits * RATE_TUITION_IN
        capitalfee = 0
    else:
        tuitionfee = numcredits * RATE_TUITION_OUT
        capitalfee = numcredits * RATE_CAPITAL

    institutionfee = numcredits * RATE_INSTITUTION
    activityfee = numcredits * RATE_ACTIVITY
    totalowed = tuitionfee + capitalfee + institutionfee + activityfee
    balance = totalowed - scholarshipamt

def display_results():
    print('\n-----------------------------------')
    print('Number of credits : ' + str(numcredits))
    print('-------------------------------------')
    print('Tuition           $ ' + format(tuitionfee, '10,.2f'))
    print('Capital           $ ' + format(capitalfee, '10,.2f'))
    print('Institution       $ ' + format(institutionfee, '10,.2f'))
    print('Activity          $ ' + format(activityfee, '10,.2f'))
    print('Total             $ ' + format(totalowed, '10,.2f'))
    print('Scholarship       $ ' + format(scholarshipamt, '10,.2f'))
    print('-------------------------------------')
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %I:%M %p")
    print(formatted_time)
    print("PVCC FEE RATES: https://www.pvcc.edu/tuition-and-fees")

# Execute
main()