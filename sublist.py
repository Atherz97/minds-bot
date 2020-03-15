#
# python3 massCheck.py testmode
#
from minds import Minds, Profile
import sys
import json
import time
import random
import _thread

# ignore long wait times
IGNORE_TIME = 0 

# if 1, we don't actually commit API calls
testmode = 0

# add custom do not subscribes
nosub_list = []
nosub_list.append('981635836376260618')  #artopium - for being a bitch fag
nosub_list.append('981603004186632193')  #mizantroop too much attention

counter = 0

if len(sys.argv) > 1:
	testmode = int(sys.argv[1])

print("testmode: " + str(testmode))

__GUIDS = []

# log in
while 1 == 1:
	try:
		minds_api = Minds(Profile("antwandhoward","@@Ua9h5t9t"))
	except:
		continue
	break

self_guid = "1048152926922481673"
subscriptions = minds_api.channel_subscriptions(0,1000)['users']
alreadySubscribed = []
for user in subscriptions:
	print(user['guid'])
