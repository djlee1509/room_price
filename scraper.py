import requests
from bs4 import BeautifulSoup
import smtplib
import time

start = time.time()
print("This is the result: -")



headers = {
  "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

def check_price():
  items = 10
  while items <= 1000:

    URL = 'https://www.spareroom.co.uk/flatshare/?offset=' + str(items) + '&search_id=914373898&sort_by=age&mode=list'

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

  # locations = soup.find_all('span', attrs={'class':'listingLocation'})

    prices = soup.find_all('strong', attrs={'class':'listingPrice'})

  # for location in locations:
  #   area = location.get_text()
  #   print(area)

    for price in prices:
      rent = price.get_text().strip()
      print(rent)

    items += 10

check_price()

end = time.time()
print("{0:.2f}".format(end - start))
