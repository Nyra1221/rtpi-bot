import urllib2, urllib, json, app
from app import *

def fetchtime(stopnum):
    try:
        val = int(stopnum)
    except ValueError:
        return "Stop numbers must be numeric!"

    if len(stopnum) > 6:
        return "This is not a valid stop number!"


    n = []
    data = "?stopid={}".format(stopnum)+"&format=json"
    content = "https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation"
    req = urllib2.urlopen(content + data + "?")
    i = 0 
    info = json.load(req)


    if len(info["results"]) == 0:
        return "Sorry, there's no real time info for this stop!"

    if len(info["results"]) > 5:
            while i < 5:
                n.append("Route:" + " " + str(info['results'][i]['route']) + " " + "to" + " " + str(info['results'][i]['destination']) + "\n" + "Due:" + " " + str(info["results"][i]["duetime"]) + " " + "minutes." + "\n")
                i = i + 1
            return '\n'.join(str(x) for x in n)

    else:
        while i < len(info["results"]):
            n.append("Route:" + " " + str(info['results'][i]['route']) + " " + "to" + " " + str(info['results'][i]['destination']) + "\n" + "Due:" + " " + str(info["results"][i]["duetime"]) + " " + "minutes." + "\n")

            i = i + 1 
    return '\n'.join(str(x) for x in n)

def chunks(info, n):
    results = info['results']
    for i in range(0, len(results), n):
        chunk = [
            'Route: {} to {}\nDue: {} minutes.\n'.format(
                result['route'], result['destination'], result["duetime"])
                    for result in results[i:i+n]]
        yield '\n'.join(chunk)

