import csv
import nltk
import time
import operator
import string
import collections

from twitter import *

config = {}
execfile("config.py", config)
twitter = Twitter(
		auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

from collections import defaultdict
from operator import itemgetter, attrgetter, methodcaller
from nltk import sent_tokenize, word_tokenize, pos_tag, ngrams, FreqDist
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
#print (tokenizer.tokenize('Eighty-seven miles to go, yet.  Onward!'))


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
  

print("comprimento = %s \n" % len(huge_tweets_text))

print("Hashtags: ")
hashtags_contagem = {}
for tag in huge_tweets_text.split():
	if tag.startswith("#"):
		if(tag not in hashtags_contagem):
			hashtags_contagem[tag] = 0
		hashtags_contagem[tag] += 1

print("numero de hashtags = %s" % len(hashtags_contagem))

#colunas "candidatos_hashs.csv"
c_paulo_morais = 0
c_edgar_silva = 1
c_henrique_neto = 2
c_marisa_matias = 3
c_maria_belem = 4
c_sampaio_novoa = 5
c_jorge_sequeira = 6
c_vitorino_silva = 7
c_candido_ferreira = 8
c_marcelo = 9
c_ignorar = 10

f.close()
f = open(path_f_open)
csv_f = csv.reader(f)

path_f_open_2 = "candidatos_hashs.csv"
f2 = open(path_f_open_2)
csv_f2 = csv.reader(f2)

candidato_hashtags = defaultdict(list) # each value in each column is appended to a list

reader = csv.DictReader(f2) # read rows into a dictionary format
for row in reader: # read a row as {column1: value1, column2: value2,...}
	for i in range(0,10):
		#print("appending %s to %s " % (row[str(i)], str(i)))
		if(row[str(i)] != ""):
			candidato_hashtags[i].append(row[str(i)]) # append the value into the appropriate list

estrutura_users_por_candidato = defaultdict(list)
lista_de_users_total = []
for row in csv_f:
	for tag in row[tweet_text_index].split():
		if tag.startswith("#"):
			#inicializacao para caso nao encontre a hash no csv
			num_coluna = c_ignorar
			
			#procurar no csv qual a coluna em que esta a hash (ate 9)
			for i in range(0,10):
				#se encontrou numa coluna valida
				if(tag in candidato_hashtags[i] and row[tweet_user_id_index] not in lista_de_users_total):
					#modificar
					num_coluna = i
				
					#adiciona o utilizador que fez o tweet a lista de apoiantes do candidato
					estrutura_users_por_candidato[num_coluna].append(row[tweet_user_id_index])
					lista_de_users_total.append(row[tweet_user_id_index])
					break
			
total = 0

for i in range(0,10):
	total += len(estrutura_users_por_candidato[i])
	#print("users do candidato %s : %s \n\n\n---------------------------------\n" % (i, len(estrutura_users_por_candidato[i])))
candidato = ""

print("Numero total de apoiantes: %s" % total)

for i in range(0,10):
	if(i == 0): 
		candidato = "Paulo Morais"
	if(i == 1):
		candidato = "Edgar Silva"
	if(i == 2):
		candidato = "Henrique Neto"
	if(i == 3):
		candidato = "Marisa Matias"
	if(i == 4):
		candidato = "Maria de Belem"
	if(i == 5):
		candidato = "Sampaio da Novoa"
	if(i == 6):
		candidato = "Jorge Sequeira"
	if(i == 7):
		candidato = "Vitorino Silva"
	if(i == 8):
		candidato = "Candido Ferreira"
	if(i == 9):
		candidato = "Marcelo Rebelo de Sousa"
	previsao = (len(estrutura_users_por_candidato[i]))*100 / total
	print("previsoes para %s:\n Apoiantes no twitter: %s\n Percentagem: %s \n Hashtags usadas:%s\n---------------------------------" % (candidato,len(estrutura_users_por_candidato[i]), previsao,candidato_hashtags[i]))

#print(estrutura_users_por_candidato)

#tino
print(estrutura_users_por_candidato[9])
	
f.close()
f2.close()

for i in range(0,10):
	contador = 0

#analisar quem segue quem do candidato i:
	for username in estrutura_users_por_candidato[i]:
		contador+=1

		print("analisando amigos do username %s (%s de %s)\n" % (username,contador,len(estrutura_users_por_candidato[i])))
		

		try:
			query = twitter.friends.ids(user_id = username)
		except Exception as e:
				print("Exception 1...")
				continue
		
		time.sleep(6)
		print "found %d friends" % (len(query["ids"]))
		
		for n in range(0, len(query["ids"]), 100):
			ids = query["ids"][n:n+100]


			try:
				subquery = twitter.users.lookup(user_id = ids)
			except Exception as e:
				print("Exception 2...")
				continue
			time.sleep(6)
			for user in subquery:
				if(user["id"] in lista_de_users_total):
					print " [%s] %s" % ("*" if user["verified"] else " ", user["screen_name"])
				
		