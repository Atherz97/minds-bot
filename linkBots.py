#
# python3 linkBots.py SUBSCRIBE? REMIND? TEST? CLEAN_MODE? Internal? External?
#
from minds import Minds, Profile
import sys
import json
import time
import random
import _thread

# ignore long wait times
IGNORE_TIME = 0 

# internal leads = within the bot family
leadInternal = 0

# external leads = from greater minds.com
# set to 2 for search terms
leadExternal = 2

# don't actually commit API calls
testmode = 0

# maximum accounts to act on per bot
maximum = 125

# like only
likeonly = 0

# search terms
terms = ['crypto',"bitcoin","freedom","gamedev","original","art","classic","photography","music","video","nature","food","vegan","magic","paranormal","technology","literature","news"]

# blacklisted posts
blacklist = ['1064457640073183232','1063155407067082752']

# load accounts
data = {}
with open('accounts.json','r') as f:
	data = json.load(f)
print("total accounts: " + str(len(data['people'])))
# only dirty bots data['people'] = data['people'][-380:]

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
		with open("skiplist.json","w") as f:
			json.dump(skiplist,f)
		time.sleep(60*30)
_thread.start_new_thread(updateSkipList,tuple())

# do not subscribe list
nosub_list = []
for p in data['people']:
	if p['name'] != "Affrontit":
		nosub_list.append(p['guid'])

# add custom do not subscribes
nosub_list.append('981635836376260618')  #artopium - for being a bitch fag
nosub_list.append('981603004186632193')  #mizantroop too much attention
nosub_list.append('1043171579380375570') #dailyghostvideos you're done

counter = 0
subscribe = 1
if len(sys.argv) > 1:
	subscribe = int(sys.argv[1])

remind = 0
if len(sys.argv) > 2:
	remind = int(sys.argv[2])

if len(sys.argv) > 3:
	testmode = int(sys.argv[3])

KEEP_CLEAN = 1
if len(sys.argv) > 4:
	KEEP_CLEAN = int(sys.argv[4])

if len(sys.argv) > 5:
	leadInternal = int(sys.argv[5])

if len(sys.argv) > 6:
	leadExternal = int(sys.argv[6])

print("subscribe: " + str(subscribe))
print("remind: " + str(remind))
print("testmode: " + str(testmode))
print("clean mode: " + str(KEEP_CLEAN))
print("internal leads: " + str(leadInternal))
print("external leads: " + str(leadExternal))

# eliminate dirty bots
if KEEP_CLEAN == 1:
	data['people'] = data['people'][:100]

# internal = add the GUIDs of the other robots
# this allows for cross-pollination of external feeds
global aguids
aguids = []
if leadInternal == 1:
	for p in data['people']:
		if (str(int(p['guid'])) == p['guid']):
			aguids.append(p['guid'])
		else:
			print(" missing channel info " + p['name'])


random.shuffle(data['people'])

global __GUIDS 
__GUIDS = []

