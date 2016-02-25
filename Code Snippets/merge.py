from os import listdir
from os.path import isfile, join
mypath = "C:\\Users\\jifup\\Dropbox\\MAPi\\Python\\python-twitter-workspace\\registo tweets legislativas2016 final\\"
all_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

primeiro = True

fout=open("merged1.csv","a")

for file in all_files:
	if(".csv" in file and "2016" in file):
		print(file)
		f = open(file)
		if(not primeiro):
			f.next() # skip the header
		for line in f:
			 fout.write(line)
		f.close() # not really needed
		
		primeiro = False
fout.close()


