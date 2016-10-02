import urllib2, urllib, json, fetch
try:
	stopnum = raw_input("Stop Number: ")
except: 
	stopnum = 1
print "\n"
print fetch.fetchtime(stopnum)



	