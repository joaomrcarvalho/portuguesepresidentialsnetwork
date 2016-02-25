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
mypath = "/home/jifu/Dropbox/MAPi/Python/python-twitter-workspace/csvs_ids/users/"

all_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

list_of_total_ids = []
file_user_ids = open("/home/jifu/Dropbox/MAPi/Python/python-twitter-workspace/csvs_ids/ids_totais.txt")
for line in file_user_ids:
	list_of_total_ids.append(int(line.replace("\n","")))
file_user_ids.close()


num_total_comparacoes = 0
num_total_ligacoes = 0


file_output_csv = open("/home/jifu/Dropbox/MAPi/Python/python-twitter-workspace/csvs_ids/file_output.csv", 'a')


file_number = 1
for file in all_files:
	print("%s out of %s\n" % (file_number, len(all_files)))
	file_number+=1

	if("txt" in file):
		print(file)
		f = open(join(mypath, file))
		for line in f:
			chars_to_ignore = ['.', '!', '?']
			user_to_test = int(line.split(",")[1].translate(None, ''.join(chars_to_ignore)))
			
			num_total_comparacoes += 1
			if(user_to_test in list_of_total_ids):
				#print("o user %s esta na lista!!!\n" % user_to_test)
				num_total_ligacoes += 1
				file_output_csv.write(line)
					
		
		f.close()
file_output_csv.close()

print("numero de ligacoes: %s \n" % num_total_ligacoes)


print("numero de comparacoes: %s \n" % num_total_comparacoes)





