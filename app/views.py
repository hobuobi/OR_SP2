from flask import Flask, render_template, request, url_for
from app import app, yelp, sentiment, scraper, revFilter
import unicodedata, os

conditions = [revFilter.time, revFilter.friendly, revFilter.communicative, revFilter.quality]

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route('/')
@app.route('/index')
def index():
##    db = get_db()
##    cur = db.execute('select title, text from entries order by id desc')
##    entries = cur.fetchall()
    return render_template('index.html')

@app.route('/results/', methods=['POST'])
def searchResults():
    preferences = {
        'timely' : 'avgTime' if request.form.get('timely') is not None else False,
        'communicative' : 'avgComm' if request.form.get('communicative') is not None else False,
        'quality' : 'avgQual' if request.form.get('quality') is not None else False,
        'friendly' : 'avgFrnd' if request.form.get('friendly') is not None else False
    }
    prefAdj = [request.form.get('timely'),request.form.get('communicative'),request.form.get('quality'),request.form.get('friendly')]
    search=request.form['search']
    term = revFilter.searchTerm(search)
    params = {
        'term': term
    }
    response = yelp.client.search('Boston', **params)
    businesses = response.businesses
    reviews = []
    allBiz = []
    for biz in businesses[:10]:
        reviews = []
        for rev in scraper.scrape10(biz.url):
            flatten = lambda l: [item for sublist in l for item in sublist]
            for sentence in flatten([item.split("!") for item in rev.split(".")]):
                sentence = unicodedata.normalize("NFKD", sentence)
                reviews.append({
                    'review': sentence,
                    'timely': sentiment.analyze(sentence) if revFilter.filterCondition(sentence,revFilter.time) else None,
                    'friendly': sentiment.analyze(sentence) if revFilter.filterCondition(sentence,revFilter.friendly) else None,
                    'communicative': sentiment.analyze(sentence) if revFilter.filterCondition(sentence,revFilter.communicative) else None,
                    'quality': sentiment.analyze(sentence) if revFilter.filterCondition(sentence,revFilter.quality) else None,
                    'sentiment': sentiment.analyze(sentence)
                })
        print(reviews)
        allBiz.append({
            'name' : biz.name,
            'number' : biz.phone,
            'reviews' : reviews,
            'avgSent': sentimentAvg(reviews,'sentiment'),
            'avgTime': sentimentAvg(reviews,'timely'),
            'avgComm': sentimentAvg(reviews,'communicative'),
            'avgQual': sentimentAvg(reviews,'quality'),
            'avgFrnd': sentimentAvg(reviews,'friendly')
        })
    pref_prime = 'avgSent'
    for pr,val in preferences.items():
        if(val is not False):
            pref_prime = val
            break
    averages = {
        'avgTime': 0,
        'avgComm': 0,
        'avgQual': 0,
        'avgFrnd': 0
    }
    for biz in allBiz:
        total = 0
        averages['avgTime'] += biz['avgTime']
        averages['avgComm'] += biz['avgComm']
        averages['avgQual'] += biz['avgQual']
        averages['avgFrnd'] += biz['avgFrnd']
    averages['avgTime'] /= len(allBiz)
    averages['avgComm'] /= len(allBiz)
    averages['avgQual'] /= len(allBiz)
    averages['avgFrnd'] /= len(allBiz)
    sortedBiz = sorted(allBiz, key= lambda biz: biz[pref_prime], reverse=True)
    topBiz = sortedBiz[0]
    pref = '/'.join([x for x in prefAdj if x is not None])
    return render_template('results.html', term=term,results=allBiz,top=topBiz,pref=pref,averages=averages)
def sentimentAvg(sent,filt):
    total = 0
    count = 0
    for x in sent:
        if x[filt] is not None:
            total = total+x[filt]
            count = count+1
    if total == 0:
        return 0
    else:
        return total/count
