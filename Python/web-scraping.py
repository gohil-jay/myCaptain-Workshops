import requests
from bs4 import BeautifulSoup
# import pandas (only for CSVs)
import argparse
import web-sql

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", helps="Enter the number of pages to parse", type = int)
parser.add_argument("--dbname", helps="Enter the number of pages to parse", type = int)
args = parser.parse_args()

max_page = args.page_num_max
url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
scrapped_list = []
web-sql.connect(args.dbname)

for page_num in range(1, max_page+1):
  final_url = url + str(page_num)
  print("Get from URL", + final_url)
  req = requests.get(final_url)
  content = req.content
  
  soup = BeautifulSoup(content, "html.parser")
  hotels = soup.find_all("div", {"class": "hotelCardListing"})
  print(hotels)
