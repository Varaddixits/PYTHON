price_dict = {"Notebook": 35, "Pen": 20, "Sharpner": 10, "Scale": 10, "Pencil": 5, "Sticky notes": 40}

price_dict["Paper"]= 100
price_dict["Scissors"]= 50

price_dict["Notebook"] = 50
print(price_dict)

p_remove = "Notebook"

if p_remove in price_dict:
    del price_dict[p_remove]
    print(p_remove,"Removed")
else:
    print(p_remove,"Not Removed")


total =sum(price_dict.values())
avg = total/len(price_dict)

print(avg,"Average Price")






