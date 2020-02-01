import json
import YoutubeSearch as ySearch
import jsonFlatten as jf
import pandas as pd
from datetime import datetime
import dateutil.parser


def JsonToCSV(ytItem, ytItemType, fileName):
    jsonfile = "/home/hashhanson123/VideoGamingAnalytics/OutputFiles/" + fileName + ".json"
    csvfile = "/home/hashhanson123/VideoGamingAnalytics/OutputFiles/" + fileName + ".csv"
    result = ySearch.youtube_search(ytItem, ytItemType)
    jsonOnly = result[2][0]
    #flattenJson = jf.flatten_json(jsonOnly)
    with open(jsonfile, "w") as file:
        json.dump(jsonOnly, file)

    json_df = pd.read_json(jsonfile)
    csv_df = json_df.to_csv(csvfile)
