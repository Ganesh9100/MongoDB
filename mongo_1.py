#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo


# In[3]:


client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')  # client will interact with database 


# In[4]:


database=client['Employee']  # database name 
empinfo=database.employee_information  # collection name 


# In[5]:


record={
    'name':'Ganesh Raj',
    'age':21,
    'gender':'M'
}


empinfo.insert_one(record) # to insert one record to collection


# In[7]:


records=[
    {
        'f_name':'Valayapathy',
        'l_name':'V',
        'age':55
    },
    {
        'f_name':'Rajeswarie',
        'l_name':'V',
        'age':45
    },
    {
        'f_name':'Harish',
        'l_name':'V',
        'age':19
    },
    {
        'f_name':'Ganesh Raj',
        'l_name':'V',
        'age':21
    }
    
]


empinfo.insert_many(records)    # to insert many records 


# In[8]:


# queries 

# to ge the first doc in collection 

empinfo.find_one()


# In[10]:


# to get all the records      ----  select * from table_name

empinfo.find()  # type of curser 


# In[12]:


for rec in empinfo.find():
    print(rec)
    print()


# In[13]:


# to write a query we have to use {} 

for rec in empinfo.find({'f_name':'Ganesh Raj'}):
    print(rec)


# In[17]:


# $in -- ( fetch ages in 19,21,.....)   
# simply same as for i in list


for rec in empinfo.find({'age':{'$in':[19,21,45]}}):    
    print(rec)


# In[18]:


# less than --- $lt

for rec in empinfo.find({'age':{'$lt':46}}):  # this fetches all rec where age less than 46
    print(rec)


# In[22]:


# $lt with and operation (,)

for rec in empinfo.find({'l_name':'V','age':{'$lt':46}}):
    print(rec)


# In[23]:


# using or operation 


for rec in empinfo.find({'$or':[{'f_name':'Ganesh Raj'},{'age':45}]}):
    print(rec)


# In[25]:


# fetching all records using or and less than 


# instead of $or we can also use $and

for rec in empinfo.find({'$or':[{'f_name':'Ganesh Raj'},{'age':{'$lt':60}}]}):
    print(rec)


# In[26]:


for rec in empinfo.find({'$and':[{'f_name':'Ganesh Raj'},{'age':{'$lt':60}}]}):
    print(rec)


# In[ ]:





# In[27]:


# CEATING NEW COLLECTIONS FROM SAME DATABASE 

store=database.stores # collection name 




# In[28]:


# creating nested recordssss

store.insert_many( [
   { 'item': "journal", 'qty': 25, 'size': { 'h': 14, 'w': 21,'uom': "cm" }, 'status': "A" },
   { 'item': "notebook", 'qty': 50,'size': { 'h': 8.5, 'w': 11,'uom': "in" },'status': "A" },
   { 'item': "paper", 'qty': 100, 'size': { 'h': 8.5, 'w': 11,'uom': "in" },'status': "D" },
   { 'item': "planner", 'qty': 75, 'size': { 'h': 22.85,'w': 30,'uom': "cm" },'status': "D" },
   { 'item': "postcard", 'qty': 45, 'size': { 'h': 10, 'w': 15.25,'uom': "cm" },'status': "A" }
]);


# In[30]:


# fetching the value of records with size -----


for records in store.find({'size': { 'h': 14, 'w': 21,'uom': "cm" }}):
    print(records)


# In[32]:


for records in store.find({'size': {'w': 21,'uom': "cm" }}):
    print(records)


# In[ ]:




