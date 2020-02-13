# Description

The aim of this project is to define an API capable of retrieving and storing data related to a store.

For this project I used the following technologies:

1. Docker: To serve my MicrosoftSQLServer database.
2. Flask: As a framework to create my web application.
3. Marshmellow: To serialize the data.
4. SQLAlchemy: To connect with the relational database and to use the ORM.
5. SWagger: For documentation.
6. unittest: To test the code logic.
7. flask extensions (i.e. flask_restful).

# Arquitecture.

I defined a simple MVC architecture which is suitable for communicating the model, view and the template components of the web app in an efficient and modular manner. Additionally I followed the RESTfull paradigm to define the enpoints (APIs).

To model the data I used a relational model which is shown below:


![alt text](https://github.com/cristhianmurcia182/cristhian_store_web_app/blob/master/modelo10.png)


# API
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

# Steps to run the app.

To run the app follow the steps depicted below:

1. Install python 3.7.

2. Clone this repo and navigate to it using the terminal (i.e. cd cristhian_store_web_app).

3. Create a python venv and install the dependencies displayed in the requirements file of this repo **pip install -r requirements**. Then activate the venv (i.e. source venv/bin/activate).

4. Install docker.

5. Execute *docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=yourStrong(!)Password' -p 1433:1433 -d mcr.microsoft.com/mssql/server:2017-CU8-ubuntu*. This command creates a docker container which has and image for MicrosoftSQLServer. Type a password that you remember, we will use it later.

6. Start the container installed in step 5, try *docker start <your containner name>*. To know your container name type *docker ps -a* and find the one installed in step 5.
    
7. Start the container command prompt. Try *docker exec -it <container_id|container_name> /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P <your_password>*. 

8. Inside the shell create a database, which will be used by flask to store the data. Type *CREATE DATABASE store;* hit enter and then type *GO*, hit enter. Please remember the name of the database, it will be used later.

9. It is necesary to install a MicrosoftSQLServer driver to enable a connection between SQLAlchemy and the MSSQL database, otherwise some errors will appear (I spent 2 hours figuring this out). On mac you can install the driver using the package manager *brew* (searche it on google). After that you can type *brew install microsoft/mssql-release/mssql-tools*. It is important to know the location of the driver in your local machine, to do so, just type */etc/odbcinst.ini* and copy the name and the path of the driver, this information will be used later.

10. Open the config.py file of your local repo and replace the variables with the local ones (DB_NAME = 'Use the name of your MSSQL database', DB_PASSWORD = 'the password of the sa user that you defined when downloading the container (step 5)'
    DRIVER = 'the path of the driver installed in step 9').
    
 11. Type python *models.py db init* in your command prompt  to create the first migration folder and start alembic.
 
 12. Type python models.py db upgrade to run the first migration and create the tables in the database.
 
 13. Type python populate_database.py to populate the tables with dummy data.
 
 14. Start the flask app by typing python app.py.
 
 15. After following this steps the flask server will be running, now you can test the API by making requests with the CURLs described in the API section above, I suggest to use postman.
 
 16. Swagger documentation is visualized by runing flask and pasting *http://127.0.0.1:5000/ * in your borwser.
 
 17  The unit tests associated to my logic functions can be executed by typing python backend_test.py.
 
 # TO DO
 
Due to the limited time provided  and my responsabilities (I have to work full time), I only managed to defined the backend. To enhance what I have here, I suggest to define stronger unittest, Create a validation layer to catch mistakes and rules defined by the client (i.e. It is not possible to create a client with duplicated phone or ID). Improve the docummentation.

Nevertheless, the most important aspect missing in this project is the Front-End, which facilitates serving the data.

*Finally I would like to thank team international for letting me present this test*


