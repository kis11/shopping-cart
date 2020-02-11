# shopping-cart
Shopping Cart Project

Hey, welcome to the Shopping Cart project.

The environment we are working in is shopping-env. To create and access this virtual environment in your terminal, type:

```sh
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
```

You also need to make sure you install the necessary packages to run the program. These are:

```sh
csv
datetime
os
pandas
json
dotenv
sendgrid
```

Use the "pip install" format to install these packages when you first create the virtual environment. Consult the professor's Github repository if you need extra details. 

On Github, fork the folder and clone it onto your computer. Make sure you include a .gitignore file. 

Then, access the folder shopping-cart within the environment:

```sh
cd ~/selectedpathonyourcomputer/shopping-cart/
```

## Email Functionality 

To make the email functionality work, you need to have a Sendgrid account. Create a new dynamic email template, with test data:

```sh
{
    "subtotal_price_usd": "$10.50",
    "tax_price_usd": "$4.45",
    "total_price_usd": "$14.95",
    "human_friendly_timestamp": "July 4th, 2019 10:00 AM",
    "products":[
        {"id":1, "name": "Product 1", "price": "2.65"},
        {"id":2, "name": "Product 2", "price": "2.65"},
        {"id":3, "name": "Product 3", "price": "2.65"},
        {"id":2, "name": "Product 2", "price": "2.65"},
        {"id":1, "name": "Product 1", "price": "2.65"}
    ]
}
```

And code:

```sh

<img src=http://cdn.mcauto-images-production.sendgrid.net/ba27d61627340a59/1273c923-d32f-4ad3-9f52-7c6f51d5aa41/260x244.png>

<h3>Hey, this is your receipt from Lion Enterprises Grocery.</h3>

<p>Date: {{human_friendly_timestamp}}</p>

<p>Subtotal: {{subtotal_price_usd}}</p>
<p>Tax: {{tax_price_usd}}</p>
<p>Total: {{total_price_usd}}</p>

<ul>
{{#each products}}
	<li>You ordered: {{this.name}} for {{this.price}} </li>
{{/each}}
</ul>

<p>Have a great day, and don't forget to stop in again soon.</p>
```
You also need to create a .env file that has your API keys. Set 3 variables in your .env file:

```sh
SENDGRID_API_KEY =
MY_EMAIL_ADDRESS =
SENDGRID_TEMPLATE_ID =
```

Set the email address to the intended recipient. The template ID should be visible on the Sendgrid website. They API key was given to you when you made your account. 

Important: Make sure you also have a .gitignore file, that includes .env.

In your virtual environment, make sure you are navigated to the shopping-cart folder, and then type "shopping_cart.py". 


The prompt should open and you may select the identifiers chosen at the store. When you are done, make sure you type DONE in all caps. Then, your receipt will pop up. You will then have the option to also receive an email receipt, which will be sent to the designated recipient. 

Thanks and happy shopping. 
