#define the menu of restaurent
import emoji

menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80
}

#Greet
print("Welcome to our restaurant!")
print("Pizza: rs40\nPasta: rs50\nBurger: rs60\nSalad: rs70\nCoffee: rs80")


order_total = 0
item_1 = input("Enter the first item you want to order: ").title()
if item_1 in menu:
    order_total += menu[item_1]  #order total + menu[item_1]
    print(f"Your order for {item_1} has been added to your order.")
else:
    print(f"Sorry, {item_1} is not available in our menu.")

another_order = input("Do you want to order another item? (yes/no): ")
if another_order.lower() == "yes":
    item_2 = input("Enter the second item you want to order: ").title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your order for {item_2} has been added to your order.")
    else:
        print(f"Sorry, {item_2} is not available in our menu.")

print(f"The total amount of items to pay is: {order_total}")

print("Thank you for your order! Please visit again.")
