PERSON A — GUI Builder + Data Input Manager
Role: Builds all GUIs for input, viewing, tabs, and display.
Focus: Window layout, widgets, structure, and user interactions.
A1. GitHub Setup Tasks
Create branch: personA-gui-layout
Add main.py or equivalent GUI file
Commit GUI skeleton (no logic yet)
A2. Create Tkinter Window & Tabs
Build the main Tkinter window
Set window title
Set default size
Create a Notebook (tab system)
Add three tabs:
Add Subscription
View/Sort/Manage Subscriptions
Statistics / Health Score
A3. Build the “Add Subscription” Tab
Add the following widgets:
Input Elements:
Subscription Name (Entry box)
Cost (Entry box)
Billing Cycle (Weekly, Monthly, Yearly) — radio buttons or dropdown
Category dropdown (Entertainment, Utilities, Food)
Buttons:
Add Subscription
Connects to Person B’s logic function later (stub only)
Layout:
Position labels + input boxes
Group widgets neatly
Add placeholder labels for error/success messages
A4. Build the “View + Sort” Tab
Display Area:
Build list/table display (Listbox or Treeview)
Create function stubs to “refresh display”
Sorting Controls:
Dropdown for:
Alphabetical
Cost
Category
Highest → Lowest
Toggle for Weekly/Monthly/Yearly display
Search Controls:
Search bar input entry
“Search” button (links to Person B’s logic later)
Delete Controls:
Delete button
Build the pop-up confirmation window (“Are you sure?”)
A5. Build the “Statistics” Tab
Add labels/placeholders for:
Total subscription count
Average cost
Total monthly cost
Health score text
Highlight expensive subs (above $20/month)
Category summaries
(Person B will supply the logic.)
A6. Add Dark/Light Mode Toggle
Add a toggle button
Build function stub to switch colors
(Person B will help implement the theme switching logic.)
A7. Finalize GUI Integration
Make sure all buttons call Person B’s functions
Ensure GUI updates correctly when data changes
Build layout consistency across tabs
Clean up unused widgets, spacing, alignment
