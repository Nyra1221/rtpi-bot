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
        split_into_pairs_of_5(info) 

    else:
        while i < len(info["results"]):
            n.append("Route:" + " " + str(info['results'][i]['route']) + " " + "to" + " " + str(info['results'][i]['destination']) + "\n" + "Due:" + " " + str(info["results"][i]["duetime"]) + " " + "minutes." + "\n")

            i = i + 1 
    return '\n'.join(str(x) for x in n)


def split_into_pairs_of_5(info)
    outer = []
    inner = []
    for x in range(len(info["results"])):
        if x % 5 == 0 and inner:
            outer.append(inner)
            inner = []

        inner.append("Route:" + " " + str(info['results'][i]['route']) + " " + "to" + " " + str(info['results'][i]['destination']) + "\n" + "Due:" + " " + str(info["results"][i]["duetime"]) + " " + "minutes." + "\n")

    if inner:
        outer.append(inner)
        inner = []

    return outer


result = split_into_pairs_of_5(info)

for i in info:
    send_message('\n'.join(str(x) for x in i))