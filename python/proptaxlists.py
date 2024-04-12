# Name: William Payne
# Prog Purpose: This program uses lists to find the personal property tax for vehicles in Charlottesvile
#   and produces a refort which displays all data and the total tax due
#
# Peronsal Property tax in Charlottesville:
#       -- $4.20 per $100 of the vehicle value (4.20% per year)
#       -- Paid every six months
# Personal Property Tax Relief (PPTR):
#       -- Eligibility: Owned or leased vehicles which are predominantly used for non-business purposes & have passenger license plates
#       -- Tax relief for qualified vehicles is 33%

import datetime

######################### Define tax rate ###################################
PPT_RATE = 0.042
RELIEF_RATE = 0.33

######################### Create list data ##################################
vehicle = [
    "2019 Volvo",
    "2018 Toyota",
    "2022 Kia",
    "2020 Ford",
    "2023 Honda",
    "2019 Lexus",
    "2010 Kia",
    "2024 Ford"
]

vehicle_value = [13000, 10200, 17000, 21000, 28000, 16700, 7600, 190000]

pptr_eligible = ["Y", "Y", "N", "Y", "N", "Y", "Y", "N"]

owner_name = [
    "Brand, Debra",
    "Smith, Carter",
    "Johnson, Bradley",
    "Garcia, Jennifer",
    "Henderson, Leticia",
    "White, Danielle",
    "Amber Steger",
    "Paige Wright"
]

ppt_owned = []
total = 0

######################### Define program functions ###########################

def main():
    perform_calculations()
    display_results()

def perform_calculations():
    global total

    for i in range(len(vehicle)):
        tax_due = (vehicle_value[i] * PPT_RATE) / 2

        if pptr_eligible[i] == "Y":
            tax_due *= (1 - RELIEF_RATE)

        ppt_owned.append(tax_due)
        total += tax_due

def display_results():
    line = "-----------------------------------------------------------"
    tab = "\t"
    dt_full = datetime.datetime.now()
    dt_short = dt_full.strftime("%Y-%m-%d %H:%M")

    print(line)
    print("*************** PERSONAL PROPERTY TAX REPORT ***************")
    print("                 Charlottesville, Virginia")
    print(f"RUN DATE/TIME: {dt_short}")
    print("\nName" + tab + "Vehicle" + tab + "Value" + tab + "Relief" + tab + "TAX DUE")
    print(line)

    for i in range(len(vehicle)):
        # Displaying information in a formatted way
        print(f"{owner_name[i]}{tab}{vehicle[i]}{tab}${vehicle_value[i]:,.2f}{tab}{pptr_eligible[i]}{tab}${ppt_owned[i]:,.2f}")

    print(line)
    print(f"************************************** TOTAL TAX DUE: {tab}${total:,.2f}")

# Run the main function
main()
