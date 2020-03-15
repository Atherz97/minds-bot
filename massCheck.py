#
# python3 massCheck.py testmode
# scroll down to line 64 to add your profile info - this subscribes to accounts using network effect
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

# load skip list
skiplist = {
	"list":[],
}
with open('skiplist.json','r') as f:
	skiplist = json.load(f)
print("skiplist loaded")

# update skip list
def updateSkipList():
	while 1 == 1:
		with open("skiplist.json","r") as f:
			skiplist = json.load(f)
			#json.dump(skiplist,f)
		time.sleep(60*30)
_thread.start_new_thread(updateSkipList,tuple())

# for some reason our stack counter is buggy,
# so this will force reset it when enough threads complain
fullStack = 0
def resetStack():
	global fullStack, __STACK
	while 1 == 1:
		if fullStack > 10:
			__STACK = 0
			fullStack = 0
		time.sleep(25)
_thread.start_new_thread(resetStack,tuple())

counter = 0

if len(sys.argv) > 1:
	testmode = int(sys.argv[1])

print("testmode: " + str(testmode))

__GUIDS = []
__STACK = 0

# log in
while 1 == 1:
	try:
		minds_api = Minds(Profile("YOUR_USER","YOUR_PASS"))
	except:
		continue
	break

self_guid = "1048152926922481673"
subscriptions = minds_api.channel_subscriptions(0,1000)['users']
alreadySubscribed = []
for user in subscriptions:
	alreadySubscribed.append(user['guid'])

#
#	get new people from the subscriptions
#	of GUID
#
def get_leads(guid,level):
	if level == 5:
		return

	global __STACK, fullStack

	attempt = 0
	while 1 == 1:
		try:
			if __STACK < 8:
				print(" :: " + str(level) + " > loading subs " + str(guid))
				__STACK = __STACK + 1
				subs = minds_api.channel_subscriptions_of(guid,0,200)
				__STACK = __STACK - 1
				break
			else:
				fullStack = fullStack + 1
			time.sleep(15)
		except:
			__STACK = __STACK - 1
			if level > 2 or attempt == 2:
				print(" :: ? load subs fail guid " + guid)
				return
			attempt = attempt + 1
			continue

	random.shuffle(subs['users'])
	for u in subs['users']:
		aguid = u['guid']
		if aguid in skiplist['list']:
			continue
		if aguid in alreadySubscribed:
			# MAYBE go to their followers, but we have to get through others
			if random.choice([0,0,0,1]) == 1:
				_thread.start_new_thread(get_leads,(aguid,level + 1,))
				time.sleep(1)
			continue
		try:
			#lastPostTime = minds_api.newsfeed_channel(aguid,0,1)['activity'][0]['time_created']
			while 1 == 1:
				try:
					if __STACK < 8:
						__STACK = __STACK + 1
						lastPostTime = minds_api.newsfeed_channel(aguid,0,1)['activity'][0]['time_created']
						__STACK = __STACK - 1
						break
					else:
						fullStack = fullStack + 1
					time.sleep(2)
				except:
					__STACK = __STACK - 1
					continue
			if (int(lastPostTime) < time.time() - 86400 * 2):
				skiplist['list'].append(aguid)
				continue
			__GUIDS.append(aguid)
			print(" > " + aguid + " added too.")
			_thread.start_new_thread(get_leads,(aguid,level + 1,))
		except Exception as e:
			pass

#
#	mass subscribe function, automating the subscription
#	process after leads are found
#
def mass_subscribe():
	while 1 == 1:
		time.sleep(1)
		guids = __GUIDS
		if len(guids) == 0:
			continue
		print()
		print("subscribing...")

		for target in guids:
			_thread.start_new_thread(act_on,(target,))
			time.sleep(30)

	print("add another username:")
	mass_subscribe()

_thread.start_new_thread(mass_subscribe,tuple())

#
#	give three likes and a follow
#	so that they notice us
#
def act_on(target):
	__GUIDS.remove(target)
	
	# check if we're already subbed to them
	if target in alreadySubscribed:
		print("user " + str(target) + " already subscribed.")
		return
	
	try:	

		# load up the newsfeed of that particular target
		pp = minds_api.newsfeed_channel(target,1,3)
		time.sleep(1)
		
		# scan their posts for things to remind, like, etc
		if pp['status'] != 'success' or pp.get('activity') == None:
			return
	
		if len(pp['activity']) == 0:
			return

		print(" :: " + pp['activity'][0]['ownerObj']['name'])
		so = pp['activity'][0]['ownerObj']['guid']
	
		for _xx in pp['activity']:
			if random.choice([0,0,0,0,0,1]) == 1:
				continue
			xx = _xx
			r = 0
		
			if xx['guid'] == False:
				continue
		
			#
			# like
			#
			try:
				if testmode == 0:
					minds_api.upvote(xx['guid'])
					time.sleep(15)
				print(" L " + xx['guid'])
			except Exception as e:
				print(" ? failed " + str(e))
			s = 1
			sn = xx['ownerObj']['name']
					
		# after three posts attempt to subscribe
		if s == 1:
			try:
				if testmode == 0:
					minds_api.subscribe(so)
					alreadySubscribed.append(so)
					time.sleep(20)
				print(" | S " + str(sn))
			except Exception as e:
				print(" ? failed " + e)	
	except Exception as e:
		print(" ? failed " + str(e))

#
# accept input from USER on new accounts to track
#
ok = 1
while 1 == 1:
	time.sleep(1)
	if ok == 0:
		username = ""
		ok = 1
	else:
		username = input("add username to lead queue: ")

	try:
		guid = minds_api.get_channel(username)['channel']['guid']
		__GUIDS.append(guid)
		print(" > user " + str(guid) + " added.")
		_thread.start_new_thread(get_leads,(guid,0,))
	except:
		print(" ? failed")
