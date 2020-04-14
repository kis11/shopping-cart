import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")
SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID", "OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")

template_data = {
   "total_price_usd": "$14.95",
   "human_friendly_timestamp": "June 1st, 2019 10:00 AM",
   "products":[
       {"id":1, "name": "Product 1"},
       {"id":2, "name": "Product 2"},
       {"id":3, "name": "Product 3"},
       {"id":2, "name": "Product 2"},
       {"id":1, "name": "Product 1"}
    ]
}

client = SendGridAPIClient(SENDGRID_API_KEY) 
message = Mail(from_email=MY_EMAIL_ADDRESS, to_emails=MY_EMAIL_ADDRESS)
message.template_id = SENDGRID_TEMPLATE_ID 
message.dynamic_template_data = template_data
try:
    response = client.send(message)
    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    print(response.status_code) #> 202 indicates SUCCESS
    print(response.body)
    print(response.headers)
except Exception as e:
    print("OOPS", e)