''' def subrun '''
# for every robot, run this
def subrun(p):
	counter = 0

	print("> " + p['name'] + "...")
	
	while 1 == 1:
		try:
			minds_api = Minds(Profile(p['name'],p['password']))
			time.sleep(1)
		except:
			continue
		break

	# unsubscribe from other bots
	'''
	for _x_ in nosub_list:
		if testmode == 0:
			minds_api.unsubscribe(_x_)
		print(" U - " + str(_x_))
		time.sleep(random.randint(1,2))
	'''

	# load up potential profiles to browse
	guids = []
	if leadExternal != 0:
		guids = get_leads(minds_api,p['name'])
	if leadInternal != 0:
		for x in aguids:
			guids.append(x)
	guids = list(set(guids))
	random.shuffle(guids)
	
	# go through at least 5 profiles up to MAXIMUM
	for x in range(0,random.randint(5,maximum)):
		# let's pick a username and have it not be a teammate
		target = random.choice(guids)
		g = 20
		while leadExternal != 0 and g > 0 and target in nosub_list:
			target = random.choice(guids)
			g = g - 1
		if g == 0:
			print(" ? " + p['name'] + " could not escape bot")
		
		so = 0  # subscribe target's guid
		s = 0 	# 1 if will sub
		sn = "" # subscribe target's name

		# load up the newsfeed of that particular target
		pp = minds_api.newsfeed_channel(target,1,2)
		time.sleep(1)

		# scan their posts for things to remind, like, etc
		if pp['status'] != 'success' or pp.get('activity') == None:
			continue
		
		if len(pp['activity']) == 0:
			continue
		
		try:
			print(" :: " + p['name'] + " > " + pp['activity'][0]['ownerObj']['name'])
			so = pp['activity'][0]['ownerObj']['guid']
			for _xx in pp['activity']:
				if random.choice([0,0,1]) == 1:
					continue
				xx = _xx
				r = 0
				
				#if (xx.get('remind_object') != None) and (xx['remind_object'] != False):
				#	xx = xx['remind_object']
				
				if xx['ownerObj']['name'] == p['name']:
					continue

				# only from recent past...
				epoch = time.time()
				if xx.get('guid') == None:
					try:
						xx['guid'] = xx['entity_guid']
					except Exception as e:
						print(xx)
						break

				if xx['guid'] == False or int(xx['time_created']) > epoch or int(xx['time_created']) < epoch - (86400 * 10):
					if int(xx['time_created']) < epoch - (86400 * 30):	
						skiplist['list'].append(target)
					break
				
				# use sparingly for blacklisting individual posts
				if xx['guid'] in blacklist:
					break
						
				# try and cancel out NSFW
				sfw = 1
				if "sexy" in xx['message'] or "#girl" in xx['message']:
					sfw = 0
					print("NSFW")
					print(xx['message'])
					break
					
				# like
				if random.choice([1,1,1,1,0]) == 1:
					try:
						minds_api.upvote(xx['guid'])
						print(" L " + p['name'] + ' ' + xx['guid'])
						if IGNORE_TIME == 1:
							time.sleep(5)
						else:
							time.sleep(random.randint(20,60))
					except Exception as e:
						print(" ? failed " + str(e))
				r = 1
				s = 1
				sn = xx['ownerObj']['name']
						
				# share if desired
				if remind == 1 and r == 1 and random.choice([0,1]) == 1 and sfw == 1:
					if testmode == 0:
						try:
							minds_api.remind(xx['guid'])
							print(" | R " + p['name'] + ' ' + xx['guid'])
							if IGNORE_TIME == 1:
								time.sleep(5)
							else:
								time.sleep(random.randint(140,600))
							r = 0
						except Exception as e:
							_titty = 0
					break

			# after three posts attempt to subscribe
			if subscribe == 1 and s == 1 and random.choice([1,1,1,0]) == 1:
				try:
					print(" | S " + p['name'] + " " + str(sn))
					__GUIDS.append(so)

					if testmode == 0:
						minds_api.subscribe(so)
						if IGNORE_TIME == 1:
							time.sleep(5)
						else:
							time.sleep(random.randint(50,600))
					skiplist['list'].append(target)
				except Exception as e:
					print(" ? failed " + e)	
				break
		except Exception as e:
			print(" ? failed " + str(e))
	
	print(" ^ " + p['name'] + " done.")			
	return

''' def get leads '''
# get leads from this account's posts' like feed
# whoever liked any one of their last 10 posts gets counted
def get_leads(api,name):
	_guids = []
	g = api.get_channel(name)['channel']['guid']
	lead_posts = api.newsfeed_channel(g)
	while (1 == 1):
		try:
			subs = api.channel_subscriptions(0,128)['users']
			time.sleep(1)
		except:
			continue
		break

	print(" > " + name + " subs generated")
	try:
		if lead_posts['status'] == "success":
			for i in lead_posts['activity']:
				_i = i
				if _i['remind_object'] != False:
					_i = i['remind_object']
	
				c = 0
				if (c < 100 and _i['type'] == "activity"):
					counter = 0
					if _i['thumbs:up:user_guids'] != False:
						random.shuffle(_i['thumbs:up:user_guids'])
						for x in _i['thumbs:up:user_guids']:
							if x not in nosub_list and x not in skiplist['list']:
								_guids.append(x)
								counter = counter + 1
					if _i['thumbs:down:user_guids'] != False:
						for x in _i['thumbs:down:user_guids']:
							_guids.append(x)
							counter = counter + 1
					c = c + 1
	except Exception as e:
		pass

	# now go to the subscribers of the person
	for u in subs:
		if u['guid'] not in skiplist['list']:
			_guids.append(u['guid'])

	return _guids

# do this for every one of our robots
random.shuffle(data['people'])
ticker = 1
for p in data['people']:
	try:
		_thread.start_new_thread(subrun,(p,))
		if testmode == 1 or IGNORE_TIME == 1:
			time.sleep(5)
		else:
			if ticker == 4:
				time.sleep(random.randint(400,900))
				ticker = 1
			else:
				time.sleep(30)
				ticker = ticker + 1
	except Exception as e:
		print(e)
		continue

# every so and so tell @antwandhoward to subscribe to those
# that the bots subscribed to. welcome them.
''' _thread.start_new_thread(mass_subscribe) '''

# keep program alive until complete
while 1 == 1:
	time.sleep(1)
