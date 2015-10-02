import requests
import datetime

from settings import key_plats,key_departures

def sites(searchstring):
    url = "http://api.sl.se/api2/typeahead.json?key={key}&searchstring={searchstring}"

    # download the page from trafiklab
    resp = requests.get(url.format(key=key_plats,searchstring = searchstring))



    return  resp.json()['ResponseData']

def departures(siteid):

    url = "http://api.sl.se/api2/realtimedepartures.json?key={key}&siteid={siteid}&timewindow=60"

    resp = requests.get(url.format(key=key_departures,siteid = siteid))


    return resp.json()['ResponseData']


def trains(siteid):
    trainlist=[]

    #for train in departures(siteid)['Buses']:
    #     t={}
    #     t['Destination'] =   train['Destination']
    #     t['LineNumber']  =   train['LineNumber']
    #     t['TimeToGo']  =    #minutes to go
    #     t['Late']  =    # true or false if late



    #     expected =datetime.datetime.strptime(train['ExpectedDateTime'] , '%Y-%m-%dT%H:%M:%S')
    #     TimeToGo = expected - datetime.datetime.now()
    #
    #
    #
    #     t['TimeToGo']  =  train[str(TimeToGo.total_seconds())]
    #
    #     trainlist.append(t)
    #
    #
    #
    # return trainlist
    return   departures(siteid)['Buses']


#{u'TimeTabledDateTime': u'2015-10-02T11:28:00',
# u'Destination': u'Geneta (Scaniarinken)',
#  u'DisplayTime': u'7 min',
# u'StopPointNumber': 75138,
#  u'ExpectedDateTime': u'2015-10-02T11:31:00',
#  u'TransportMode': u'BUS',
#  u'Deviations': None,
# u'GroupOfLine': None,
# u'StopAreaName': u'S\xf6dert\xe4lje hamn',
# u'SiteId': 9521,
#  u'LineNumber': u'754',
# u'StopAreaNumber': 75138,
#  u'StopPointDesignation': u'D',
# u'JourneyDirection': 2}