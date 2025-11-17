import tkinter as tk
from tkinter import messagebox

root = None
subscriptions = []

EXPENSE_THRESHOLD = 80
FAIR_THRESHOLD = 40
CATEGORIES = ["Entertainment", "Car Expenses", "Health Expenses", "Food", "Utilities", "Other"]

input_entry = None
listbox = None
total_label = None
health_label = None
welcome_frame = None
manager_frame = None

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

def update_display():
    listbox.delete(0, tk.END)
    
    if len(subscriptions) == 0:
        listbox.insert(tk.END, "No subscriptions yet")
    else:
        for sub in subscriptions:
            name = sub[0]
            cost = sub[1]
            category = sub[2]
            
            display_text = f"{name:<30} ${cost:.2f}     ({category})"
            listbox.insert(tk.END, display_text)
            
            if cost >= FAIR_THRESHOLD:
                idx = listbox.size() - 1
                listbox.itemconfig(idx, fg='red')
    
    total = calculate_total()
    total_label.config(text=f"Total Monthly Spending: ${total:.2f}")
    
    health_msg, health_color = get_health_score(total)
    health_label.config(text=f"Health Score: {health_msg}", fg=health_color)

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

def show_manager():
    welcome_frame.pack_forget()
    manager_frame.pack(fill=tk.BOTH, expand=True)
    update_display()

def create_welcome_page(parent):
    frame = tk.Frame(parent, bg="#e8f5e9")
    
    tk.Label(frame, text="BudgetBuddy", 
             font=('Arial', 32, 'bold'), 
             fg="#2e7d32",
             bg="#e8f5e9").pack(pady=(120, 20))
    
    tk.Label(frame, text="Subscription Manager", 
             font=('Arial', 18),
             bg="#e8f5e9").pack(pady=10)
    
    tk.Button(frame, text="Get Started", 
              font=('Arial', 16, 'bold'),
              command=show_manager,
              bg="#4CAF50", 
              fg="white", 
              padx=50, 
              pady=20).pack(pady=60)
    
    return frame

def create_manager_page(parent):
    global input_entry, listbox, total_label, health_label
    
    frame = tk.Frame(parent, bg="#f5f5f5", padx=40, pady=40)
    
    tk.Label(frame, text="Subscription Manager", 
             font=('Arial', 28, 'bold'), 
             fg="#1976D2",
             bg="#f5f5f5").pack(pady=(0, 30))
    
    tk.Label(frame, 
             text="Enter: Name, Cost, Category (Example: Netflix, 15.99, Entertainment)", 
             font=('Arial', 11),
             bg="#f5f5f5").pack(pady=(0, 10))
    
    input_entry = tk.Entry(frame, 
                          width=60, 
                          font=('Arial', 16), 
                          relief=tk.SOLID,
                          bg="white",
                          fg="black",
                          insertbackground="black",
                          bd=3)
    input_entry.pack(pady=(0, 15))
    
    tk.Button(frame, 
              text="Add Subscription", 
              command=add_subscription,
              bg="#2196F3", 
              fg="white", 
              font=('Arial', 14, 'bold'), 
              pady=15,
              width=30).pack(pady=(0, 30))
    
    tk.Label(frame, 
             text="Your Subscriptions:", 
             font=('Arial', 14, 'bold'),
             bg="#f5f5f5").pack(pady=(0, 10))
    
    listbox = tk.Listbox(frame, 
                        height=12, 
                        font=('Courier', 12), 
                        bd=3,
                        bg="white",
                        fg="black",
                        relief=tk.SOLID)
    listbox.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
    
    tk.Button(frame, 
              text="Delete Selected", 
              command=delete_subscription,
              bg="#f44336",  
              font=('Arial', 12, 'bold'),
              pady=10,
              width=30).pack(pady=(0, 20))
    
    stats_frame = tk.Frame(frame, bg="white", relief=tk.SOLID, bd=3)
    stats_frame.pack(fill=tk.X, pady=(10, 0))
    
    total_label = tk.Label(stats_frame, 
                          text="Total Monthly Spending: $0.00", 
                          font=('Arial', 16, 'bold'), 
                          bg="white")
    total_label.pack(pady=(15, 5))
    
    health_label = tk.Label(stats_frame, 
                           text="Health Score: N/A", 
                           font=('Arial', 14), 
                           bg="white")
    health_label.pack(pady=(5, 15))
    
    return frame

def start_app():
    global root, welcome_frame, manager_frame
    
    root = tk.Tk()
    root.title("BudgetBuddy")
    root.geometry("850x800")
    
    welcome_frame = create_welcome_page(root)
    manager_frame = create_manager_page(root)
    
    welcome_frame.pack(fill=tk.BOTH, expand=True)
    
    root.mainloop()

if __name__ == "__main__":
    start_app()