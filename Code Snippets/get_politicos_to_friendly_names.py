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
				

list_of_ids_politico_atual = []

#@mmatias
#@snap2016PR
#@jorgesequeirapr
#@tinoderans2016


file_user_ids_politico = open("C:\\Users\\Jifu\\Dropbox\\MAPi\\Python\\python-twitter-workspace\\csvs_ids\\tweet_ids_tinoderans2016.txt")
file_input_csv = open("C:\\Users\\Jifu\\Dropbox\\MAPi\\Python\\python-twitter-workspace\\csvs_ids\\node_list.csv")
file_output_csv = open("C:\\Users\\Jifu\\Dropbox\\MAPi\\Python\\python-twitter-workspace\\csvs_ids\\node_list_processado.csv", 'a')

for line in file_user_ids_politico:
	list_of_ids_politico_atual.append(int(line.replace("\n","")))
file_user_ids_politico.close()


primeira_linha = True
for line in file_input_csv:
	if(primeira_linha):
		file_output_csv.write(line)
		primeira_linha = False
		continue

	line = line.replace("\n","")
	id_a_analisar = int(line.split(',')[0])
	print(id_a_analisar)
	if(id_a_analisar in list_of_ids_politico_atual):
		file_output_csv.write(str("%s,1" % (line)))
	else:
		file_output_csv.write(str("%s,0" % (line)))	

	file_output_csv.write("\n")
file_user_ids_politico.close()


