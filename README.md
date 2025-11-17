Whats in the code: 
- First page
    - Get started
- Add subscription
- Delete subcription
- Categories
- Outputs the spending health
- Highlights the spendings over 20 in red
    - Thresholds for spendings 
- Error checkers 

What it needs: 
- Background to be changed to have a different color than textbox
- Once in the second page dont have the top button
    - Make it a textbox that says subscription manager
- It has to be hex code not the color name 
- Needs to be sorted so that we can sort by specific catigories. 
- See your spending price for weekly, monthly and yearly. 

PERSON B — Data Manager + Logic/Backend Developer
Role: Writes all data processing, list operations, math, sorting, filtering, and statistical logic.
Focus: List of lists, conversions, calculations, sorting, search, health score, etc.
B1. GitHub Setup Tasks
Create branch: personB-data-logic
Add a logic.py or similar file for functions
Commit initial function structure (empty function definitions)
B2. Build the Data Structure
Create the main list of lists:
[name, cost, cycle, category, monthly_cost]
Create a function to return the entire list to the GUI
B3. Implement “Add Subscription” Logic
Function should:
Validate name
Validate cost is numeric
Validate a billing cycle is chosen
Validate category is chosen
Convert the cost to monthly cost
Weekly → ×4
Yearly → ÷12
Append new list to main subscription list
Return success/error messages to GUI
B4. Implement Sorting Logic
Create functions for:
Sort alphabetically
Sort by cost (ascending)
Sort by cost (descending)
Sort by category
Sort by billing cycle
Refresh main list after sorting
B5. Implement Search Logic
Search by exact name
Search by partial match
Search by category
Return list of matching subscriptions
Return indexes of matches for GUI highlighting
B6. Implement Category Filtering
Functions to:
Filter by category
Return filtered lists
Calculate totals per category
B7. Implement Statistics Logic
Functions to calculate:
Total number of subscriptions
Average cost
Total monthly cost (accumulator)
Highest & lowest subscription (min/max)
Count subscriptions above $20
B8. Implement the Health Score System
Logic:
If total cost < 40 → “Excellent spending control!”
40–80 → “Fair, worth reviewing”
80 → “High spending! Consider reviewing”
Return string to GUI.
B9. Implement Delete Subscription Logic
Accept index of subscription
Delete list item
Return success message
Make it work with GUI’s confirmation popup
B10. Implement Optional Features
(Only if time allows)
Calculate days until next renewal
Text-based “pie chart” breakdown
Light/dark mode backend color values
Export to file
Load data from file
