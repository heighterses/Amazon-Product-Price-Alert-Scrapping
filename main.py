import lxml
import requests
from bs4 import BeautifulSoup

amazon_product_link = "https://www.amazon.com/dp/B0B6C76RQX/ref=syn_sd_onsite_desktop_0?ie=UTF8&psc=1&pd_rd_plhdr=t"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 "
                  "Safari/537.36"

}
response = requests.get(amazon_product_link, headers=headers)

web_formatted_text = response.text

soup = BeautifulSoup(web_formatted_text, "lxml")

Nike_Shoes_Price = soup.find_all(class_="a-price-whole")

for p in Nike_Shoes_Price:
    pro = p.getText()
    print(pro)
