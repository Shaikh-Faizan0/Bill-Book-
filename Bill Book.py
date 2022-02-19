sum = 0
Name = input("Enter unique name :")
f = open(Name, "w")
a = f.write(f"items   :   price(Rs)\n")
while (True):
    items = input("Enter the Name of the items "
                  "or q for total bill :")


    if items != "q":
        i = input("Enter the price of items :")
        sum = sum + int(i)
        print(f"you sum is {sum}\n")
        f = open(Name, "a")
        a = f.write(f"{items}  :   {i}Rs\n")
        f.close()

    else:
        print(f"\nyour total bill is {sum}\n")

        f = open(Name, "r")
        a = f.read()
        print(a)
        f.close()
        break
