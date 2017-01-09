electrician = ['electrician','lights','wiring','socket','power','flickering','flicker','circuit']
plumber = ['plumber','faucet', 'pipe', 'toilet', 'plumbing','leak']
time = ['timely', 'fast', 'quick', 'wait','slow','time','arrived','arrive','come','go','went','going','reliable','wait','efficient','within','convenient']
friendly = ['friendly','talked','nice','enjoy','enjoyable','talk','chat','went over','helped','help']
communicative = ['talked','talk','phone','call','called','email','promised','promise','say','said','saying','explain','chat']
quality = ['experience','experienced','well','good','perform','fix','fixed','install','installed','service','recommend',]

electrician = [name.upper() for name in electrician]
plumber = [name.upper() for name in plumber]
time = [name.upper() for name in time]
friendly = [name.upper() for name in friendly]
communicative = [name.upper() for name in communicative]
quality = [name.upper() for name in quality]
def clean(str):
    str = str.upper()
    strArray = [char for char in str if ord(char)>=65 and ord(char)<=90]
    return "".join(strArray)

def match(arr1, arr2):
    for item in arr2:
        if item in arr1:
            return True
            break
    return False

def filter(reviews):
    for rev in reviews:
        words = rev['review'].split(' ')
        words = [clean(word) for word in words]
        if not match(words,time):
            reviews.remove(rev)
    return reviews
def filterCondition(review,list):
    words = review.split(' ')
    words = [clean(word) for word in words]
    return match(words,list)
def searchTerm(str):
    search = [clean(word) for word in str.split(' ')]
    if match(search,electrician):
        return 'electrician'
    elif match(search,plumber):
        return 'plumber'
    return str
