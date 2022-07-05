import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    '''
    get the subdomain from the request and use it as the url, make a request to the url, and return the response
    '''
    subdomain = request.subdomain
    url = f'https://{subdomain}.ssrf.io/'
    response = requests.get(url)
    return response