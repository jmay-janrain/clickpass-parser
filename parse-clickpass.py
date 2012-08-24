#!/usr/bin/python

import fileinput
import re
import json

SAVED_JSON_FILENAME = 'domain_ref_count'

# regex to find a referred domain
re_comp = re.compile('parent_url=http%3A%2F%2F([a-zA-Z0-9.]+)%2F')

domain_refs = {}

# Attempt to load the last count
try:
	file = open(SAVED_JSON_FILENAME, 'r')
	domain_refs = json.loads( file.read() )
	file.close()
except:
	domain_refs = {}

for line in fileinput.input():
	found = re_comp.findall(line)
	
	if len(found) > 0:
		domain = found[0]
		if domain in domain_refs.keys():
			domain_refs[domain] = domain_refs[domain] + 1
		else:
			domain_refs[domain] = 1
			
# Serialize the results to JSON
file = open(SAVED_JSON_FILENAME, 'w')
file.write( json.dumps( domain_refs ))

	


