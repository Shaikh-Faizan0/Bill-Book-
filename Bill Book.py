total = 0
bill_items = []

def display_bill():
    print("=" * 30)
    print("{:^30}".format("Bill Details"))
    print("=" * 30)
    for item, price in bill_items:
        print(f"{item:<15} : {price:>10} Rs")
    print("-" * 30)
    print(f"Total{'':<15} : {total:>10} Rs")
    print("=" * 30)

print("=" * 50)
print("{:^50}".format("Bill Calculator and Tracker"))
print("=" * 50)

name = input("Enter a unique name for your bill: ")
print("Enter the names and prices of items. Type 'q' to calculate the total.\n")

while True:
    item_name = input("Item name: ")
    if item_name.lower() == "q":
        break

    try:
        item_price = float(input("Item price (Rs): "))
        total += item_price
        bill_items.append((item_name, item_price))

        print(f"Added '{item_name}' with {item_price:.2f} Rs.")
        print("Current total: {:.2f} Rs\n".format(total))

    except ValueError:
        print("Invalid price format. Please enter a valid number.\n")

print("\nBill calculation completed.")
display_bill()

with open(f"{name}.txt", "w") as file:
    file.write("Bill Details\n")
    for item, price in bill_items:
        file.write(f"{item} : {price:.2f} Rs\n")
    file.write("-" * 30 + "\n")
    file.write(f"Total{'':<15} : {total:.2f} Rs\n")

print("=" * 50)
print("{:^50}".format("Thank you for using the Bill Calculator and Tracker!"))
print("=" * 50)
