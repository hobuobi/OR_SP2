from flask import Flask, render_template, request, url_for
from app import app, yelp, sentiment, scraper, revFilter

@app.route('/')
@app.route('/index')
def index():
##    db = get_db()
##    cur = db.execute('select title, text from entries order by id desc')
##    entries = cur.fetchall()
    return render_template('index.html')

@app.route('/hello/', methods=['POST'])
def searchResults():
    term=request.form['searchterm']
    term = revFilter.searchTerm(term)
    params = {
        'term': term
    }
    print(term)
    response = yelp.client.search('Boston', **params)
    businesses = response.businesses
    reviews = []
    allBiz = []
    print(businesses)
    for biz in businesses[:5]:
        reviews = []
        for rev in scraper.scrape10(biz.url):
            flatten = lambda l: [item for sublist in l for item in sublist]
            for sentence in flatten([item.split("!") for item in rev.split(".")]):
                if revFilter.filterCondition(rev):
                    reviews.append({
                        'review': sentence,
                        'sentiment': sentiment.analyze(sentence)
                    })
        print(reviews)
        allBiz.append({
            biz.name : reviews,
            'avgsent': sentimentAvg(reviews)
        })
    return render_template('form_action.html', term=term,results=allBiz)
def sentimentAvg(sent):
    total = 0
    for x in sent:
        if x['sentiment'] is not None:
            total = total+x['sentiment']
    return total/len(sent)
