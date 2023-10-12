import lxml
import requests
from bs4 import BeautifulSoup

amazon_product_link = "https://www.amazon.com/Nike-Basketball-Trainers-AR3762-Sneakers/dp/B07ZTW6M7Z/ref=sr_1_2?crid=1HKGAGOT1FOZE&keywords=nike%2Bmens%2Bjordan&qid=1696767117&sprefix=nike%2Bmens%2Bjorda%2Caps%2C320&sr=8-2&th=1&psc=1"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

}
response = requests.get(amazon_product_link, headers=headers)

web_formatted_text = response.text

soup = BeautifulSoup(web_formatted_text, "lxml")

Nike_Shoes_Price = soup.find('span', class_="a-price-whole")
Nike_Shoes_Price_text = Nike_Shoes_Price.getText()
float_Nike_Shoes_Price_text = float(Nike_Shoes_Price_text)


if float_Nike_Shoes_Price_text >= 13.1:
    print("purcahse")

elif float_Nike_Shoes_Price_text < 13.1:
    print("nope not rn")
