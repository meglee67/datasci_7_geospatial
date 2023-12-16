## GCP
# https://developers.google.com/maps/documentation/geocoding/start
# https://developers.google.com/maps/documentation/geocoding/requests-reverse-geocoding

# this code is a combo of (https://github.com/hantswilliams/HHA_507_2023/blob/main/WK7/code_7/geocoding_gcp/interactive_class.py) and https://github.com/hantswilliams/HHA_507_2023/blob/main/WK7/code_7/geocoding_gcp/geocoding.py
import requests
import pandas as pd
import numpy as np
import re
import geopandas as gpd
import matplotlib.pyplot as plt
import urllib.parse
import os
from dotenv import load_dotenv
import json

load_dotenv()
api_key = os.getenv("GOOGLE_MAPS_API")

search = 'https://maps.googleapis.com/maps/api/geocode/json?address='


# convert location to url friendly string
location = urllib.parse.quote(location)
url = search + location + '&key=' + api_key

# get response
response = requests.get(url)

# get json
json = response.json()
