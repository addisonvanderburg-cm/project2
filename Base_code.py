import tkinter as tk

window = tk.Tk()
window.title("My First Gui App")

label = tk.Label(window, text= "Hello, Budgetbuddy")
label.pack()

button = tk.Button(window, text= "Click me", command= lambda: print ("Button Clicked"))
button.pack()

window.mainloop()