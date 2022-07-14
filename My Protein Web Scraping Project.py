#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib


# In[117]:


# Connect to Website and pull in data

URL = 'https://us.myprotein.com/sports-nutrition/the-plant-protein/12061084.html'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

page = requests.get(URL, headers = headers)

soup1 = BeautifulSoup(page.content, "html.parser")


soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find("h1", {"class": "productName_title"}).get_text()

price = soup2.find("p", {"class":"productPrice_price"}).get_text()

# print(title)
# print(price)


# In[72]:


# #Put into a more organized format
# soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
# print(soup2)


# In[135]:


# #Get Title of Product
title = soup2.find("h1", {"class": "productName_title"}).get_text()
print(title)


# In[136]:


#Get Price of Product
# price = soup2.find('span class' =='a-offscreen').get_text()
# print(price)
# soup.find("div", {"class":"real number"})['data-value']

price = soup2.find("p", {"class":"productPrice_price"}).get_text()
print(price)


# In[137]:


#strip "$" from price to make it more usable for CSV format.
price = price.strip()[1:]
title = title.strip()
print(title)
print(price)


# In[138]:


#import date to add to CSV data
import datetime
today = datetime.date.today()
print(today)


# In[141]:


#create a CSV to input data into
import csv

header =['Title', 'Price', 'Date']
data = [title, price, today]

with open('PlantProteinDataSet.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

#type(data)


# In[148]:


#import as dataframe into Pandas
import pandas as pd

df = pd.read_csv(r'C:\Users\jobea\PlantProteinDataSet.csv')
            
print(df)


# In[147]:


#Now we are appending data to the CSV
#Ran this 6 times to test and get the data above

with open('PlantProteinDataSet.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[ ]:



def check_price():    
    URL = 'https://us.myprotein.com/sports-nutrition/the-plant-protein/12061084.html'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

    page = requests.get(URL, headers = headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find("h1", {"class":"productName_title"}).get_text()

    price = soup2.find("p", {"class":"productPrice_price"}).get_text()

    price = price.strip()[1:]
    title = title.strip()

    import datetime

    today = datetime.date.today()

    import csv
    
    header =['Title', 'Price', 'Date']
    data = [title, price, today]


    with open('PlantProteinDataSet.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
    if(price < 50):
        send_mail()


# In[ ]:


# Runs check price after a set time and inputs data into CSV.  It will check the price every day to see if it has changed.
while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd

df = pd.read_csv(r'C:\Users\jobea\PlantProteinDataSet.csv')
            
print(df)


# In[ ]:


# Automating this process to send myself an email when a price hits below a certain level.

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('jobeauthement@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Protein you want is below $50! Now is your chance to buy!"
    body = "Jobe, This is the moment we have been waiting for. Now is your chance to pick up your protein at a discount. Don't miss this opportunity! Link here: https://us.myprotein.com/sports-nutrition/the-plant-protein/12061084.html"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'jobeauthement@gmail.com',
        msg
     
    )

