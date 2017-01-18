# yelp stuff
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import io, os, json
'''
with io.open('app/config.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)
'''
auth = Oauth1Authenticator(
    consumer_key=os.environ['CONSUMER_KEY'],
    consumer_secret=os.environ['CONSUMER_SECRET'],
    token=os.environ['TOKEN'],
    token_secret=os.environ['TOKEN_SECRET']
)

client = Client(auth)
