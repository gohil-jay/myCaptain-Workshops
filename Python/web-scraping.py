import requests
from bs4 import BeautifulSoup
import pandas
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", helps="Enter the number of pages to parse", type = int)
parser.add_argument("--dbname", helps="Enter the number of pages to parse", type = int)
args = parser.parse_args()

max_page = args.page_num_max
url = "URL goes here"
scrapped_list = []
