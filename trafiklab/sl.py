import requests

from settings import key_plats

def sites(searchstring):
    url = "api.sl.se/api2/typeahead.json?key={key}&searchstring={searchstring}"

    # download the page from trafiklab
    resp = requests.get(url.format(key=key_plats,searchstring = searchstring))



    return  "hej"
