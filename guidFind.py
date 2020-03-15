import json
import time
from minds import Minds, Profile

minds_api = Minds(Profile("dConnect312","dC12-4"))

profile_guid = '1048152926922481673'

result = minds_api.newsfeed_channel(profile_guid)

if result['status'] == "success":
	print(len(result["activity"]))
	for i in result["activity"]:
		print("0//////////////////////////////0")
		print(i['message'])
		print()
		print(i['entity_guid'])

