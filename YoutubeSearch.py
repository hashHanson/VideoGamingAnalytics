from apiclient.discovery import build
from apiclient.errors import HttpError
#from oauth2client.tools import argparser

DEVELOPER_KEY = "AIzaSyAKmVOTjE4D4Tu059cnFi0XiP1sbF4xMfI"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"




def youtube_search(q,Type="video", max_results=50,order="relevance", token=None, location=None, location_radius=None):

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=q,
    pageToken=token,
    type = Type,
    order = order,
    part="id,snippet",
    maxResults=max_results,
    location=location,
    locationRadius=location_radius

  ).execute()



  videos = []
  channels = []
  playlists = []

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append(search_result)
    elif search_result["id"]["kind"]=="youtube#channel":
        channels.append(search_result)
    elif search_result["id"]["kind"]=="youtube#playlist":
        playlists.append(search_result)
  try:
      nexttok = search_response["nextPageToken"]
      return(nexttok, videos,channels,playlists)
  except Exception as e:
      nexttok = "last_page"
      return(nexttok, videos, channels,playlists)


'''
def geo_query(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    video_response = youtube.videos().list(
        id=video_id,
        part='snippet, recordingDetails, statistics'

    ).execute()

    return video_response
'''
