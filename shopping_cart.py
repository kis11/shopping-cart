# shopping_cart.py

#from pprint import pprint

import csv
import datetime
import os
import pandas
import json
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

date = datetime.date.today()

from datetime import datetime
now = datetime.now()

csv_filepath = os.path.join(os.path.dirname(__file__), "data", "products.csv")
storeproducts = pandas.read_csv(csv_filepath)

total_price = 0
tax = total_price * .06
selectedids = []
productdict = []

while True:
    selectedid = input("Please enter a product identifier, and type DONE in all caps when complete: ")
    if selectedid == "DONE":
        break
    elif selectedid.isnumeric() == False: #source:https://www.w3schools.com/python/ref_string_isnumeric.asp
        print("Invalid identifier, please try again.")
        exit
    elif int(selectedid)> len(storeproducts) : #source: https://stackoverflow.com/questions/20297332/how-do-i-retrieve-the-number-of-columns-in-a-pandas-data-frame
        print("Invalid identifier, please try again.")
        exit
    else:
        selectedids.append(int(selectedid)-1)

print("#> ---------------------------------")
print("#> LION ENTERPRISES GROCERY")
print("#> WWW.LION-ENTERPRISES-GROCERY.COM")
print("#> ---------------------------------")
print("#> CHECKOUT ON " + date.strftime("%B %d, %Y") + " AT " + now.strftime("%I:%M:%S %p")) 
print("#> ---------------------------------")
print("#> SELECTED PRODUCTS: ")
for selectedid in selectedids:
    selectedid = int(selectedid)
    matchingproductprice = storeproducts.loc[selectedid].at["price"]
    matchingproductname = storeproducts.loc[selectedid].at["name"]
    print("#>" + "  "  +  "..." + "  " + matchingproductname + " " + "(" + str('${:.2f}'.format(matchingproductprice) + ")"))
    total_price = total_price + matchingproductprice 
tax = total_price * .06
print("#> ---------------------------------")
print("#> SUBTOTAL: " + str('${:.2f}'.format(total_price)))
print("#> TAX: " + str('${:.2f}'.format(tax)))
print("#> TOTAL: " + str('${:.2f}'.format(tax + total_price)))
print("#> ---------------------------------")
print("#> THANKS, SEE YOU AGAIN SOON!")
print("#> ---------------------------------")

while True:
    emailreceipt = input("Would you like an email receipt too? Please respond yes or no:")
    if emailreceipt == "yes" or "Yes" or "YES":
        storeproducts2 = storeproducts[['id', 'name', 'price']].copy()
        storeproducts2['price'] = storeproducts2['price'].map('${:,.2f}'.format)
        storeproducts2 = storeproducts2.take(selectedids) #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.take.html
        receiptlist2 = storeproducts2.to_dict('records')
        load_dotenv()
        SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
        MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")
        SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID", "OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
        template_data = {
        "subtotal_price_usd": str('${:.2f}'.format(total_price)),
        "tax_price_usd": str('${:.2f}'.format(tax)),
        "total_price_usd": str('${:.2f}'.format(tax + total_price)),
        "human_friendly_timestamp": date.strftime("%B %d, %Y") + " at " + now.strftime("%I:%M:%S %p"),
        "products": receiptlist2
        }    
        client = SendGridAPIClient(SENDGRID_API_KEY) 
        message = Mail(from_email=MY_EMAIL_ADDRESS, to_emails=MY_EMAIL_ADDRESS)
        message.template_id = SENDGRID_TEMPLATE_ID 
        message.dynamic_template_data = template_data
        try:
            response = client.send(message)
        except Exception as e:
            print("Oops, Sendgrid is down.", e)
        break
    elif emailreceipt == "no" or "No" or "NO": 
        print("OK, thanks again.")
        break
    else:
        print("Sorry, try again.")


