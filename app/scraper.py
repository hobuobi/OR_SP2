from lxml import html
import requests

def scrape(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    results = []
    reviews = tree.xpath("//div[@class='review-content']/p/text()")
    for rev in reviews:
        results.append(rev)
    return results
def scrape10(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    results = []
    reviews = tree.xpath("//div[@class='review-content']/p/text()")
    for rev in reviews:
        results.append(rev)
    return results[:10]
