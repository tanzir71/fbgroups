#-*- coding: utf-8 -*-
import requests
import json
import time
from facepy import GraphAPI


#Author: T Shrinivasan <tshrinivasan@gmail.com>

# get api from here  https://developers.facebook.com/tools/explorer

api = "FILL YOUR API Access Token FROM THE ABOVE URL"

graph = GraphAPI(api)


message = '''


Add all your contents to be posted to facebook groups here




'''


# Find the ids of your desired groups from http://lookup-id.com/  
# and add this in this array groups

groups = ['groupid1']



for group_id in groups:
	print "Posting to " + 'http://www.facebook.com/groups/' + str(group_id)
	graph.post(path =str(group_id) + '/feed', message=message)
	time.sleep(10)
print "Done"
