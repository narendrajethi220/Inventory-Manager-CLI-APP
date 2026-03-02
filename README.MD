🏪 Inventory Manager — Problem Definition

📌 Problem Statement
You are hired to build a Shop Inventory Management System for a local grocery store owner. The owner wants a simple Python program to track his products, manage stock levels, and get alerts when items are running low — all from a text menu.

🎯 Objective
Build a menu-driven Python program using only:
Lists — to store product names, quantities, prices
Loops — to keep menu running
Conditions — to check stock, validate input
Basic operations — add, subtract, multiply

📋 Features to Build
✅ Feature 1 — Main Menu
Program must keep showing this menu until user presses 5 to Exit
==============================
   🏪 SHOP INVENTORY MANAGER
==============================
1. Add New Product
2. Sell Product
3. Restock Product
4. View Stock Report
5. Exit
------------------------------
Enter your choice:


✅ Feature 2 — Add New Product
Ask for product name, price per unit, quantity
If product already exists → show error, don't add duplicate
Store in 3 separate lists: product_names, product_prices, product_qty
Sample Input / Output:
--- ADD PRODUCT ---
Enter product name  : Apple
Enter price per unit: 10
Enter quantity      : 20

✅ Apple added successfully!

--- ADD PRODUCT ---
Enter product name  : Apple
⚠️  Apple already exists in inventory!


✅ Feature 3 — Sell Product
Ask for product name and quantity to sell
Check: Does product exist? If not → show error
Check: Is enough stock available? If not → show error
If valid → subtract quantity and show remaining stock
Sample Input / Output:
--- SELL PRODUCT ---
Enter product name     : Apple
Enter quantity to sell : 5

✅ Sold 5 units of Apple
💰 Sale Value : ₹50
📦 Remaining Stock: 15 units

--- SELL PRODUCT ---
Enter product name     : Apple
Enter quantity to sell : 50

❌ Not enough stock! Only 15 units available.

--- SELL PRODUCT ---
Enter product name     : Banana
❌ Banana not found in inventory!


✅ Feature 4 — Restock Product
Ask for product name and quantity to add
Product must already exist in inventory
Add new quantity to existing stock
Sample Input / Output:
--- RESTOCK PRODUCT ---
Enter product name    : Mango
Enter quantity to add : 30

✅ Mango restocked! New quantity: 33 units


✅ Feature 5 — View Stock Report
Display all products: Name | Price | Quantity | Status
Qty = 0 → ❌ OUT OF STOCK
Qty < 5 → ⚠️ LOW STOCK
Qty >= 5 → ✅ Available
Show total products and total inventory value at bottom
Sample Output:
====================================================
            📦 STOCK REPORT
====================================================
No.  Product     Price    Qty     Status
----------------------------------------------------
1.   Apple       ₹10      15      ✅ Available
2.   Mango       ₹30      3       ⚠️  LOW STOCK
3.   Banana      ₹5       0       ❌ OUT OF STOCK
4.   Orange      ₹20      8       ✅ Available
----------------------------------------------------
Total Products        : 4
Total Inventory Value : ₹395
====================================================


⚠️ Validation Rules
Situation
What to show
Choice not in 1–5
❌ Invalid choice! Try again.
Quantity is 0 or negative
❌ Quantity must be greater than 0!
Price is 0 or negative
❌ Price must be greater than 0!
Selling more than stock
❌ Not enough stock!
Product not found
❌ Product not found!
Duplicate product
⚠️ Product already exists!
Inventory empty on report
📭 No products in inventory yet!


🗂️ Data Storage Structure
Use 3 parallel lists — index must match across all lists:
`
# Apple  → index 0 → price ₹10 → qty 15
# Mango  → index 1 → price ₹30 → qty 3
# Banana → index 2 → price ₹5  → qty 0


🧠 Logic Hints (Think, don't copy!)
FIND PRODUCT → loop through product_names
               if name matches → note that index
               use same index on price and qty lists

SELL LOGIC   → find index
               check product_qty[index] >= sell_qty
               if yes → product_qty[index] = product_qty[index] - sell_qty

TOTAL VALUE  → start total = 0
               loop i from 0 to len(product_names)
               total = total + (product_prices[i] × product_qty[i])


📐 Constraints
Use only Lists, Loops, Conditions, and Operations
All data lives in the 3 parallel lists
Must use a while True loop for the menu

✅ Success Checklist
☐ Menu loops until Exit is chosen
☐ Can add multiple products
☐ Duplicate product is blocked
☐ Sell reduces stock correctly
☐ Cannot sell more than available stock
☐ Restock increases quantity
☐ Stock report shows correct status tags
☐ Total inventory value calculated correctly
☐ All invalid inputs handled with messages

