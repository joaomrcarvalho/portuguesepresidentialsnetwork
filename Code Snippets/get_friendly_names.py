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
				
#mypath = "C:\\Users\\jifup\\Dropbox\\MAPi\\Python\\python-twitter-workspace\\csvs_ids\\users\\"
#mypath = "/home/jifu/Dropbox/MAPi/Python/python-twitter-workspace/csvs_ids/"

list_of_total_ids = []

file_user_ids = open("C:\\Users\\jifup\\Dropbox\\MAPi\\Python\\python-twitter-workspace\\csvs_ids\\ids_totais.txt")
#file_user_ids = open("/home/jifu/Dropbox/MAPi/Python/python-twitter-workspace/csvs_ids/ids_totais.txt")
for line in file_user_ids:
	list_of_total_ids.append(int(line.replace("\n","")))
file_user_ids.close()

print list_of_total_ids

file_output_csv = open("C:\\Users\\jifup\\Dropbox\\MAPi\\Python\\python-twitter-workspace\\csvs_ids\\node_list.csv", 'a')
#file_output_csv = open("/home/jifu/Dropbox/MAPi/Python/python-twitter-workspace/csvs_ids/node_list.csv", 'r+')

file_output_csv.write("user_id,label\n")

username = ""

cont = 0
for user_id in list_of_total_ids:
	cont+=1
	print("%s out of %s" % (cont, len(list_of_total_ids)))	
	file_output_csv.write(str("%s," % user_id))
	try:
		user = twitter.users.lookup(user_id = user_id)
		username = user[0]["screen_name"]
	except Exception as e:
		print(e)
		username = "-"
	file_output_csv.write(str("%s\n" % username))
	print("%s -> %s \n" % (user_id, username))
	time.sleep(10)
file_output_csv.close()
