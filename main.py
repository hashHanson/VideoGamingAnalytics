import YoutubeSearch as ytSearch
import jsonFlatten
import pandas as pd
import json


if __name__=='__main__':
    result = ytSearch.youtube_search("Talking Tom","channel")
    flattenJson = jsonFlatten.flatten_json(result)  
    with open("/home/hashhanson123/VideoGamingAnalytics/OutputFiles/TalkingTom.json","w") as file:
        json.dump(flattenJson,file)

    pdResult = pd.read_json("/home/hashhanson123/VideoGamingAnalytics/OutputFiles/TalkingTom.json")
    print(pdResult)
