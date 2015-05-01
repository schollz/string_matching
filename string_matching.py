from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import Levenshtein
import operator
from multiprocessing import Pool
from collections import Counter
import cPickle as pickle

try:
	defaultList = pickle.load(open('defaultList.p','r'))
except:
	defaultList = []

try:
	defaultHash = pickle.load(open('defaultHash.p','r'))
except:
	defaultHash = {}



def compareStrings(strings):
	leven1 = fuzz.token_set_ratio(strings[0],strings[1])
	leven2 = Levenshtein.ratio(str(strings[0]),str(strings[1]))
	return (strings[0],strings[1],leven1+leven2*100,leven2)
	
def searchThroughList(searchString,listOfStrings=defaultList):
	if len(listOfStrings)==0:
		return "You need to save a hash to defaultHash.p if you want to load one automatically!"
	stringList = []
	for string in listOfStrings:
		stringList.append((searchString.lower(),string.lower()))
		
	pool2 = Pool(2) 
	results = pool2.map(compareStrings, stringList)
	pool2.close()
	pool2.join()
	#print (sorted(results, key=operator.itemgetter(2, 3), reverse=True))[:10]
	topResult = (sorted(results, key=operator.itemgetter(2, 3), reverse=True))[0]
	print (sorted(results, key=operator.itemgetter(2, 3), reverse=True))[:10]
	return listOfStrings[[x.lower() for x in listOfStrings].index(topResult[1])]

def generateSearchableHashFromList(listOfStrings):
	sHash = {}
	for string in listOfStrings:
		for i in range(0,len(string)-2):
			doublet = string[i:i+3].lower()
			if doublet not in sHash:
				sHash[doublet] = []
			sHash[doublet].append(string)
	return sHash
	

def searchThroughHash(searchString,sHash=defaultHash):
	if len(sHash)==0:
		return "You need to save a hash to defaultHash.p if you want to load one automatically!"
	searchString = searchString.lower()
	possibleStrings = []
	for i in range(0,len(searchString)-2):
		doublet = searchString[i:i+3]
		if doublet in sHash:
			possibleStrings += sHash[doublet]
	c = Counter(possibleStrings)
	mostPossible = []
	for p in c.most_common(1000):
		mostPossible.append(p[0])
	return searchThroughList(searchString,mostPossible)
	