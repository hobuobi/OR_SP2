import http.client, urllib.request, urllib.parse, urllib.error, base64, json
def analyze(str):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '459870a2c95c46c88895ed2537388cb6 ',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'numberOfLanguagesToDetect': '{integer}',
    })
    body = '{"documents":[{"id":"1","text":"'+str+'"}]}'
    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        senti = json.loads(data.decode("utf-8"))
        return senti['documents'][0]['score'] # returns the score of the input
    except Exception as e:
        print('err: ',str)
