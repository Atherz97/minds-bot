from minds import Minds, Profile
import sys

minds_api = Minds(Profile("dConnect312","dC12-4"))

# channel guid
guid = minds_api.get_channel(sys.argv[1])['channel']['guid']
print(guid)

# last 10 post guid
posts = minds_api.newsfeed_channel(guid,0,12)

if posts['status'] == "success":
	for i in posts["activity"]:
		print(" > " + str(i['guid']) + " " + str(i['message']) + " " + str(i['tags']))

