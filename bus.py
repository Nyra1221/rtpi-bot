#This is a simple script for testing changes to fetch.py independent of Facebook Messenger.

import urllib2, urllib, json, fetch
try:
	stopnum = raw_input("Stop Number: ")
except: 
	stopnum = 1
print "\n"
print fetch.fetchtime(stopnum)



	