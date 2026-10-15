try:
    order_amount = float(input("Enter the amount of the order: "))

    if order_amount >= 2000:
        discount_rate = 15
    elif order_amount >= 1500:
        discount_rate = 10
    elif order_amount >= 1000:
        discount_rate = 7
    else:
        discount_rate = 0

    discount = order_amount * discount_rate / 100
    final_price = order_amount - discount

    print("Discount:", discount_rate, "%")
    print("Discount amount:", discount)
    print("Final amount:", final_price)

except ValueError:
        print("Error : Please enter a numeric value")
