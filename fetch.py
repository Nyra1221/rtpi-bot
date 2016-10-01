import urllib2, urllib, json

def fetchtime(stopnum):
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

    else:
        while i < len(info["results"]):
            n.append("Route:" + " " + str(info['results'][i]['route']) + " " + "to" + " " + str(info['results'][i]['destination']) + "\n" + "Due:" + " " + str(info["results"][i]["duetime"]) + " " + "minutes." + "\n")

            i = i + 1 
    return '\n'.join(str(x) for x in n)

