import urllib2, urllib, json, app, ssl

def fetchtime(stopnum):
    try:
        val = int(stopnum)
    except ValueError:
        return "Stop numbers must be numeric!" 

    if stopnum == "654321":
        return "https://www.youtube.com/watch?v=tsfnuyyjaB0" # Why am I like this

    if len(stopnum) > 6:
        return "This is not a valid stop number!"# Here we're ensuring that the bot only processes requests that are ints and 0-6 chars in length
        # This is to stop crashes from massive messages. I sent this thing the Bee Movie script before I put this in place. It didn't end well.


    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE # An evil workaround thanks to Dublin Bus fishing their certs. Please never do this if you can help it
    
    n = []
    data = "?stopid={}".format(stopnum)+"&format=json" #Taking stop number and subbing it into the request URL
    content = "https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation"
    req = urllib2.urlopen(content + data + "?", context = ctx)
    i = 0 
    info = json.load(req)


    if len(info["results"]) == 0:
        return "Sorry, there's no real time info for this stop!" #If there are no results

    if len(info["results"]) > 5:
            while i < 5:
                n.append("Route: {} to {} \nDue: {} minutes\n".format(info["results"][i]["route"], info["results"][i]["destination"], info["results"][i]["duetime"]))
                i = i + 1
            return '\n'.join(str(x) for x in n) #Only displays 5 buses for busy stops to avoid tripping the 320 char limit.

    else:
        while i < len(info["results"]):
            n.append("Route: {} to {} \nDue: {} minutes\n".format(info["results"][i]["route"], info["results"][i]["destination"], info["results"][i]["duetime"]))
            i = i + 1 
    return '\n'.join(str(x) for x in n) #For everything else.

def chunks(info, n):
    results = info['results']
    for i in range(0, len(results), n):
        chunk = [
            'Route: {} to {}\nDue: {} minutes.\n'.format(
                result['route'], result['destination'], result["duetime"])
                    for result in results[i:i+n]]
        yield '\n'.join(chunk) # A work in progress function to send complete bus listings as separate messages thereby bypassing the 320 char limit.

