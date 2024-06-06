from flask import Flask
from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

load_dotenv()
baseURL = os.environ.get('API_URL')
apiKey = os.environ.get('API_KEY')
endpoint = "/games"
headers = {'Accept': 'application/json'}
payload = {'key': apiKey}

res = requests.get(baseURL + endpoint, headers=headers, params=payload)

@app.get('/')
def testing():
  return res.json()

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)