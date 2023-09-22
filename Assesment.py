product_price={
   "jeans":1000,
   "tops":300,
   "shirt":600,
   "kurties":500,
   "saree":800,

}

shopping_cart = {}

def display_products():
    print("Available Products:")
display_products()      

def complete_purchase():
    confirm = input("Confirm purchase (yes/no): ").lower()
    if confirm == "yes":
        print("Thank you for your purchase!")
        shopping_cart.clear()
    else:
        print("Purchase canceled.")

while True:
    print("\n*** Online Shopping ***")
    print("1. Display Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Complete Purchase")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    if choice == "1":

        print("jeans")
        print("tops")
        print("shirt")
        print("kurties")
        print("saree")

    elif choice == "2":
        product_name = input("Enter product name: ")
        product_price=int(input("Enter your product quantity:"))
        print(product_name*product_price)
    elif choice == "3":
        print("your purchased product cart details")
    elif choice == "4":
        complete_purchase()
    elif choice == "5":
        print("Thank you for shopping with us!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-5).")
