import flask
import numpy as np
import pandas as pd
from copy import deepcopy
import json

# Initialize the app
app = flask.Flask(__name__)

@app.route("/")
def viz_page():
    with open("index.html", 'r') as viz_file:
        return viz_file.read()

@app.route("/relations", methods=["POST"])
def get_ends():
    data = flask.request.json
    print(data)
    x = data["station"]
    print(x)
    data = pd.read_json('relations.json')
# # the startstation has to come from the index.html
    ends = data[x].loc['endstations']
    df_ends = pd.DataFrame.from_dict(ends, orient='index')
    # the end df has to be sent to d3, and dots made on this df
    out_json = df_ends.to_json(orient='records')  
    print(out_json)
    return out_json

#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
app.run(port=5002,debug=True)
