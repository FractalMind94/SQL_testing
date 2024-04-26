# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 09:58:03 2024

@author: KOM
"""
import sqlite3
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

northwind = mysql.connector.connect(
  host="localhost", #By default = localhost
  user="root", #by default = root
  password=""
)

northwind.database = "northwind" # using an existing database

# Create a cursor object
cursor = northwind.cursor()

# Read the SQL file
with open('northwind.sql', 'r') as sql_file:
    sql_script = sql_file.read()    

# SQL query to retrieve data from different tables
sql_query = '''
SELECT Orders.OrderID, Customers.ContactName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
'''

# Execute the query
cursor.execute(sql_query)

# Fetch the results
results = cursor.fetchall()


#Define each table by its name in sql
categories = "categories"
customers = "customers"
employees = "employees"
employeeterritories = "employeeterritories"
orderdetails = "orderdetails"
orders = "orders"
products = "products"
region = "region"
shippers = "shippers"
suppliers = "suppliers"
territories = "territories"


#Import each table as a dataframe (Overwriting the data above)
categories = pd.read_sql(f"SELECT * FROM {categories}", con=northwind)
customers = pd.read_sql(f"SELECT * FROM {customers}", con=northwind)
employees = pd.read_sql(f"SELECT * FROM {employees}", con=northwind)
employeeterritories = pd.read_sql(f"SELECT * FROM {employeeterritories}", con=northwind)
orderdetails = pd.read_sql(f"SELECT * FROM {orderdetails}", con=northwind)
orders = pd.read_sql(f"SELECT * FROM {orders}", con=northwind)
products = pd.read_sql(f"SELECT * FROM {products}", con=northwind)
region = pd.read_sql(f"SELECT * FROM {region}", con=northwind)
shippers = pd.read_sql(f"SELECT * FROM {shippers}", con=northwind)
suppliers = pd.read_sql(f"SELECT * FROM {suppliers}", con=northwind)
territories = pd.read_sql(f"SELECT * FROM {territories}", con=northwind)

