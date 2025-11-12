import os
from Library.classes_9 import Budget


def calc_balance(income, total_expense):
    return income - total_expense

def financial_status(balance):
    print(f"\n--- Financial Status ---")
    if balance > 0:
        print(f"Let's GOOO! Your remaining balance is ${balance:.2f}. You're in good shape.\n")
    elif balance < 0:
        print(f"\n!!Warning!! Your current deficit is ${abs(balance):.2f}. Consider reducing spending!")
    else:
        print("You broke even this month. Keep a close eye on your spending!!!!!!!")



name = input("\n What is your name? ")
while not name: 
    print(f"Name cannot be empty")
    name = input("\n What is your name? ")
os.system('cls' if os.name == 'nt' else 'clear')

print(f"Hey {name}, this is BudgetBuddy! Your personal Budgeting Assistant")

while True:
    try:
        income = float(input("\n What is your monthly income (Numbers only please): "))
        if income < 0:
            print("Income must be non-negative. Please try again!!")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number for your income!!")


total_expense_list = []


grocery = Budget("Grocery")
car = Budget("Car")


grocery.add_expense()
car.add_expense()


grocery.get_expense_details()
car.get_expense_details()


total_grocery = grocery.get_expense()
total_car = car.get_expense()

total_expense_list.append(total_grocery)
total_expense_list.append(total_car) 

total_expenses_sum = sum(total_expense_list) 

print(f"\nYour total combined expenses are: ${total_expenses_sum:.2f}")


bal = calc_balance(income, total_expenses_sum)

financial_status(bal)
