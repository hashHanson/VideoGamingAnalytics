import pandas as pd
import convertToCsv as ctc
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello I like to make AI Apps'


@app.route('/output/<value>')
def pullfromYoutube(value):

    ctc.JsonToCSV(value, "channel", value)
    df = pd.read_csv(
        "/home/hashhanson123/VideoGamingAnalytics/OutputFiles/"+value+".csv")
    return jsonify(df.to_dict())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
