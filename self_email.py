# -*- coding: utf-8 -*-
"""
Created in 2023

@author: Quant Galore
"""
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def send_message(message, subject):
    

    
    recipient = EMAIL
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
    
    subject = subject
    body = message
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(from_addr = auth[0], to_addrs = recipient, msg = message)
