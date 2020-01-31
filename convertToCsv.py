import json
import YoutubeSearch as ySearch


def JsonToCSV(ytItem, ytItemType, fileName):
    jsonfile= "/home/hashhanson123/VideoGamingAnalytics/OutputFiles/" + fileName + ".json"
    csvfile= "/home/hashhanson123/VideoGamingAnalytics/OutputFiles/" + fileName + ".csv"
    result = ySearch.youtube_search(ytItem, ytItemType)
    with open(jsonfile, "w") as file:
        json.dump(result, file)
