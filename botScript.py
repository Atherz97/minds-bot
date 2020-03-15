#
#  usage: python3 botScript.py [minds_username] [max bots] [sub?] [remind?] [n'th post or 0 for 10] [clean mode?]
#

from minds import Minds, Profile
import sys
import json
import time
import random
import _thread

minds_api = Minds(Profile("dConnect312","dC12-4"))

# channel guid
guid = minds_api.get_channel(sys.argv[1])['channel']['guid']

# last 10 post guid
posts = minds_api.newsfeed_channel(guid,0,15)

# set to one to disable time constraint
IGNORE_TIME = 0

# clean = bots with fresh looking accounts
# dirty = empty account bots, no bio etc
KEEP_CLEAN = 1

# GROUP BOMBS SOON
GROUP_BOMB = 0
GROUP = []
GROUP_GUIDS = []
for i in GROUP:
	GROUP_GUIDS.append(minds_api.get_channel(i)['channel']['guid'])

# load up targetted posts
# checking to make sure that they haven't been posted yet
# and that they're from at least the last 2 weeks
epoch = time.time()
target_post = '1063134431039619072'
target_post_2 = '1062894600250359808'
target_10 = []
if posts['status'] == "success":
	target_post = str(posts['activity'][0]['guid'])
	if (len(posts['activity']) > 1):
		target_post_2 = str(posts['activity'][1]['guid'])
	for i in posts["activity"]:
		if IGNORE_TIME == 1 and i['guid'] != False:
			target_10.append(str(i['guid']))
		else:
			if i['guid'] != False and int(i['time_created']) < epoch and int(i['time_created']) > epoch - (86400 * 14):
				target_10.append(str(i['guid']))
	if len(target_10) == 0:
		print("posts returned are OLD")
		print(posts['activity'])
	target_post = target_10[0]
	target_post_2 = target_10[1]

subscribe_to = guid

# load accounts
data = {}
with open('accounts.json','r') as f:
	data = json.load(f)
print("total accounts: " + str(len(data['people'])))
# end load

# modes
maximum = len(data['people'])
if len(sys.argv) > 2:
	maximum = int(sys.argv[2])
print("maximum accounts: " + str(maximum))

tenmode = 1

subscribe = 0
if len(sys.argv) > 3:
	subscribe = int(sys.argv[3])
print("subscribe posts: " + str(subscribe))

remind = 0
if len(sys.argv) > 4:
	remind = int(sys.argv[4])
print("remind mode: " + str(remind))

opm = 0
if len(sys.argv) > 5:
	opm = int(sys.argv[5])
	if opm > 0:
		tenmode = 0
		print("ten posts: 0")
print("one post mode: " + str(opm))

KEEP_CLEAN = 1
if len(sys.argv) > 6:
	KEEP_CLEAN = int(sys.argv[6])
print("clean mode: " + str(KEEP_CLEAN))
if KEEP_CLEAN == 1:
	data['people'] = data['people'][:120]
else:
	if KEEP_CLEAN == 2:
		data['people'] = data['people'][-300:]
	IGNORE_TIME = 1

# end modes

random.shuffle(data['people'])

counter = 0
def activate(p):

	n = p['name']
	print(" > " + n)

	minds_api = Minds(Profile(p['name'],p['password']))

	# vote up the selected post guid
	if (tenmode):
		for x in range(0,9):
			if (x < len(target_10)):
				t = target_10[x]
			else:
				continue
			
			try:
				print(" L " + n + " " + t)
				minds_api.upvote(t)
				time.sleep(random.randint(15,30))
			except Exception as e:
				print(" ? failed")
			
			# if reblogged, stop scrolling
			r = 1
			if remind == 1 and random.choice([0,1,1]) == 1 and x < 6:
				try:
					print(" R " + n + " " + t)
					minds_api.remind(t)
					r = 0
					time.sleep(random.randint(12,80))
				except Exception as e:
					print(" ? failed")
			
			# stop scrolling after a certain point
			if random.choice([r,r,r,0]) == 0:
				break
	else:
		try:
			time.sleep(random.randint(1,40))
			if random.choice([1,1,1,1,1,1,1,1]) == 1:
				print(" L " + n + " " + target_10[opm - 1])
				minds_api.upvote(target_10[opm -1])
				time.sleep(random.randint(15,45))
		except Exception as e:
			print(" ? failed")
		
		if remind == 1 and random.choice([0,0,0,1]) == 1:
			try:	
				print(" R " + n + " " + target_10[opm-1])
				minds_api.remind(target_10[opm-1])
				time.sleep(random.randint(12,120))
			except Exception as e:
				print(" ? failed")

	# potentially hit the second post and a random post
	if (random.choice([0,0,0,1]) == 1) and opm == 0 and len(target_post_2) > 2:
		if (tenmode):
			try:
				oo = random.choice(target_10)
				print(" L " + n + " " + oo)
				minds_api.upvote(oo)
			except Exception as e:
				print(" ? failed")
		else:
			try:
				print(" L " + n + " " + target_post_2)
				minds_api.upvote(target_post_2)
			except Exception as e:
				print(" ? failed")
		time.sleep(random.randint(15,50))
        
	# subscribe after all's said and done
	if random.choice([0,1,1]) == 1 and subscribe == 1:
		try:
			print(" S " + n + " " + subscribe_to)
			minds_api.subscribe(subscribe_to)
			time.sleep(random.randint(10,30))
		except Exception as e:
			print(" ? failed")

	print(" ^ " + n)

for p in data['people']:
	if counter > maximum:
		break
	try:
		counter = counter + 1
		_thread.start_new_thread(activate,(p,))
	except Exception as e:
		print(e)
		continue

	if IGNORE_TIME == 1:
		time.sleep(2)
	else:
		time.sleep(random.randint(60,200))

while 1 == 1:
	time.sleep(1)
