# Shop Inventory Management System
product_name_list = list()
product_per_unit_list = list()
product_quantity_list = list()

#Is Product Exists Function
def product_exists(product_name):
  if product_name_list.count(product_name)==0:
    return -1
  else:
    product_index=product_name_list.index(product_name)
    return product_index

# Add Product Function
def add_product():
  print("--------- ADD PRODUCT ----------")

  product_name=input("Enter product name: ")
  if product_exists(product_name.lower())!=-1:
    print()
    print(f"⚠️  {product_name} already exists in inventory!")
    print()
  else:
    product_name_list.append(product_name.lower())

    product_price_per_unit=float(input("Enter price per unit: "))
    if product_price_per_unit<=0:
      print()
      print("❌ Price must be greater than 0!")
      print()
    else:
      product_per_unit_list.append(product_price_per_unit)

      product_quantity=float(input("Enter quantity: "))
      if product_quantity<=0:
        print()
        print("❌ Quantity must be greater than 0!")
        print()
      else:
        product_quantity_list.append(product_quantity)
        print()
        print(f"✅ {product_name} added successfully!")
        print()

# Sell Product Function
def sell_product():
   product_name=input("Enter product name: ")

   if product_exists(product_name.lower())==-1:
     print()
     print(f"❌ {product_name} not found in inventory! ")
     print()

   else:
     product_index=product_name_list.index(product_name.lower())
     product_quantity=product_quantity_list[product_index]

     quantity=float(input("Enter quantity to sell: "))
     if quantity<=0:
      print()
      print("❌ Quantity must be greater than 0!")
      print()
     else:
      if product_quantity<quantity:
         print()
         print(f"❌ Not enough stock! Only {product_quantity} units available.")
         print()
      else:
       product_quantity_list[product_index]-=quantity

       print()
       print(f"✅ Sold {quantity} units of Apple")

       sale_value=product_quantity * product_per_unit_list[product_index]
       print(f"💰 Sale Value : ₹{sale_value}")
       print(f"📦 Remaining Stock: {product_quantity_list[product_index]} units")
       print()

# Restock Product Function
def restock_product():
  product_name=input("Enter product name: ")

  if product_exists(product_name.lower())==-1:
    print()
    print(f"❌ {product_name} not found in inventory! ")
    print()

  else:
    product_index=product_exists(product_name.lower())

    quantity=float(input("Enter quantity to add: "))

    if quantity<=0:
      print()
      print("❌ Quantity must be greater than 0!")
      print()
    else:
      product_quantity_list[product_index]+=quantity
      print()
      print(f"✅ {product_name} restocked! New quantity: {product_quantity_list[product_index]} units")
      print()

#Product Quantity Status Function
def check_status(product_quantity):
  if product_quantity==0:
    return " ❌ OUT OF STOCK"
  elif product_quantity<5:
    return "⚠️ LOW STOCK"
  else:
    return "✅ Available"





# View Stock Report Function
def view_stock_report():
  print("========================================")
  print("       📦 STOCK REPORT      ")
  print("========================================")
  print("No. Product    Price     Qty      Status")
  print("----------------------------------------")
  list_len = len(product_name_list)
  total_inventory_value=0;

  for i in range(0,list_len,1):
    print(f"{i+1}    {product_name_list[i]}    {product_per_unit_list[i]}   {product_quantity_list[i]}     {check_status(product_quantity_list[i])}")
    total_inventory_value+= product_per_unit_list[i]*product_quantity_list[i]
  print("----------------------------------------")
  print(f"Total Products: {list_len}")
  print(f"Total Inventory Value: {total_inventory_value}")
  print("========================================")



def main_menu():
  print("================================")
  print("   🏪 SHOP INVENTORY MANAGER ")
  print("================================")
  print("1. Add New Product ")
  print("2. Sell Product")
  print("3. Restock Product")
  print("4. View Stock Report")
  print("5. Exit")
  print("--------------------------------")


while True:
  main_menu()
  user_input=input("Enter your choice: ")

  if user_input=="1":
    add_product()
  elif user_input=="2":
    sell_product()
  elif user_input=="3":
    restock_product()
  elif user_input=="4":
    view_stock_report()
  elif user_input=="5":
    print("xxxxxxxxx Thank you! xxxxxxxxx")
    break
  else:
    print("❌ Invalid choice! Try again.")






