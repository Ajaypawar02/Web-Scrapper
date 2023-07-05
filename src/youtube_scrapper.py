import os
import googleapiclient.discovery

# Set up the YouTube Data API client

def scapping_youtube():
  api_service_name = "youtube"
  api_version = "v3"
  api_key = "AIzaSyBZI7KXEAtsLC5hNT-bq6g4Clj3lqEIofc"  # Replace with your own API key
  youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)
  links = []
  # Perform a searc
  results_per_page = 50
  max_results = 10000

  pages = max_results // results_per_page

  for page in range(pages):
    search_query = "https://openinapp.com"
    request = youtube.search().list(
        part="snippet",
        q=search_query,
        type="video",
        maxResults=50, # You can adjust the maximum number of results as needed
        pageToken = None if page == 0 else next_page,
    )
    response = request.execute()
    next_page = response.get("nextPageToken")

    # Extract the video IDs and construct the YouTube links
    youtube_links = []
    for item in response["items"]:
        video_id = item["id"]["videoId"]
        youtube_link = f"https://www.youtube.com/watch?v={video_id}"
        youtube_links.append(youtube_link)

    # Print the YouTube links
    for link in youtube_links:
        links.append(link)

  return links
