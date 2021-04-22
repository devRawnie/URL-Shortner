from requests import post
from json import dumps, load

def shorten(url):
    if url is None or len(url) < 15:
        print("Error: Invalid/Empty URL passed")
        return None
    linkRequest = {
    "destination": url
    , "domain": { "fullName": "rebrand.ly" }
    # , "slashtag": "A_NEW_SLASHTAG"
    # , "title": "Rebrandly YouTube channel"
    }
    try:
        with open("keys.json") as f:
            keys = load(f)
    except Exception as e:
        print("Error: Could not load keys file\n %s" % str(e))
        return None

    requestHeaders = {
    "Content-type": "application/json",
    "apikey": keys["api_key"]
    }

    r = post("https://api.rebrandly.com/v1/links", 
        data = dumps(linkRequest),
        headers=requestHeaders)

    if r.status_code == 200:
        link = r.json()
        print("Status: Created short url successfully")
        return link["shortUrl"]
    else:
        print("Error: Invalid response recieved", link)
        return None
