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
params = {'key': apiKey}

# Generic route for collections
@app.get('/<endpoint>')
def get_all(endpoint):
  params.update(request.args) # The URL query args
  res = requests.get(baseURL + request.path, headers=headers, params=params)
  return res.json()

# Route for retrieving singular game
@app.get('/game/<id>')
def get(id):
  endpoint = '/games'
  url = baseURL + endpoint + '/' + id
  res = requests.get(url, headers=headers, params=params)
  return res.json()