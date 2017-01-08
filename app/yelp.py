# yelp stuff
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import io, os, json

with io.open('app/config.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)
