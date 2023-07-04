import sys
sys.path.append("/home/ajay/Listed_2/src")
from scrapper import Scrapper_Web
from bs4 import BeautifulSoup



if __name__ == "__main__":
    scrapper = Scrapper_Web(15, "site:youtube.com openinapp.co")
    links = scrapper.get_url()
    print(links)