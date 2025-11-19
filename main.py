import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = None
welcome_frame = None
manager_frame = None

subscriptions = [] 

input_entry = None
category_dropdown = None 
listbox = None
total_label = None
health_label = None
chart_frame = None

CATEGORIES = ["Entertainment", "Car Expenses", "Health Expenses", "Food", "Utilities", "Other"]



def calculate_total():
    return sum(sub[1] for sub in subscriptions)

def calculate_all_time_costs():
    monthly = calculate_total()
    return monthly / 4.345, monthly, monthly * 12

def get_health_score(total_cost):
    if total_cost < 40:
        return "Excellent spending control!", "#2ECC71"
    elif total_cost < 80:
        return "Fair, but review spending." , "#F1C40F"
    else:
        return "High spending! Consider reviewing subscriptions.", "#E74C3C"



def update_chart():
    global chart_frame

    for widget in chart_frame.winfo_children():
        widget.destroy()

    if not subscriptions:
        return

    names = [sub[0] for sub in subscriptions]
    costs = [sub[1] for sub in subscriptions]
    categories = [sub[2] for sub in subscriptions]

    category_colors = {
        "Entertainment": "#4CAF50",
        "Car Expenses": "#3498DB",
        "Health Expenses": "#E91E63",
        "Food": "#F39C12",
        "Utilities": "#9B59B6",
        "Other": "#95A5A6"
    }

    bar_colors = [category_colors.get(c, "#95A5A6") for c in categories]

    fig = Figure(figsize=(6.5, 3.5), dpi=100)
    ax = fig.add_subplot(111)

    fig.patch.set_facecolor("#161B22")
    ax.set_facecolor("#161B22")

    bars = ax.bar(names, costs, color=bar_colors)

    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h + 1,
                f"${h:.2f}",
                ha="center", va="bottom",
                fontsize=10, color="#FFFFFF", fontweight="bold")

    ax.set_title("Subscription Costs (Monthly)", color="#FFFFFF", fontsize=12)
    ax.set_ylabel("Cost ($)", color="#FFFFFF")
    ax.set_xlabel("Subscriptions", color="#FFFFFF")

    ax.tick_params(axis="x", labelrotation=30, labelsize=9, colors="#FFFFFF")
    ax.tick_params(axis="y", colors="#FFFFFF")

    fig.subplots_adjust(bottom=0.30, right=0.80)

    for cat, col in category_colors.items():
        ax.bar(0, 0, color=col, label=cat)

    ax.legend(
        bbox_to_anchor=(1.02, 0.5),
        loc='center left',
        frameon=True,
        facecolor="#161B22",
        edgecolor="#2D333B",
        labelcolor="#FFFFFF",
        title="Categories",
        title_fontsize=10
    )

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)



def update_display():
    global total_label, health_label

    listbox.delete(0, tk.END)

    if not subscriptions:
        listbox.insert(tk.END, "No subscriptions yet")
    else:
        sorted_subs = sorted(subscriptions, key=lambda s: s[2])
        for name, cost, category in sorted_subs:
            text = f"{name:<30} ${cost:8.2f}   ({category})"
            listbox.insert(tk.END, text)

            idx = listbox.size() - 1
            if cost > 20:
                listbox.itemconfig(idx, {'fg': '#E74C3C'})
            else:
                listbox.itemconfig(idx, {'fg': '#FFFFFF'})

    total = calculate_total()
    total_label.config(text=f"Total Monthly Spending: ${total:.2f}")

    msg, col = get_health_score(total)
    health_label.config(text=f"Health Score: {msg}", fg=col)

    update_chart()




def add_subscription():
    entry = input_entry.get().strip()
    parts = [p.strip() for p in entry.split(',')]

    if len(parts) != 2:
        messagebox.showerror("Error", "Input must be: Name, Cost")
        return

    name, cost_str = parts
    try:
        cost = float(cost_str)
    except:
        messagebox.showerror("Error", "Cost must be a number.")
        return

    category = category_dropdown.get()

    subscriptions.append([name, cost, category])
    input_entry.delete(0, tk.END)
    update_display()

def delete_subscription():
    try:
        idx = listbox.curselection()[0]
        name = listbox.get(idx).split('$')[0].strip()

        for i, sub in enumerate(subscriptions):
            if sub[0] == name:
                del subscriptions[i]
                break

        update_display()
    except:
        messagebox.showwarning("Warning", "Select a subscription to delete.")


def show_cost_summary():
    if not subscriptions:
        messagebox.showwarning("Warning", "No subscriptions yet.")
        return

    w, m, y = calculate_all_time_costs()

    messagebox.showinfo(
        "Cost Summary",
        f"Monthly: ${m:.2f}\nYearly: ${y:.2f}\nWeekly: ${w:.2f}"
    )




def create_welcome_page(parent):
    bg_main = "#0D1117"
    card_bg = "#161B22"
    border = "#2D333B"
    text = "#E6EDF3"
    text_faint = "#A5ABB3"
    blue = "#2385F5"

    frame = tk.Frame(parent, bg=bg_main)

    card = tk.Frame(frame, bg=card_bg,
                    padx=50, pady=50,
                    highlightbackground=border,
                    highlightthickness=1)
    card.pack(expand=True, pady=100)

    tk.Label(card, text="Financial Manager",
             font=("Arial", 36, "bold"),
             fg=text, bg=card_bg).pack(pady=(0, 10))

    tk.Label(card, text="Your Monthly Subscription Manager",
             font=("Arial", 16),
             fg=text_faint, bg=card_bg).pack(pady=(0, 30))

    tk.Button(
        card, text="Get Started", command=show_manager,
        bg="white", fg="black", font=("Arial", 16, "bold"),
        padx=40, pady=12, relief=tk.FLAT, bd=0,
        activebackground="#DDDDDD" 
    ).pack()

    return frame



