#!/usr/bin/python

import time
from twitter import *
from collections import defaultdict
import fileinput
from csv import writer

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)



#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

dicionario_candidato_users = defaultdict(list)	


days = ["2016-01-20"] 
#days = ["2016-01-11", "2016-01-12", "2016-01-13", "2016-01-14", "2016-01-15", "2016-01-16", "2016-01-17"] 
#days = ["2016-01-19"] 

for day in days:
	max_id = ""
	resultadosPorPagina = 100
	count = 1
	file_path = str.format('%s.csv' % day)
	out = open(file_path, 'a')
	out.write('tweet_created_at,tweet_id,tweet_user_id,tweet_text')
	out.close()




	numTweets = 0

	stop = False
	#while(True):
	while(count < 1000 and stop == False):					
		c1 = []
		c2 = []
		c3 = []
		c4 = []
		
		# https://dev.twitter.com/docs/api/1/get/search
		query = twitter.search.tweets(q = "presidenciais2016 OR presidenciais", lang='pt', until = day, max_id = max_id, count = resultadosPorPagina)
		out = open(file_path, 'a')



		
		print ("processing batch %s..." % (count)) 
		primeiro = True;
		
		if(len(query["statuses"]) == 1):
			stop = True
		
			
		for result in query["statuses"]:
			if(primeiro):
				primeiro = False
				continue
		
			numTweets = numTweets + 1	
			tweet_created_at = result["created_at"]
			tweet_id = result["id"]
			tweet_user_id = result["user"]["id"]
			tweet_text = result["text"].encode('utf-8', errors='replace')
			tweet_text = tweet_text.replace("\n"," ")
			c1.append(tweet_created_at)
			c2.append(tweet_id)
			c3.append(tweet_user_id)
			c4.append(tweet_text)
			
			max_id = result["id"]
		
			dicionario_candidato_users['marcelo'].append(result["user"]["id"])
			print(tweet_id)
		
		rows = zip(c1,c2,c3,c4)
		
		csv = writer(out)
		for row in rows:
			values = [value for value in row]
			csv.writerow(values)
			
		
		
		count = count + 1
		print "-------------------------------------------"

		out.close()

	print ("numero de tweets registados para %s: %s \n" % (day, numTweets)) 
			
def createFollowingFileForTag(tag):
	f = open('%s.txt' % tag, 'a')
	for user_id in dicionario_candidato_users[tag]:
		print "amigos do user_id %s" % (user_id)
		query_friends = twitter.friends.ids(user_id = user_id)
		for friend_id in query_friends["ids"]:
			print friend_id
			f.write("%s,%s\n" % (user_id, friend_id) )
		time.sleep(2)
		

for tag in dicionario_candidato_users:
	print "utilizadores a apoiar o candidato %s: \n" % dicionario_candidato_users[tag]
	#createFollowingFileForTag(tag)