from urllib.parse import unquote
import pandas as pd
import requests
from bs4 import BeautifulSoup

class Scrapper_Web:
  def __init__(self, top_k : int , keywords: str):
    self.top_k = top_k
    self.keywords = keywords
    """ Put the keywords here ie  site:youtube.com openinapp.co"""
    # self.url = f"https://www.google.com/search?q={self.keywords}"
    # self.page_number = 1

  def get_url(self):

    try:
      page_number = 1
      count = 0
      CountsCount = 0
      df = pd.DataFrame(columns=['Link'])
    
      for i in range(0, self.top_k):
        cot = 0
        start_index = (page_number - 1) * 10
        urls = f"https://www.google.com/search?q={self.keywords}&start={start_index}"
        response = requests.get(urls)
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all the search results (links)
        search_results = soup.find_all('a')
        # Extract the URLs
        for result in search_results:
            link = result.get('href')
            if link.startswith('/url?q='):
                # Extract the actual URL from the Google Search result
                url = link[7:]
                # Remove any additional parameters
                url = url.split('&')[0]
                url = unquote(url)

                if "www.youtube.com" in url:
                  df.loc[len(df)] = url
                  count += 1
                  cot += 1
        page_number += 1

        if cot == 0:
          break
        if cot == 2:
          CountsCount += 1
        if CountsCount >= 2:
          break

      
      return df
    
    except Exception as e:
      raise e




    