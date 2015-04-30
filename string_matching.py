from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import Levenshtein
import operator
from multiprocessing import Pool
import cPickle as pickle
import time

''' Get rid of the big matrix
print 'getting tree'
(t,genreNames,bandNames,bandIds,X) = pickle.load(open('tree.p','r'))
print 'dumping band names'
pickle.dump((t,genreNames,bandNames,bandIds),open('bandNames.p','w'))
print 'done'
'''

print 'getting band names'
tt=time.time()
(t,genreNames,bandNames,bandIds) = pickle.load(open('bandNames2.p','r'))
print 'done'
print time.time()-tt

def compareStrings(strings):
	leven1 = fuzz.token_set_ratio(strings[0],strings[1])
	leven2 = Levenshtein.ratio(str(strings[0]),str(strings[1]))
	return (strings[0],strings[1],leven1,leven2)
	
def getRelated(searchString):
	stringList = []
	for bandName in bandNames:
		stringList.append((searchString,bandName))
		
	pool2 = Pool(2) 
	tt=time.time()
	results = pool2.map(compareStrings, stringList)
	pool2.close()
	pool2.join()
	#print (sorted(results, key=operator.itemgetter(2, 3), reverse=True))[:10]
	topResult = (sorted(results, key=operator.itemgetter(2, 3), reverse=True))[0]
	bandIndex = bandNames.index(topResult[1])
	bandActualIndex = bandIds[bandIndex]

	subtree = t
	for leaf in t.traverse("postorder"):
		try:
			if str(leaf.name) == str(bandActualIndex)+'.':
				for tree in leaf.iter_ancestors():
					subtree = tree
					if len(subtree.get_leaf_names())>5:
						break
		except:
			pass
	textTree = subtree.get_ascii(show_internal=False)
	relatedBands = []
	for leaf in subtree.traverse("postorder"):
		try:
			pseudoIndex = bandIds.index(int(leaf.name[:-1]))
			if str(leaf.name) == str(bandActualIndex)+'.':
				replacement = "<span style='color:red;'><b>%(name)s</b></span>"
			else:
				replacement = "%(name)s"
			
			textTree = textTree.replace(leaf.name,replacement % {'name':bandNames[pseudoIndex]})
			relatedBands.append(bandNames[pseudoIndex])
		except:
			pass
	return (textTree,relatedBands)
