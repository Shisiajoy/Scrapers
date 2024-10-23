import requests
from bs4 import BeautifulSoup

# Define the headers to mimic a browser visit to allow for web scraping
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

# the URL of the page to scrape
url = 'https://www.jumia.co.ke/flash-sales/'

# Send a GET request to the URL 
response = requests.get(url , headers = headers)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the products on the page
products = soup.find_all('div', class_='prd')

# Loop through each product 
for product in products:
    product_name = product.find('h3', class_='name').text.strip()
    brand_name = product.find('h3', class_='brand-name').text.strip()
    price = product.find('div', class_='prc').text.strip()
    discount = product.find('div', class_='s-prc-w').text.strip()
    review_count = product.find('div', class_='rev').text.strip()
    rating = product.find('div', class_='rating').text.strip() # Correct class for rating

       # Print the extracted information
    print('Product Name:', product_name)
    print('Brand Name:', brand_name)
    print('Price:', price)
    print('Discount:', discount)
    print('Review Count:', review_count)
    print('Rating:', rating)