def create_manager_page(parent):
    global input_entry, category_dropdown, listbox, total_label, health_label, chart_frame

    bg_main = "#0D1117"
    card_bg = "#161B22"
    border = "#2D333B"
    text = "#E6EDF3"
    text_faint = "#A5ABB3"
    blue = "#2385F5"

    frame = tk.Frame(parent, bg=bg_main, padx=20, pady=20)

    tk.Label(frame, text="Financial Buddy",
             font=("Arial", 30, "bold"),
             fg=text, bg=bg_main).pack(anchor="w", pady=(0, 15))

  
    top = tk.Frame(frame, bg=card_bg,
                   highlightbackground=border,
                   highlightthickness=1,
                   padx=20, pady=20)
    top.pack(fill=tk.X, pady=(0, 15))

    in_row = tk.Frame(top, bg=card_bg)
    in_row.pack(fill=tk.X, pady=(0, 10))

    tk.Label(in_row, text="Service (Name, Cost):",
             font=("Arial", 12),
             fg=text_faint, bg=card_bg).pack(side=tk.LEFT, padx=(0, 8))

    input_entry = tk.Entry(
        in_row, width=30, font=("Arial", 13),
        bg=bg_main, fg=text, insertbackground=text,
        highlightbackground=border, highlightthickness=1, bd=0
    )
    input_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

    tk.Label(in_row, text="Category:",
             font=("Arial", 12),
             fg=text_faint, bg=card_bg).pack(side=tk.LEFT, padx=(16, 5))

    cat_var = tk.StringVar()
    cat_var.set(CATEGORIES[0])
    category_dropdown = cat_var

    menu = tk.OptionMenu(in_row, cat_var, *CATEGORIES)
    menu.config(bg=card_bg, fg=text, relief=tk.FLAT,
                activebackground=border,
                highlightbackground=border)
    menu["menu"].config(bg=card_bg, fg=text)
    menu.pack(side=tk.LEFT)

    tk.Button(top, text="Add Subscription",
              command=add_subscription,
              bg=blue, fg="#333333", 
              font=("Arial", 13, "bold"),
              pady=8, relief=tk.FLAT, bd=0
             ).pack(pady=(10, 0))

    
    mid = tk.Frame(frame, bg=card_bg,
                   highlightbackground=border,
                   highlightthickness=1,
                   padx=20, pady=20)
    mid.pack(fill=tk.BOTH, expand=True)

    tk.Label(mid, text="Your Subscriptions (Sorted by Category):",
             font=("Arial", 15, "bold"),
             fg=text, bg=card_bg
             ).pack(anchor="w", pady=(0, 8))

    listbox = tk.Listbox(
        mid, height=10, font=("Courier", 12),
        bg="#0D1117", fg="#FFFFFF",
        relief=tk.FLAT, bd=0,
        highlightbackground=border, highlightthickness=1
    )
    listbox.pack(fill=tk.BOTH, expand=True, pady=(0, 12))

    btn_row = tk.Frame(mid, bg=card_bg)
    btn_row.pack(fill=tk.X)

    tk.Button(
        btn_row, text="Delete Selected", command=delete_subscription,
        bg="#D73833", fg="#000000", 
        font=("Arial", 12, "bold"),
        pady=6, relief=tk.FLAT, bd=0
    ).pack(side=tk.LEFT, expand=True, padx=6)

    tk.Button(
        btn_row, text="Show Cost Summary (W/M/Y)",
        command=show_cost_summary,
        bg="#E0B437", fg="#000000",
        font=("Arial", 12, "bold"),
        pady=6, relief=tk.FLAT, bd=0
    ).pack(side=tk.RIGHT, expand=True, padx=6)

   
    bottom = tk.Frame(frame, bg=card_bg,
                      highlightbackground=border,
                      highlightthickness=1,
                      padx=20, pady=20)
    bottom.pack(fill=tk.BOTH, expand=True, pady=(12, 0))

    total_label = tk.Label(bottom,
                           text="Total Monthly Spending: $0.00",
                           font=("Arial", 16, "bold"),
                           fg=text, bg=card_bg)
    total_label.pack()

    health_label = tk.Label(bottom,
                            text="Health Score: N/A",
                            font=("Arial", 14),
                            fg=text_faint, bg=card_bg)
    health_label.pack()

    chart_frame = tk.Frame(bottom, bg=card_bg)
    chart_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))

    return frame




def show_manager():
    welcome_frame.pack_forget()
    manager_frame.pack(fill=tk.BOTH, expand=True)
    update_display()



def start_app():
    global root, welcome_frame, manager_frame

    root = tk.Tk()
    root.title("Financial Buddy- Dark Mode")
    root.geometry("950x950")
    root.configure(bg="#0D1117")

    welcome_frame = create_welcome_page(root)
    manager_frame = create_manager_page(root)

    welcome_frame.pack(fill=tk.BOTH, expand=True)

    root.mainloop()


if __name__ == "__main__":
    start_app()
