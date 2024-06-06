from flask import Flask
from flask import request
from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

load_dotenv()
baseURL: str = os.environ.get('API_URL')
apiKey: str = os.environ.get('API_KEY')

headers = {'Accept': 'application/json'}

# Games route
@app.get('/games')
def get_games():
  endpoint = '/games'
  params = {'key': apiKey}
  params.update(request.args) # The URL query args

  res = requests.get(baseURL + endpoint, headers=headers, params=params)

  return res.json()