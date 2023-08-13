import requests
from bs4 import BeautifulSoup
import csv
url = 'https://www.flipkart.com/search?q=purifier&sid=j9e%2Cabm%2Ci45&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=purifier%7CWater+purifiers&requestId=b98bf101-3042-496b-8a72-6b0fc5c672f0&as-searchtext=puri'

# Send a GET request to the URL
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
purifier_containers = soup.find_all('div', {'class': '_2kHMtA'})
# Create a CSV file to store the product details
csv_filename = 'flipkart_purifier_products.csv'

# Open the CSV file in write mode
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    # Create a CSV writer
    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(['Product Name', 'Price', 'Rating', 'Features'])

    # Loop through epurifierh purifier container and extrpurifiert product details
    for purifier in purifier_containers:
        try:
            product_name = purifier.find('div', {'class': '_4rR01T'}).text
            price = purifier.find('div', {'class': '_30jeq3'}).text
            rating = purifier.find('div', {'class': '_3LWZlK'}).text
            features = purifier.find('ul', {'class': '_1xgFaf'}).text.strip()

            # Write the product details to the CSV file
            csv_writer.writerow([product_name, price, rating, features])
        except AttributeError:
            continue

print('Scraping and CSV export completed successfully.')