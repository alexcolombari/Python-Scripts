#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import smtplib
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def check_price(desired_value):
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    original_price = soup.find("span", {"class": "priceBlockStrikePriceString"}).get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price = float(price[2:4].strip())
    print('Checking price for ' + title.strip())
    
    send_mail(price, original_price) if converted_price < desired_value else 'Price doesnt fallen down yet'

def send_mail(price, original_price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login(email, passwd)

    hour = datetime.now()
    subject = '[ALERT] Price fall down!'
    body = 'Original price: {}\nCurrent price: {}\nCheck the Amazon link: {}\n\n\n\
Sended in {} from Python Script'.format(original_price, price, URL, hour)
    msg = "Subject: {}\n\n {}".format(subject, body)

    server.sendmail(email, email, msg)
    print('Email has been sent!')
    server.quit()

if __name__ == '__main__':
    '''
    Update some variables to use this code:
    email --> use Gmail
    URL --> Insert the URL of your desired product from the Amazon's site
    headers --> google for 'my user agent' and copy the answer
    '''

    URL = 'https://www.amazon.com.br/Until-Down-Padr%C3%A3o-PlayStation-4/dp/B0754JJQHJ'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

    email = raw_input('Enter with your email: ')
    passwd = raw_input('Password: ')
    pay_value = input('Maximum amount to pay: ')
    wait_time = input('Time for each check (in seconds): ')
    os.system('clear' if os.name == 'posix' else 'cls') # Clear terminal window

    print('Checking price every {} seconds').format(wait_time)
    while True:
        check_price(pay_value)
        time.sleep(wait_time) # Time to check the prices (in seconds)
