subscriptions = []

EXPENSE_THRESHOLD = 80
FAIR_THRESHOLD = 40
CATEGORIES = ["Entertainment", "Car Expenses", "Health Expenses", "Food", "Utilities", "Other"]

def calculate_total():
    total = 0
    for sub in subscriptions:
        total = total + sub[1]
    return total

def get_health_score(total_cost):
    if total_cost < FAIR_THRESHOLD:
        message = "Excellent spending control!"
        color = "green"
    elif total_cost < EXPENSE_THRESHOLD:
        message = "Fair, but worth reviewing."
        color = "orange"
    else:
        message = "High spending! Consider reviewing subscriptions."
        color = "red"
    return message, color

def add_subscription():
    input_text = input_entry.get().strip()

    if not input_text:
        return

    parts = [p.strip() for p in input_text.split(',')]

    if len(parts) != 3:
        messagebox.showerror("Error", "Must enter: Name, Cost, Category")
        return

    name = parts[0]
    cost_str = parts[1]
    category_input = parts[2]

    if not name:
        messagebox.showerror("Error", "Name cannot be empty")
        return

    try:
        cost = float(cost_str)
        if cost <= 0:
            messagebox.showerror("Error", "Cost must be positive")
            return
    except ValueError:
        messagebox.showerror("Error", "Cost must be a number")
        return

    category_clean = category_input.lower().replace('expenses', '').replace('expense', '').strip()
    valid_category = None

    for cat in CATEGORIES:
        cat_clean = cat.lower().replace(' expenses', '').replace(' expense', '').strip()
        if category_clean == cat_clean:
            valid_category = cat
            break

    if valid_category is None:
        messagebox.showerror("Error", f"Invalid category. Use: {', '.join(CATEGORIES)}")
        return

    new_sub = [name, cost, valid_category]
    subscriptions.append(new_sub)

    input_entry.delete(0, tk.END)
    update_display()

def delete_subscription():
    try:
        selection = listbox.curselection()[0]
        deleted_name = subscriptions[selection][0]
        del subscriptions[selection]
        update_display()
    except IndexError:
        messagebox.showwarning("Warning", "Select a subscription to delete")
