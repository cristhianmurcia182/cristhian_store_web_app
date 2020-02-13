# Description

The aim of this project is to defined an API capable of retrieving and storing data related to a store.

For this project I used the following technologies:

1. Docker: To serve my MicrosoftSQLServer database.
2. Flask: As a framework to create my web application.
3. Marshmellow: To serialize the data.
4. SQLAlchemy: To connect with the relational database and to use the ORM.
5. SWagger: For documentation.
6. unittest: To test the code logic.
7. flask extensions (i.e. flask_restful).

# Arquitecture.

I defined a simple MVC architecture to isolate and to communicate in a clean manner the models, the views and the templates. Additionally I followd the RESTfull paradigm to define the enpoints.

To model the data I used a relational model which is shown below:


![alt text](https://github.com/cristhianmurcia182/cristhian_store_web_app/blob/master/modelo10.png)

To try out my endpoints please use postman and paste the following CURLs:

## Create a product:

curl --location --request POST 'http://localhost:5000/products' \
--header 'Content-Type: application/json' \
--data-raw '
{"name": "chocolatina jet", "unitary_cost": "123131"}'

## Create a client

curl --location --request POST 'http://localhost:5000/clients' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "Simon Bolivrl", "phone": "123131", "num_doc":"123123"}'

## Retrieve products

curl --location --request GET 'http://localhost:5000/products' \
--header 'Content-Type: application/json' \
--data-raw ''


## Retrieve clients

curl --location --request GET 'http://localhost:5000/clients' \
--header 'Content-Type: application/json' \
--data-raw ''


## Retrieve receipts

curl --location --request GET 'http://localhost:5000/receipts' \
--header 'Content-Type: application/json' \
--data-raw ''

