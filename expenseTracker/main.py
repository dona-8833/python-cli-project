import json
# creating the json file
def writer(expense):
        with open("exp.json","w") as file:
            json.dump(expense,file,indent=4)
# getting data from file
def reader():
    try:
        with open("exp.json","r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError,json.JSONDecodeError):
        return []
# adding the expense
def addExpense():
    print(f'''
========================
    Add Expenses
========================
''')
    while True:
        amount_input = input("Enter the amount or 'q' to quit: ").strip()
        if amount_input.lower() == "q":
            print("Expense cancelled.")
            return
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Amount should be a number.")

    while True :
        category = input("Enter the category or 'q' to quit: ").strip()
        if category.lower() == "q":
            print("Expense cancelled.")
            return
        elif category == "":
            print("category can not be empty")
        else:
            break

    while True:
        description = input("Enter the description or 'q' to quit: ").strip()
        if description.lower() == "q":
            print("Expense cancelled.")
            return
        elif description == "":
            print("Description can not be empty")
        else:
            break

    prev_expense = reader()
    expense = {
        "id":max(expense["id"] for expense in prev_expense) + 1,
        "amount":amount,
        "category":category,
        "description":description
    }
    prev_expense.append(expense)
    writer(prev_expense)
    print(f"Expense {max(expense["id"] for expense in prev_expense) + 1} successfully added")
# continue or exit
def continue_or_exit():
    while True:
        choice = input("Do you want to continue? (y/n): ").strip().lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Please enter y or n")
# view all expenses
def view_expenses():
    expenses = reader()
    print(f'''
========================
    All Expenses
========================
''')
    check_expense(expenses)
    for expense in expenses:
        print(f"Amount: {expense["amount"]}")
        print(f"Category: {expense["category"]}")
        print(f"Description: {expense["description"]}\n")
# Total expenses
def total_spending():
    print(f'''
========================
    Total Expenses
========================
''')
    expenses = reader()
    check_expense(expenses)
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Expenses: {total}")
# Total by category 
def Total_category():
    expenses = reader()
    if len(expenses) < 1:
        check_expense(expenses)
        return
    categories = []
    for expense in expenses:
        categories.append(expense["category"])
    while True:
        userInput = input("Type the category or * to get for all of (e) to exit ").strip().lower()
        if userInput == "e":
            return
        elif userInput == "*":
            for category in set(categories):
                total = 0
                for expense in expenses:
                    if category == expense["category"]:
                        total += expense["amount"]
                print(f"{category}: {total}" )
        elif userInput not in categories:
            print("\nInvalid category ")
            print("Available categories:")
            for category in set(categories): 
                print(category)
        elif userInput in categories:
            total = 0
            for expense in expenses:
                if userInput == expense["category"]:
                    total+= expense["amount"]
            print(f"{userInput} :{total}")
# Edit Expense
def edit_expense():
    expenses = reader()
    if len(expenses) < 1:
        check_expense(expenses)
        return
    id = []
    for expense in expenses:
        id.append(expense["id"])
        print(f"{expense["id"]}-amount: {expense["amount"]} category: {expense["category"]} description: {expense["description"]}")
    while True:
        userInput = input("select the expense you want to edit or (e) to exit ").strip().lower()
        if userInput == "e":
            return
        try:
            userInput = int(userInput)
        except ValueError:
            print("Please enter a number or 'e'.")
            continue
        if userInput not in id:
            print("select from the above id")
            edit_expense()
            return
        while True:
            amount_input = input("Enter the amount or 'q' to quit: ").strip()
            if amount_input.lower() == "q":
                print("Edit cancelled.")
                return
            elif amount_input == "":
                amount = ""
                break
            try:
                amount = float(amount_input)
                break
            except ValueError:
                print("Amount should be a number.")

        while True :
            category = input("Enter the category or 'q' to quit: ").strip()
            if category.lower() == "q":
                print("Edit cancelled.")
                return
            else:
                break

        while True:
            description = input("Enter the description or 'q' to quit: ").strip()
            if description.lower() == "q":
                print("Edit cancelled.")
                return
            else:
                break

        for expense in expenses:
            if userInput == expense["id"]:
                if amount == "":
                    expense["amount"] = expense["amount"]
                else :
                    expense["amount"] = amount
                if category == "":
                    expense["category"] = expense["category"]
                else:
                    expense["category"] = category
                if description == "":
                    expense["description"] = expense["description"]
                else:
                    expense["description"] = description
        
        writer(expenses)
        print(f"Expense {userInput} Successfully edited")
        break
# delete Expense
def delete_expense():
    expenses = reader()
    if len(expenses) < 1:
        check_expense(expenses)
        return
    id = []
    print(f"{"ID":5} {"Category":25} {"Description":30} {"Amount":20}")
    for expense in expenses:
        id.append(expense["id"])
        amount = expense["amount"]
        ids = str(expense["id"])

        print(f"{ids:5} {expense["category"]:25} {expense["description"]:30} {amount:25,.2f}")
    while True:
        userInput = input("enter the value you want to delete of (q) to quit ")
        if userInput == "q":
            return
        try:
            userInput = int(userInput)
        except ValueError:
            print("Please enter a number or 'e'.")
            continue
        if userInput not in id:
            print("select from the above id")
            delete_expense()
            return
        for index,expense in enumerate(expenses):
            if userInput == expense["id"]:
                del expenses[index]
                writer(expenses)
                return
# check expense
def check_expense(exp):
    if len(exp) < 1:
        print("You have no expense")
# single filter
def single_filter(expenses, filter_type, user_input):
    if filter_type == "category":
        categories = {expense["category"] for expense in expenses}
        if user_input not in categories:
            print("Invalid category name")
            print("Available categories:")
            for category in categories:
                print(category)
            return
        total = 0
        for expense in expenses:
            if user_input == expense["category"]:
                total += expense["amount"]
                print(f"amount: {expense['amount']}")
                print(f"category: {expense['category']}")
                print(f"description: {expense['description']}\n")
        print(f"Total: {total}")
    elif filter_type == "amount":
        amount = user_input.split("-")
        if len(amount) == 1:
            total = 0
            for expense in expenses:
                if float(amount[0]) == expense["amount"]:
                    total += expense["amount"]
                    print(f"amount: {expense['amount']}")
                    print(f"category: {expense['category']}")
                    print(f"description: {expense['description']}\n")
            print(f"Total: {total}")
        elif len(amount) == 2:
            total = 0
            minimum = float(amount[0])
            maximum = float(amount[1])
            for expense in expenses:
                if minimum <= expense["amount"] <= maximum:
                    total += expense["amount"]
                    print(f"amount: {expense['amount']}")
                    print(f"category: {expense['category']}")
                    print(f"description: {expense['description']}\n")
            print(f"Total: {total}")
        else:
            print("Invalid amount input")
# filter expense
def multiple_filter(expenses,amount,category):
        filter_amount = amount.split("-")
        if len(filter_amount) == 1:
            try:
                filter_amount = float(filter_amount[0])
            except ValueError:
                print("the amount should be a number")
                return
            total = 0
            for expense in expenses :
                if expense["category"] == category and expense["amount"] == filter_amount:
                    total += expense["amount"]
                    print(f"amount: {expense['amount']}")
                    print(f"category: {expense['category']}")
                    print(f"description: {expense['description']}\n")
            if total < 1:
                print("Avaibale amounts and categories")
                print({expense["category"] for expense in expenses})
                print({expense["amount"] for expense in expenses})
            print(f"Total: {total}")
        elif len(filter_amount) == 2:
            try:
                minimum = float(filter_amount[0])
                maximum = float(filter_amount[1])
            except ValueError:
                print("the amount should be a range of number")
                return
            total = 0
            for expense in expenses:
                if expense["category"] == category and minimum <= expense["amount"] <= maximum:
                    total += expense["amount"]
                    print(f"\namount: {expense['amount']}")
                    print(f"category: {expense['category']}")
                    print(f"description: {expense['description']}\n")
            print(f"Total: {total}")
        else:
            print("invalid input format") 
# filter expense
def filter_expense():
    expenses = reader()
    if len(expenses) < 1:
        check_expense(expenses)
        return
    while True:
        print(f'''
=======================
    Select Filter
=======================

[1] single filter 
[2] multiple filter
''')
        userInput = input("Select from the option above or (q) to quit: ").strip().lower()
        if userInput == "q":
            return
        try: 
            userInput = int(userInput)
        except ValueError:
            print("your input must be between the above list")
            continue
        if userInput == 1:
            print(f'''
=======================
    Single Filter
=======================

[1] category filter 
[2] amount filter
''')
            userInput = input("Select from the option above or (q) to quit: ").strip().lower()
            if userInput == "q":
                return
            try:
                userInput = int(userInput)
            except ValueError:
                print("your input must be between the above list")
                continue
            if userInput == 1 :
                category_input = input("enter the category name or (q) to quit:").strip().lower()
                if category_input == "q":
                    return
                if category_input.isalpha():
                    single_filter(expenses,"category",category_input)
                    break
                else:
                    print("invalid category name")
                    continue
            elif userInput == 2:
                amount_input = input("enter the amount you want to filter or (q) to quit:").strip().lower()
                if amount_input == "q":
                    return
                single_filter(expenses,"amount",amount_input)
                break
        elif userInput == 2:
            print(f'''
=======================
    Multiple  Filter
=======================

[1] amount and category
''')
            userInput = input("Select from the option above or (q) to quit: ").strip().lower()
            if userInput == "q":
                return
            try:
                userInput = int(userInput)
            except ValueError:
                print("your input must be between the above list")
                continue
            if userInput == 1 :
                print("usage!!")
                print("amount,category")
                print("500,food")
                print("600-1000,oil")
                try:
                    multiple_filter_amount,multiple_filter_category = list(input("Enter the key you want to filter with").split(","))
                    multiple_filter(expenses,multiple_filter_amount,multiple_filter_category)
                    return
                except ValueError:
                    print("expected 2 values got 1")
                    return
            else:
                print("invalid list number")
# main
def main():
    while True:
        print(
'''
========================
    Expense Tracker
========================
[1] Add an expense
[2] View all expenses
[3] Calculate total spending
[4] Calculate spending by category
[5] Edit
[6] Delete an expense
[7] Filter 
[8] Exit

'''
        )

        try:
            userInput = int(input("Select an option: "))

        except ValueError:
            print("\nPlease enter a number.")
            continue
        if userInput == 8:
            return
        elif userInput == 1:
            addExpense()
        elif userInput == 2:
            view_expenses()
        elif userInput == 3:
            total_spending()
        elif userInput == 4:
            Total_category()
        elif userInput == 5:
            edit_expense()
        elif userInput == 6:
            delete_expense()
        elif userInput == 7:
            filter_expense()
        else:
            print("select from the listed options")

        if not continue_or_exit():
            print("Goodbye!")
            return

if __name__ == "__main__":
    main()