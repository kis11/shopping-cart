import os
import pandas


#
## if CSV file in the data dir:
#csv_filepath = os.path.join(os.path.dirname(__file__), "data", "products.csv")
#selectedid = str(2)
#storeproducts = pandas.read_csv(csv_filepath)
##print(storeproducts)
#
##print(storeproducts["name"])
#
#selectedproduct = storeproducts.loc[4]
#selectedproductprice = storeproducts.loc[4].at["price"]
#
#
##matching_products = [p for p in storeproducts if str(p["id"]) == str(selectedid)]
##matching_product = matching_products[0]
##print(matching_products)

csv_filepath = os.path.join(os.path.dirname(__file__), "data", "products.csv")
storeproducts = pandas.read_csv(csv_filepath)


total_price = 0
selectedids = []

while True:
    selectedid = input("Please enter a product identifier, and type DONE when complete: ")
    if selectedid == "DONE":
        break
    else:
        selectedids.append(selectedid)
        

for selectedid in selectedids:
    selectedid = int(selectedid)
    matching_product = storeproducts.loc[selectedid]
    matchingproductprice = storeproducts.loc[selectedid].at["price"]
    total_price = total_price + storeproducts.loc[selectedid].at["price"]
    #print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"]))

print(matchingproductprice)