class Budget:
    def __init__(self, expense_type):
        self.expense_type = expense_type
        self.categories = [] 
        self.expenses = [] 

    def add_expense(self):
        while True:
            try:
                num_expense_str = input(
                    f"\nEnter number of {self.expense_type} expenses you want to add (integers only): "
                )
                num_expense = int(num_expense_str)
                if num_expense < 0:
                    print("\nError: Number of expenses must be non-negative. Try again!!")
                    continue
                break
            except ValueError:
                print("\nError: Invalid input. Please enter an integer!!")

        for i in range(num_expense):
            while True:
                expense_input = input(f"Enter {self.expense_type} expense #{i+1} (e.g., 'Item 10.50'): ")

                parts = expense_input.split()
                
                if len(parts) != 2:
                    print(
                        "\nError: Input must be in the format 'Type Cost' (e.g., 'Milk 10'). Please try again!!!"
                    )
                    continue

                expense_category = parts[0].split()
                expense_cost_str = parts[1]

                try:
                    expense_cost = float(expense_cost_str)
                    if expense_cost <= 0:
                         print("\nError: Cost must be a positive number. Please try again!!!")
                         continue
                except ValueError:
                    print(
                        f"\nError: '{expense_cost_str}' is not a valid cost. Please enter a number for the cost!!!!"
                    )
                    continue

                self.categories.append(expense_category)
                self.expenses.append(expense_cost)
                break 

    def get_expense_details(self):
        print(f"\n--- {self.expense_type} Expenses Details ---")
        if not self.categories:
            print("\nNo expenses recorded in this category.")
            return

        for category, cost in zip(self.categories, self.expenses):
            print(f"Expense Type: {category}, Cost: ${cost:.2f}")
        
       
    def get_expense(self):
        total = sum(self.expenses)
        print(f"Total money you spend on {self.expense_type} is ${total:.2f}")
        return total
