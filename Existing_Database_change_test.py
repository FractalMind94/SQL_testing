# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:02:26 2024

@author: KOM
"""

import mysql.connector
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
                             #user:password@host/database
con_string = 'mysql+pymysql://root:@localhost/northwind' #add password
engine = create_engine(con_string)

query = ''' SELECT * FROM northwind.customers'''
query2 =''' SELECT * FROM northwind.orders'''

customers = pd.read_sql(query, engine)
orders = pd.read_sql(query2, engine)

customer_orders = pd.concat([customers, orders])

customer_orders.to_sql('customer_orders', engine, if_exists='replace')