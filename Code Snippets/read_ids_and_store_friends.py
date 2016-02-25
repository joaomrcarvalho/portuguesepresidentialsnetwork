from os import listdir
from os.path import isfile, join
from twitter import *
from collections import defaultdict
import time
import traceback

config = {}
execfile("config.py", config)

twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
				
mypath = "C:\\Users\\jifup\\Dropbox\\MAPi\\Python\\python-twitter-workspace\\csvs_ids\\"

all_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

list_of_total_ids = []


for file in all_files:
	if("tweet_ids_" in file):
		print(file)
		f = open(file)
		for line in f:
			 list_of_total_ids.append(line.replace("\n",""))
		f.close()

print("!----------------------!")
#print list_of_total_ids
#print len(list_of_total_ids)

#time.sleep(1500)
f2 = open("saidas_teste.txt",'a')
contador = 1
time_to_wait = 6

for user_id in list_of_total_ids:
	file_atual = open(str.format("%susers\\%s.txt" % (mypath, user_id)),'a')
	print("analisando amigos do user_id %s (%s/%s) \n" % (user_id, contador, len(list_of_total_ids)))
	try:
		query_friends = twitter.friends.ids(user_id = user_id)	
	except Exception as e:
		print(e)
		print("time to wait: %s" % time_to_wait)
		time.sleep(time_to_wait+10)
		contador+=1
		file_atual.close()
		continue
	print("friends: %s" % len(query_friends["ids"]))
	for friend_id in query_friends["ids"]:
		file_atual.write("%s,%s\n" % (user_id, friend_id) )

	#time_to_wait =( ((6*len(query_friends["ids"]))/100)+6	)*2
	
	print("time to wait: %s" % time_to_wait)
	time.sleep(time_to_wait)
	contador+=1
	file_atual.close()
f2.close()