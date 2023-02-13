import csv


# function to create csv header
def createHeader():
    fieldnames = ["amount", "date", "category", "description"]
    # creating csv header row
    with open("money.csv", "w", newline="", encoding="utf-8") as CREATE_CSV:
        writer = csv.DictWriter(CREATE_CSV, fieldnames=fieldnames)
        writer.writeheader()


# function to create the csv file
def create_headerRow():
    # checking if csv header row file already exist
    with open("money.csv", "a", newline="", encoding="utf-8"):
        with open("money.csv", "r", newline="", encoding="utf-8") as READ_CSV:
            fieldnames = ["amount", "date", "category", "description"]
            reader = csv.reader(READ_CSV)
            read_list = []
            for i in reader:
                read_list.append(i)
    # if read_list is empty
    if read_list == []:
        createHeader()

    # creating csv header if its not exist
    elif read_list[0] != fieldnames:
        createHeader()


# function to add money
def addMoney():
    with open("money.csv", "a", newline="", encoding="utf-8") as ADD_CSV:
        writer = csv.writer(ADD_CSV)
        writer.writerow(add_list)


# function to view expenses
def viewExpenses():
    with open("money.csv", "r", newline="", encoding="utf-8") as VIEW_EXPENSES:
        reader = csv.reader(VIEW_EXPENSES)
        for i in reader:
            print(i[0], i[1], i[2], i[3])


my_choice = int(input("Menu:\n1. Add Expenses\n2. View Expenses\n>> "))

if my_choice == 1:
    create_headerRow()

    # getting the amount, date, category, description
    add_amount = int(input("Amount you want to add:\n>> "))
    add_date = input("Date you want to add:\n>> ")
    add_category = input("Category you want to add:\n>> ")
    add_description = input("Description you want to add:\n>> ")
    # list for adding row
    add_list = [add_amount, add_date, add_category, add_description]

    # calling the required functions
    addMoney()
elif my_choice == 2:
    viewExpenses()
