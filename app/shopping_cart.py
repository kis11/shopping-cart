# shopping_cart.py

#from pprint import pprint

#todo: dollar format, tax function

import csv
import datetime
import os
import pandas
import json
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def calc_tax(number):
    return number * .0875
def to_usd(number):
    return str('${:.2f}'.format(number)) #todo: change the below to to_usd to simplify
def email_info():
    global selectedid
    storeproducts2 = storeproducts[['id', 'name', 'price']].copy()
    storeproducts2['price'] = storeproducts2['price'].map('${:,.2f}'.format)
    storeproducts2 = storeproducts2.take(selectedids) #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.take.html
    receiptlist = storeproducts2.to_dict('records')
    load_dotenv()
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
    MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")
    SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID", "OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
    template_data = {
    "subtotal_price_usd": to_usd(total_price),
    "tax_price_usd": to_usd(tax),
    "total_price_usd": to_usd(tax + total_price),
    "human_friendly_timestamp": date.strftime("%B %d, %Y") + " at " + now.strftime("%I:%M:%S %p"),
    "products": receiptlist
    }    
    client = SendGridAPIClient(SENDGRID_API_KEY) 
    message = Mail(from_email=MY_EMAIL_ADDRESS, to_emails=MY_EMAIL_ADDRESS)
    message.template_id = SENDGRID_TEMPLATE_ID 
    message.dynamic_template_data = template_data
    try:
        client.send(message)
    except Exception as e:
        print("Oops, Sendgrid is down. Our bad.", e)
def find_price(dataframe,id):
    return dataframe.loc[id].at["price"]
def find_name(dataframe,id):
    return dataframe.loc[id].at["name"]

if __name__=="__main__":
    date = datetime.date.today()
    from datetime import datetime
    now = datetime.now()

    csv_filepath = os.path.join(os.path.dirname(__file__), '..', "data", "products.csv")
    storeproducts = pandas.read_csv(csv_filepath)

    total_price = 0
    selectedids = []
    productdict = []

    while True:
        selectedid = input("Please enter a product identifier, and type DONE in all caps when complete: ")
        if selectedid == "DONE":
            break
        elif selectedid.isnumeric() == False: 
            print("Invalid identifier entered, please try again.")
            exit
        elif int(selectedid)> len(storeproducts) : 
            print("Invalid identifier entered, please try again.")
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
       matching_product_price = find_price(storeproducts,selectedid)
       matching_product_name = find_name(storeproducts,selectedid)
       print("#>" + "  "  +  "..." + "  " + matching_product_name + " " + "(" + to_usd(matching_product_price) + ")")
       total_price = total_price + matching_product_price 
    tax = calc_tax(total_price)
    print("#> ---------------------------------")
    print("#> SUBTOTAL: " + to_usd(total_price))
    print("#> TAX: " + to_usd(tax))
    print("#> TOTAL: " + to_usd(tax + total_price))
    print("#> ---------------------------------")
    print("#> THANKS, SEE YOU AGAIN SOON!")
    print("#> ---------------------------------")

    while True:
        emailreceipt = input("Would you like an email receipt too? Please respond yes or no:")
        if emailreceipt in ("yes","Yes","YES"):
            email_info()
            break
        elif emailreceipt in ("no","No","NO"): 
            break
        else:
            print("Sorry, try again.")
    print("OK, got it. Thanks again.")
