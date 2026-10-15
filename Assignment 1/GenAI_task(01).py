product = ["Mouse","Phone","Tablet","Laptop","Headphone","Smartwatch"]

sample_product=("Gadget",10000,"Homeapplication")

print(product[-1])
print(product[1])

product.append("Soundbox")
product.append("Car")

print(product)

sample_product=list(sample_product)
sample_product[1]=1000
sample_product=tuple(sample_product)

print(sample_product)
