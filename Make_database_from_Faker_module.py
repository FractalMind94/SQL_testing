# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:17:21 2024

@author: KOM
"""

import pandas as pd
from sqlalchemy import create_engine
import pymysql
from Faker_module import data 
from Faker_module import data2
# Create sample DataFrame

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
# Define the MySQL connection parameters
db_username = 'root' #by default = root
db_password = '' #add MySQL password
db_host = 'localhost' #By default = localhost
db_port = '3306'  # by default = 3306
db_name = 'faker' # Database Name

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
df.to_sql('faker1', con=engine, index=False, if_exists='replace')
df2.to_sql('faker2', con=engine, index=False, if_exists='replace')
    

# Confirm that data has been written to the database
print(pd.read_sql('SELECT * FROM faker.faker1 ', con=engine))





