#!/usr/bin/python

import time
from twitter import *
from collections import defaultdict

config = {}
execfile("config.py", config)

twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

dicionario_candidato_users = defaultdict(list)	
				
max_id = ""
count = 0

#@snap2016PR
#@mmatias_
#@tinoderans2016
#@jorgesequeirapr

pol = "mmatias_"


query = twitter.followers.ids(screen_name = str.format("@%s" % pol), lang='pt')
query2 = twitter.followers.ids(screen_name = str.format("@%s" % pol), lang='pt', cursor = query['next_cursor'])

f = open('tweet_ids_%s.txt' % pol, 'a')


for result in query['ids']:
#for result in query2['ids']:
	print result
	f.write(str.format("%s\n" % result))
	
	count+= 1
	#time.sleep(1)

for result in query2['ids']:
	print result
	f.write(str.format("%s\n" % result))
	
	count+= 1
	#time.sleep(1)

f.close()
print count


