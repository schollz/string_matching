import pickle
from time import time 
from string_matching import *

WORDLIST_FILE = 'wordlist'

try:
	defaultList = pickle.load(open('defaultList.p','r'))
except:
	# Make a list of words, save it as "defaultList.p"
	tt = time()
	defaultList = []
	with open(WORDLIST_FILE,'r') as f:
		for line in f:
			defaultList.append(line.strip().title())
	pickle.dump(defaultList,open('defaultList.p','w'))
	print 'dumping defaultList took ' + str(time()-tt)


try:
	defaultHash = pickle.load(open('defaultHash.p','r'))
except:
	# Generate the searchable hash, save it as "defaultHash.p"
	tt = time()
	defaultHash = generateSearchableHashFromList(defaultList)
	pickle.dump(defaultHash,open('defaultHash.p','w'))
	print 'dumping defaultHash took ' + str(time()-tt)