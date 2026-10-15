orders = []

while True:
    choice = input("1 Add order , 2 Show order , Q quit")

    if choice == "1":
        orders.append(float(input("Enter order : ")))
    elif choice == "2":
        total = 0
        for order in orders:
            discount = order * 10
            print(order,"==",round(discount,2))
            total += discount
        print("total :",round(total,2))
    elif choice == "q":
        break
    else:
        continue