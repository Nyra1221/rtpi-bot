import urllib2, urllib, json

def fetchtime(stopnum):
    data = "?stopid={}".format(stopnum)+"&format=json"
    content = "https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation"
    req = urllib2.urlopen(content + data + "?")

    i = 0 
    info = json.load(req)

    if len(info["results"]) == 0:
        return "Sorry, there's no real time info for this stop!"

    while i < len(info["results"]):
        return "Route Number:" + " " + info['results'][i]['route']
        return "Due in" + " " + info["results"][i]["duetime"] + " " + "minutes." + "\n"
        i = i + 1 