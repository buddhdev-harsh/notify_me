import requests
from bs4 import BeautifulSoup
import smtplib
##############################################

class scrapit():
    
    def __init__(self, query, price):
        self.query = query
        self.price = price

    def query_search_scrap(self):
        headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

        req = requests.get(self.query,headers = headers)
        soup = BeautifulSoup(req.content , 'html.parser')
        
        outer_table = soup.find("h1",{"class":"pdp-title"}).text
        print(outer_table)
        #edit the above code for price extraction on myntra
        price = float(price[2:5])
        print(price)
        print(title)
        if(price < self.price):
            send_mail()
        else:
            print('no mail')

    def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('harahismast@gmail.com', 'harshzxcvbnmlpoiuytrewqaz')
    subject = 'price fell down'
    body = self.query
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'harahismast@gmail.com',
        'ht50159@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')
    server.quit()
            



url = input('enter the url of product you want to track price for:')
price = int(input('enter the price you want your product to be notify when it euqal to or less than it'))


res = scrapit(url,price)
res.query_search_scrap()
