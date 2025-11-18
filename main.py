import tkinter as tk
from tkinter import messagebox, simpledialog

root = None
welcome_frame = None
manager_frame = None

subscriptions = [] 

input_entry = None
category_dropdown = None 
listbox = None
total_label = None
health_label = None

EXPENSE_THRESHOLD = 80
FAIR_THRESHOLD = 40
CATEGORIES = ["Entertainment", "Car Expenses", "Health Expenses", "Food", "Utilities", "Other"]

def calculate_total():
    total = 0
    for sub in subscriptions:
        total += sub[1]
    return total

def calculate_all_time_costs():
    total_monthly = calculate_total()
    
    total_yearly = total_monthly * 12
    total_weekly = total_monthly / 4.345
    
    return total_weekly, total_monthly, total_yearly

def get_health_score(total_cost):
    if total_cost < FAIR_THRESHOLD:
        message = "Excellent spending control!"
        color = "light green"
    elif total_cost < EXPENSE_THRESHOLD:
        message = "Fair, but worth reviewing."
        color = "yellow"
    else:
        message = "High spending! Consider reviewing subscriptions."
        color = "red"
    return message, color

def update_display():
    global total_label, health_label
    
    listbox.delete(0, tk.END)
    
    total = calculate_total()
    
    if not subscriptions:
        listbox.insert(tk.END, "No subscriptions yet")
    else:
        sorted_subs = sorted(subscriptions, key=lambda x: x[2]) 
        
        for i, sub in enumerate(sorted_subs):
            name = sub[0]
            cost = sub[1]
            category = sub[2]
            
            display_text = f"{name:<30} ${cost:8.2f}     ({category})"
            listbox.insert(tk.END, display_text)
            
            if cost >= FAIR_THRESHOLD:
                listbox_index = listbox.size() - 1 
                listbox.itemconfig(listbox_index, {'fg': 'red'})
    
    total_label.config(text=f"Total Monthly Spending: ${total:.2f}")
    
    health_msg, health_color = get_health_score(total)
    health_label.config(text=f"Health Score: {health_msg}", fg=health_color)

def add_subscription():
    input_text = input_entry.get().strip()
    selected_category = category_dropdown.get()
    
    parts = [p.strip() for p in input_text.split(',')]
    
    if len(parts) != 2:
        messagebox.showerror("Error", "Input must be: Name, Cost (e.g., Netflix, 15.99)")
        return
    
    name = parts[0]
    cost_str = parts[1]
    
    if not name:
        messagebox.showerror("Error", "Name cannot be empty")
        return
    
    try:
        cost = float(cost_str)
        if cost <= 0:
            messagebox.showerror("Error", "Cost must be positive")
            return
    except ValueError:
        messagebox.showerror("Error", "Cost must be a number (e.g., 15.99)")
        return
    
    if selected_category not in CATEGORIES:
         messagebox.showerror("Error", "Please select a valid category from the dropdown.")
         return
    
    new_sub = [name, cost, selected_category]
    subscriptions.append(new_sub)
    
    input_entry.delete(0, tk.END)
    update_display()

def delete_subscription():
    try:
        selection_index = listbox.curselection()[0]
        
        selected_display_text = listbox.get(selection_index)
        
        selected_name = selected_display_text.split('$')[0].strip()
        
        for i, sub in enumerate(subscriptions):
            if sub[0] == selected_name:
                del subscriptions[i]
                break
        
        update_display()

    except IndexError:
        messagebox.showwarning("Warning", "Select a subscription to delete.")
    except Exception:
         pass

def show_cost_summary():
    if not subscriptions:
        messagebox.showwarning("Warning", "No subscriptions added yet to calculate a summary.")
        return
        
    weekly, monthly, yearly = calculate_all_time_costs()
    
    summary_text = (
        f"--- Total Subscription Costs ---\n\n"
        f"Monthly Total: ${monthly:.2f}\n"
        f"Yearly Total:  ${yearly:.2f}\n"
        f"Weekly Average: ${weekly:.2f}\n\n"
        f"These figures are calculated based on all currently listed subscriptions."
    )
    
    messagebox.showinfo("Cost Summary", summary_text)

def show_manager():
    global welcome_frame, manager_frame
    
    welcome_frame.pack_forget()
    manager_frame.pack(fill=tk.BOTH, expand=True)
    update_display()

def create_welcome_page(parent):
    frame = tk.Frame(parent, bg="#e8f5e9") 
    
    tk.Label(frame, 
             text="BudgetBuddy", 
             font=('Arial', 32, 'bold'), 
             fg="#2e7d32", 
             bg="#e8f5e9").pack(pady=(120, 20))
    
    tk.Label(frame, 
             text="Your Monthly Subscription Manager", 
             font=('Arial', 18),
             fg="#4CAF50", 
             bg="#e8f5e9").pack(pady=10)
    
    tk.Button(frame, 
              text="Get Started", 
              font=('Arial', 16, 'bold'),
              command=show_manager, 
              bg="#4CAF50", 
              fg="white", 
              padx=50, 
              pady=20,
              relief=tk.RAISED,
              bd=4).pack(pady=60)
    
    return frame

