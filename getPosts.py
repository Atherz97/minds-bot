from minds import Minds, Profile
import sys

minds_api = Minds(Profile("dConnect312","dC12-4"))

print(minds_api.get_channel("SOME_PROFILE"))

posts = minds_api.newsfeed_featured()
lead_list = []
if posts['status'] == "success":
	for i in posts["activity"]:
		c = 0
		if (c < 20 and i['type'] == "activity"):
			counter = 0
			for x in i['thumbs:up:user_guids']:
				if (counter < 15):
					lead_list.append(x)
					counter = counter + 1
			c = c + 1
print(lead_list)
