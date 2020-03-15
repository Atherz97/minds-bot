from minds import Minds, Profile
import sys
import time, datetime

minds_api = Minds(Profile("dConnect312","dC12-4"))

posts = minds_api.newsfeed_search(sys.argv[1])
print()
print()
print()
print()
print()
print()
print()
print()

for post in posts['entities']:
	if post['type'] != 'activity':
		break
	print()
	print(post['ownerObj']['name'] + " (@" + post['ownerObj']['username'] + ") " + post['guid'])
	print()
	print(post['message'])
	print()
	print(str(post['thumbs:up:count']) + "^ " + str(post['comments:count']) + "c " + str(post['reminds']) + "% T:" + datetime.datetime.fromtimestamp(int(post['time_created'])).strftime('%c'))
	print()
	print("===============================")
	print()