def create_manager_page(parent):
    global input_entry, category_dropdown, listbox, total_label, health_label
    
    # NEW: Frame background set to deep navy blue for maximum contrast
    frame_bg = "#1F618D" 
    frame = tk.Frame(parent, bg=frame_bg, padx=40, pady=40) 
    
    tk.Label(frame, 
             text="Subscription Manager", 
             font=('Arial', 28, 'bold'), 
             fg="#F0F8FF", # Lightest blue/white for text on dark background
             bg=frame_bg).pack(pady=(0, 30))
    
    input_frame = tk.Frame(frame, bg=frame_bg)
    input_frame.pack(fill=tk.X, pady=(0, 10))

    tk.Label(input_frame, 
             text="Service (Name, Cost):", 
             font=('Arial', 11),
             fg="#FFFFFF", # White text on dark background
             bg=frame_bg).pack(side=tk.LEFT, padx=(0, 10))
    
    # NEW: Entry background is pure white (#FFFFFF)
    input_entry = tk.Entry(input_frame, 
                          width=30, 
                          font=('Arial', 14), 
                          relief=tk.SOLID,
                          bg="#FFFFFF", 
                          fg="black", 
                          insertbackground="black", 
                          bd=3) # Increased border for better definition
    input_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
    
    tk.Label(input_frame, 
             text="Category:", 
             font=('Arial', 11),
             fg="#FFFFFF", # White text on dark background
             bg=frame_bg).pack(side=tk.LEFT, padx=(20, 5))
             
    category_dropdown_var = tk.StringVar(frame)
    category_dropdown_var.set(CATEGORIES[0]) 
    category_dropdown = category_dropdown_var
    
    category_menu = tk.OptionMenu(input_frame, category_dropdown_var, *CATEGORIES)
    category_menu.config(font=('Arial', 12), bg="white", relief=tk.FLAT)
    category_menu["menu"].config(font=('Arial', 12))
    category_menu.pack(side=tk.LEFT)

    
    tk.Button(frame, 
              text="Add Subscription", 
              command=add_subscription,
              bg="#2196F3", 
              fg="white", 
              font=('Arial', 14, 'bold'), 
              pady=10,
              width=40,
              relief=tk.RAISED,
              bd=4).pack(pady=(15, 20))
    
    tk.Label(frame, 
             text="Your Subscriptions (Sorted by Category):", 
             font=('Arial', 14, 'bold'),
             fg="#FFFFFF", # White text on dark background
             bg=frame_bg).pack(pady=(0, 10))
    
    listbox = tk.Listbox(frame, 
                        height=12, 
                        font=('Courier', 12), 
                        bd=3,
                        bg="#fafafa", 
                        fg="black",
                        relief=tk.SUNKEN,
                        selectmode=tk.SINGLE) 
    listbox.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
    
    action_frame = tk.Frame(frame, bg=frame_bg)
    action_frame.pack(fill=tk.X, pady=(0, 20))
    
    tk.Button(action_frame, 
              text="Delete Selected", 
              command=delete_subscription,
              bg="#f44336",  
              fg="white", 
              font=('Arial', 12, 'bold'),
              pady=10,
              width=25,
              relief=tk.RAISED,
              bd=4).pack(side=tk.LEFT, expand=True, padx=10)
              
    tk.Button(action_frame, 
              text="Show Cost Summary (W/M/Y)", 
              command=show_cost_summary,
              bg="#FFC107",  
              fg="black", 
              font=('Arial', 12, 'bold'),
              pady=10,
              width=25,
              relief=tk.RAISED,
              bd=4).pack(side=tk.RIGHT, expand=True, padx=10)
    
    # Stats frame kept white for contrast against the listbox and for better readability of score colors
    stats_frame = tk.Frame(frame, bg="#ffffff", relief=tk.FLAT, bd=3, highlightbackground="#ccc", highlightthickness=1)
    stats_frame.pack(fill=tk.X, pady=(10, 0))
    
    total_label = tk.Label(stats_frame, 
                          text="Total Monthly Spending: $0.00", 
                          font=('Arial', 16, 'bold'), 
                          bg="#ffffff")
    total_label.pack(pady=(15, 5))
    
    health_label = tk.Label(stats_frame, 
                           text="Health Score: N/A", 
                           font=('Arial', 14), 
                           bg="#ffffff")
    health_label.pack(pady=(5, 15))
    
    return frame

def start_app():
    global root, welcome_frame, manager_frame
    
    root = tk.Tk()
    root.title("BudgetBuddy - Subscription Manager")
    root.geometry("850x850") 
    
    welcome_frame = create_welcome_page(root)
    manager_frame = create_manager_page(root)
    
    welcome_frame.pack(fill=tk.BOTH, expand=True)
    
    root.mainloop()

if __name__ == "__main__":
    start_app()
