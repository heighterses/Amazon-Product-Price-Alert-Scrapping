from bs4 import BeautifulSoup

html = '''
<div class="a-section a-spacing-none aok-align-center">
    <span class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay" data-a-size="xl" data-a-color="base">
        <span class="a-offscreen">$135.92</span>
        <span aria-hidden="true">
            <span class="a-price-symbol">$</span>
            <span class="a-price-whole">135<span class="a-price-decimal">.</span></span>
            <span class="a-price-fraction">92</span>
        </span>
    </span>
    <span id="taxInclusiveMessage" class="a-size-mini a-color-base aok-align-center aok-nowrap">  </span>
</div>
'''

soup = BeautifulSoup(html, 'html.parser')

# Find the element with the class "a-price-whole" and extract the text
price_whole = soup.find('span', class_='a-price-whole').get_text()

print(price_whole)
