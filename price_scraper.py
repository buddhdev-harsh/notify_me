import requests
from bs4 import BeautifulSoup
import smtplib
import json
import re
##############################################

class scrapit():
    
    def __init__(self, query, price):
        self.query = query
        self.price = price

    def send_mail(self,product_body):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('harahismast@gmail.com', 'harshzxcvbnmlpoiuytrewqaz')
        subject = 'price fell down\n'
        body = self.query

        # product_body = 'price'+product_dict['price']+'brand_name'+product_dict['brand_name']+'product_name'+ product_dict['product_name']

        msg = "Subject: "+subject+"\n "+body+"\n"+product_body
        print(msg)

        server.sendmail(
            'harahismast@gmail.com',
            'ht50159@gmail.com',
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
        product_script = product_script.text.replace(" ","").replace("\n","").replace("\t","")

        product_json = json.loads(product_script)

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
        print(product_body)
        print("\n\n",type(price)," ",type(self.price) ,"\n\n")
        if(price < self.price):
            self.send_mail(product_body)
        else:
            print('no mail')

            



url = input('enter the url of product you want to track price for:')
price = int(input('enter the price you want your product to be notify when it euqal to or less than it'))


res = scrapit(url,price)
res.query_search_scrap()
