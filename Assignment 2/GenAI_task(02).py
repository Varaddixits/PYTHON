
order = [1200,2500,800,1750,3000]
total_avenue = 0

print("order_amount|discount|final_amount")

for order_amount in order:
    if order_amount >= 2000:
        discount_rate = 15
    elif order_amount >= 1500:
        discount_rate = 10
    elif order_amount >= 1000:
        discount_rate = 7
    else:
        discount_rate = 0


    discount = order_amount * discount_rate /100
    final_amount = order_amount - discount
    total_avenue= final_amount-total_avenue

    print(order_amount,"|",discount,"|",round(final_amount,2))
print("Total revenue after discount:",round(total_avenue,2))



