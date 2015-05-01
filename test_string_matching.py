import json
from time import time
from string_matching import *
import cPickle as pickle

'''
tt = time()
bands = json.load(open('../music-list/bands.json','r'))
band_names = bands.keys()
print 'loading bands took ' + str(time()-tt)

tt = time()
pickle.dump(band_names,open('defaultList.p','w'))
print 'dumping band names took ' + str(time()-tt)

tt = time()
band_hash = generateSearchableHashFromList(band_names)
print 'generating hash from bands took ' + str(time()-tt)

tt = time()
pickle.dump(band_hash,open('defaultHash.p','w'))
print 'dumping hash took ' + str(time()-tt)
'''

string = 'led zepplin'

print "trying with " + string

tt = time()
print searchThroughList(string)
print 'searching through list of ' + str(len(band_names)) + ' took ' + str(time()-tt)

tt = time()
try:
	if string in bands:
		print "found"
except:
	print "not found"
print 'trying dictionary took ' + str(time()-tt)

tt = time()
print searchThroughHash(string)
print 'searching through hash took ' + str(time()-tt)
