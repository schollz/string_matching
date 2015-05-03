import json
from time import time
from string_matching import *
import pickle
import sys

string = sys.argv[1]

print "trying with " + string

print "checking if it is exactly in list..."
tt = time()
try:
	if string in bands:
		print "found exactly"
except:
	print "not found exactly"
print 'trying list look-up took ' + str(time()-tt)
print "\n"

print "searching through entire list..."
tt = time()
result = searchThroughList(string)
print "Best match: " + result
print 'searching through entire list took ' + str(time()-tt)
print "\n"


print "searching through hashed list..."
tt = time()
result = searchThroughHash(string)
print "Best match: " + result
print 'searching through hashed list took ' + str(time()-tt)

