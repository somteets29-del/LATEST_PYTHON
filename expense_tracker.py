expenses = [
    [1, "05", "Data Subscription", 2500],
    [2, "06", "Lunch", 1200],
    [3, "06", "Transport", 800]
]
def add_expense(month, description, amount):
    new_id = len(expenses) + 1
    expenses.append([new_id, month, description, amount])
    print("\nExpense added Successfully\n")
    return

def view_expenses():
    print("\nAll Expenses:\n")
    for expense in expenses:
        print(f"ID: {expense[0]} | Month: {expense[1]} | Description: {expense[2]} | Amount: ₦{expense[3]}")
    print()
   
def delete_expense(expense_id):
    for expense in expenses:
        if expense[0] == expense_id:
            expenses.remove(expense)
            print("Expense deleted successfully!")
            return

    print("Expense not found")

def update_expense(expense_id, new_description, new_amount):
    for expense in expenses:
        if expense[0] == expense_id:
            expense[2] = new_description
            expense[3] = new_amount
            print("Expense updated successfully!")
            return

    print("Expense not found")
    
def summary_all():
    total = sum([expense[3] for expense in expenses])
    print("Total expenses:", total)

def summary_by_month(month):
    total = sum([expense[3] for expense in expenses if expense[1] == month])
    print(f"Total for month {month}: {total}")
    
while True:
    print("1. View Expenses")
    print("2. Add expenses")
    print("3. Delete Expenses")
    print("4. Update Expenses")
    print("5. View total expenses")
    print("6. Monthly summary")
    print("7. Exit")
    
    choice = int(input("Enter your choice: "))
    print()
    
    if choice  == 1:
        view_expenses()
   
    elif choice == 2:
        month = input("Enter month(digits only): ")
        description = input("Enter description: ")
        amount = int(input("Enter amount: "))
    
        add_expense(month, description, amount)
        
    elif choice == 3:
        expense_id = int(input("Enter expense to delete: "))
        delete_expense(expense_id)
    
    elif choice == 4:
        expense_id = int(input("Enter the expense id that you wish to update: "))
        new_description = input("New descrip: ")
        new_amount = int(input("new amount: "))
        update_expense(expense_id, new_description, new_amount)
        
    elif choice == 5:
        summary_all()

    elif choice == 6:
        month = input("Enter month: ")
        summary_by_month(month)
        
    elif choice == 7:
        print("Thank you for using our services")
        break
        
    else:
        print("Invalid choice!\nTry again")
        