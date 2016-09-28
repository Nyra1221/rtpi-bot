import urllib2, urllib, json, fetch
try:
	stopnum = int(input("Stop Number: "))
except: 
	stopnum = 1
print "\n"
print fetch.fetchtime(stopnum)



	