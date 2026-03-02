# 🏪 Inventory Manager CLI App

A simple **menu-driven Python application** that helps a grocery store owner manage inventory directly from the terminal.

This project is built using only:

* Lists
* Loops
* Conditions
* Functions
* Basic arithmetic operations

It is designed to strengthen core Python fundamentals.

---

## 📌 Problem Statement

Build a Shop Inventory Management System that allows a user to:

* Add new products
* Sell products
* Restock items
* View stock reports
* Get low-stock alerts

All operations must be handled through a text-based menu.

---

## 🎯 Features

### 1️⃣ Main Menu

The program keeps running until the user selects **Exit**.

```
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
```

---

### 2️⃣ Add New Product

* Takes product name, price, and quantity.
* Prevents duplicate product entries.
* Stores data in parallel lists.

---

### 3️⃣ Sell Product

* Checks if product exists.
* Ensures enough stock is available.
* Updates stock after successful sale.
* Displays sale value and remaining stock.

---

### 4️⃣ Restock Product

* Adds quantity to an existing product.
* Validates product existence.

---

### 5️⃣ View Stock Report

Displays:

* Product Name
* Price
* Quantity
* Status

Status Rules:

* Qty = 0 → ❌ OUT OF STOCK
* Qty < 5 → ⚠️ LOW STOCK
* Qty ≥ 5 → ✅ Available

Also shows:

* Total number of products
* Total inventory value

---

## 🗂️ Data Structure Used

The system uses **three parallel lists**:

```python
product_names = []
product_prices = []
product_qty = []
```

Example structure:

| Index | Name   | Price | Quantity |
| ----- | ------ | ----- | -------- |
| 0     | Apple  | 10    | 15       |
| 1     | Mango  | 30    | 3        |
| 2     | Banana | 5     | 0        |

Index position links all product data.

---

## ⚠️ Validation Rules

| Situation               | Message                            |
| ----------------------- | ---------------------------------- |
| Invalid menu choice     | ❌ Invalid choice! Try again.       |
| Quantity ≤ 0            | ❌ Quantity must be greater than 0! |
| Price ≤ 0               | ❌ Price must be greater than 0!    |
| Product not found       | ❌ Product not found!               |
| Selling more than stock | ❌ Not enough stock!                |
| Duplicate product       | ⚠️ Product already exists!         |
| Empty inventory report  | 📭 No products in inventory yet!   |

---

## 🧠 Logic Approach

* Product search → Loop through `product_names`
* Use index to access price and quantity
* Update quantity using arithmetic operations
* Calculate total inventory value using a loop

---

## 📐 Constraints

* Only Lists, Loops, Conditions, and Basic Operations
* Must use `while True` for menu loop
* No dictionaries or advanced data structures

---

## 🚀 How to Run

```bash
python inventory_manager.py
```

---

## ✅ Learning Outcomes

* Working with parallel lists
* Input validation
* Menu-driven program structure
* Index-based data handling
* Basic business logic implementation

---

## 📦 Project Status

✔ Core features implemented
✔ Validation handled
✔ Fully terminal-based

--
Developed with ❤️ by Narendra Singh Jethi!
