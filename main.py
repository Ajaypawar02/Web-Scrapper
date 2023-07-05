import sys
sys.path.append("/home/ajay/Listed_2/src")
from scrapper import Scrapper_Web
from bs4 import BeautifulSoup
from youtube_scrapper import scapping_youtube



if __name__ == "__main__":
    scrapper = scapping_youtube()
    df = pd.DataFrame(scrapper, columns = ["Links"])
    df.iloc[:10000]
    df.to_csv("youtube_liinks_10000.csv", index = False)
    print(df)
