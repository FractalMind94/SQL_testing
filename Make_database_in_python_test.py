# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:44:08 2024

@author: KOM
"""
import pandas as pd
from sqlalchemy import create_engine
import pymysql

# Create sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Location': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Define the MySQL connection parameters
db_username = 'root' #by default = root
db_password = '' #add MySQL password
db_host = 'localhost' #By default = localhost
db_port = '3306'  # by default = 3306
db_name = 'test1' # database name

# Connect to MySQL server
connection = pymysql.connect(host=db_host,
                             user=db_username,
                             password=db_password,
                             port=int(db_port))


# Create cursor object
cursor = connection.cursor()

# Execute SQL query to create database if not exists
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

# Close cursor
cursor.close()

# Close connection
connection.close()

# Construct the MySQL connection string with the database name
db_connection_str = f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'

# Create SQLAlchemy engine
engine = create_engine(db_connection_str)

# Write DataFrame to MySQL database
df.to_sql('test1', con=engine, index=False, if_exists='replace')

    

# Confirm that data has been written to the database
print(pd.read_sql('SELECT * FROM test1', con=engine))
