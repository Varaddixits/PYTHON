products = [("Laptop", "electronic"),
            ("Apple", "iPhone"),
            ("computer", "iPhone"),
            ("chair","furniture")]

price_dict = {"Laptop": 1000,
              "Apple": 2000,
              "computer": 3000,
              "chair": 4000,}

catlog = []

for product_name, category in products:
    catlog.append((product_name, price_dict[product_name], category))

print(catlog)
for item in catlog:
    print(item)

category_to_product = {}

for product_name, price, category in catlog:
    if category not in category_to_product:
        category_to_product[category]=[]

        category_to_product[category].append(product_name)
    print("\nproduct by category")
    print(category_to_product)

mpc =list(category_to_product)[0]

for category in category_to_product:
    if len(category_to_product[category])>len(category_to_product[mpc]):
        mpc=category

print("\nCategory with most product",mpc)
print(category_to_product[mpc])
