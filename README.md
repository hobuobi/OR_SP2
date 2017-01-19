# PRISM
### A platform for generating a multidimensional view of a service-person's reputation. 

This is a project created from insights developed at the IDEO CoLab, around the concept of an open reputation. 

#### To run: 

Make sure you have [Python 3.5](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) installed. 

1) Clone the repository using the address provided, then run `pip install -r requirements.txt`.

2) Get a Yelp API key by registering your clone of the application [here.](https://www.yelp.com/developers/documentation/v2/overview)

3) Create a `config.json` file in the app folder and place your authentication keys in the following format: 

```javascript 
{
    "consumer_key": YOUR_CONSUMER_KEY,
    "consumer_secret": YOUR_CONSUMER_SECRET,
    "token": YOUR_TOKEN,
    "token_secret": YOUR_TOKEN_SECRET
}
```
4) Save and run the command `python run.py` in your terminal. It should run at `localhost:5000` in your browser.

#### In use:

Just type out whatever the home repair situation is in natural language, and our service will scrape through reviews and pick out a serviceman that's right for your purposes. 

A few things to consider: 

1) This is a prototype. Thus, certain phrases will likely (definitely) trigger the preferences automatically, as is its ideal function. 
For example, typing things like "asap" or "soon" should trigger the "PROMPT" preference, and "nice" will trigger the "FRIENDLY" one.

2) It takes a long time for all of this to be scraped and analyzed, partially because we're relying on an outside API (the Project Oxford Text Analytics API) to perform sentiment analysis. 
Thus, if you really want the results in a minute or less, manually reduce the number of businesses considered in the search in `views.py` and the number of blocks of reviews tackled in `scraper.py`.
