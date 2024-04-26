# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:11:06 2024

@author: KOM
"""

from faker import Faker
import pandas as pd
import os.path
# "C:/Users/KOM/Desktop/Opgaver"
fake=Faker(locale="da")

test_list = []
def faker_gen(test):
    for i in range(1, test):
        test={}
        
        test["Name"]=fake.name()
        test["Address"]=fake.address()
        test["Profession"]=fake.job()
        test["Phone Number"]=fake.phone_number()
        test["E-mail"]=fake.email()
        
        
        test_list.append(test)
    return pd.DataFrame(test_list)

test_list2 = []
def faker_gen2(test2):
    for i in range(1, test2):
        test2={}
        
        test2["Name"]=fake.name()
        test2["Address"]=fake.address()
        test2["Profession"]=fake.job()
        test2["Phone Number"]=fake.phone_number()
        test2["E-mail"]=fake.email()
        
        
        test_list2.append(test2)
    return pd.DataFrame(test_list2)
    
data = faker_gen(100)
data2 = faker_gen2(100)
# data.to_excel(r"C:/Users/KOM/Desktop/Opgaver/Dashboards/Uge7_8/Starter/test.xlsx", index = False)