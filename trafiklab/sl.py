import requests

from settings import key_plats

def sites(searchstring):
    url = "http://api.sl.se/api2/typeahead.json?key={key}&searchstring={searchstring}"

    # download the page from trafiklab
    resp = requests.get(url.format(key=key_plats,searchstring = searchstring))



    return  resp.json()['ResponseData']

def departures(siteid):
    # 9521
    pass



