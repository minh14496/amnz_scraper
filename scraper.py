import requests
from bs4 import BeautifulSoup #this need to download python3 doesn't have it
import smtplib #lib for SMTP protocol client for sending email to any internet machine
import time

# Scrapping price from amazon learn to use beautifulsoup to grap html elements from website and smtplib to send email
URL='https://www.amazon.com/Samsung-Enhanced-Tracking-Analysis-Coaching/dp/B07VKQ54V1/ref=sr_1_2?keywords=galaxy%2Bwatch%2Bactive%2B2%2Blte&qid=1578964458&sr=8-2&th=1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}


page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'lxml') #need to install a parser here, parser lib choice: lxml

title = soup.find(id="productTitle").get_text()

def check_price():
    price = soup.find(id="priceblock_ourprice").get_text()

    convert_price = float(price[1:len(price)])

    if convert_price > 240:
        send_mail()

    print(convert_price)

#for sending email using smtplib, with google need to create an app password
#google for it then using the app pw generate and put it in here
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587) #for the number and smtp name Google smtp for gmail
    #these are for contacting the server and gmail
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('minh14496@gmail.com','pw is here') #email and generated pw
    subject = 'Price go down'
    body = title +'\n'+ 'Check the amazon link https://www.amazon.com/Samsung-Enhanced-Tracking-Analysis-Coaching/dp/B07VKQ54V1/ref=sr_1_2?keywords=galaxy%2Bwatch%2Bactive%2B2%2Blte&qid=1578964458&sr=8-2&th=1'
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'minh14496@gmail.com',
        'minh14496@gmail.com',
        msg
    )
    print('email has been sent')

while(True):
    check_price()
    time.sleep(3600*10)