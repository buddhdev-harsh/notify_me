import requests
from bs4 import BeautifulSoup
import smtplib
import json
import re

##############################################

class scrapit():
    
    def __init__(self, query, price ,email):
        self.query = query
        self.price = price
        self.email = email

    def send_mail(self,product_body):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('harahismast@gmail.com', 'harshzxcvbnmlpoiuytrewqaz')
        subject = 'price fell down\n'
        body = self.query


        msg = "Subject: "+subject+"\n "+body+"\n"+product_body

        server.sendmail(
            'harahismast@gmail.com',
            self.email,
            msg
        )
        print('HEY EMAIL HAS BEEN SENT')
        server.quit()


    def query_search_scrap(self):
        headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

        req = requests.get(self.query,headers = headers)
        soup = BeautifulSoup(req.content , 'html.parser')
        
        script_contents = soup.find_all('script')
    
        product_script = script_contents[1]
        json_product = product_script.string.replace(" ","").replace("\n","").replace("\t","")
        product_json = json.loads(json_product)

        price = int(product_json['offers']['price'])
        brand_name = product_json['brand']['name']
        product_name = product_json['name'][len(brand_name):]

        product_name = " ".join(re.findall('[A-Z][^A-Z]*',product_name))

        product_dict = {
            'price':price,
            'brand_name':brand_name,
            'product_name': product_name
        }

        product_body = 'price : '+str(price)+'\nbrand_name : '+brand_name+'\nproduct_name : '+ product_name
        
        if(price < self.price):
            self.send_mail(product_body)
        else:
            print('no price updates')

            



url = input('enter the url of product you want to track price for: ')
price = int(input('enter the price you want your product to be notify when it euqal to or less than it: '))
email = input('enter your email: ')

res = scrapit(url, price, email)
res.query_search_scrap()
