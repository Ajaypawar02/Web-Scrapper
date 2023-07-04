import requests
from bs4 import BeautifulSoup

search_query = "site:youtube.com openinapp.co"
page_number = 400
start_index = (page_number - 1) * 10
url = f"https://www.google.com/search?q={search_query}&start={start_index}"

# Send a GET request to the 2nd page of Google Search
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the search results (links)
search_results = soup.find_all('a')
print(search_results)

# Extract the URLs
for result in search_results:
    link = result.get('href')
    # print(link)
    if link.startswith('/url?q='):
        # Extract the actual URL from the Google Search result
        url = link[7:]
        # Remove any additional parameters
        url = url.split('&')[0]
        # Print the URL
        print(url)
