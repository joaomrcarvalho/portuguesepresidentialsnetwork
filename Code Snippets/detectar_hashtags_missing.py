import csv
import nltk
import time
import operator
import string
import collections

from collections import defaultdict
from operator import itemgetter, attrgetter, methodcaller
from nltk import sent_tokenize, word_tokenize, pos_tag, ngrams, FreqDist
from nltk.tokenize import RegexpTokenizer


path_f_open = 'merged1.csv'
f = open(path_f_open)
csv_f = csv.reader(f)

tweet_created_at_index = 0
tweet_id_index = 1
tweet_user_id_index = 2
tweet_text_index = 3

huge_tweets_text = ""

for row in csv_f:
  huge_tweets_text+=str.format("%s\n" % row[tweet_text_index])
  
hashtags_total = []
hashtags_anteriores = []

for tag in huge_tweets_text.split():
	if tag.startswith("#"):
		if(tag not in hashtags_total):
			hashtags_total.append(tag)
		
print("Numero de hashtags actuais: %s \n" % len(hashtags_total))

f.close()
f = open(path_f_open)
csv_f = csv.reader(f)

path_f_open_2 = "candidatos_hashs.csv"
f2 = open(path_f_open_2)
csv_f2 = csv.reader(f2)

reader = csv.DictReader(f2) # read rows into a dictionary format
for row in reader: # read a row as {column1: value1, column2: value2,...}
	for i in range(0,12):
		#print("appending %s to %s " % (row[str(i)], str(i)))
		if(row[str(i)] != "" and "#" in row[str(i)]):
			hashtags_anteriores.append((row[str(i)]))
			
print("Numero de hashtags anteriores: %s \n" % len(hashtags_anteriores))

interseccao = set(hashtags_total).intersection(hashtags_anteriores)

hashtags_a_classificar = []

for hash in hashtags_total:
	if hash not in interseccao:
		hashtags_a_classificar.append(hash)
		print hash

		
print("Numero de hashtags a classificar: %s \n" % len(hashtags_a_classificar))
		


			
