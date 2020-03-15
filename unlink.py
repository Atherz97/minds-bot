# python3 linkBots.py SUBSCRIBE? REMIND?
from minds import Minds, Profile
import sys
import json
import time
import random
import _thread

blacklist = ['1063155407067082752']
nosub_list = [

testmode = 0
subscribe_to = '1048152926922481673'
maximum = 100

data = {}
data['people'] = []
data['people'].append({
	'name': 'Affrontit',
	'password': '~g.Q%tv:%N.6x4.9',
})
data['people'].append({
	'name': 'breadroll64',
	'password': 'ZEf^{T8;dnh%:6:>',
})
data['people'].append({
	'name': 'PetrisPotassium',
	'password': 'T)EV]V6(;UNRS)h*',
})
data['people'].append({
	'name': 'Friendhuggrr',
	'password': "CC>M6_}P<9eTv-'X",
})
data['people'].append({
	'name': 'Mindset5',
	'password': '=F4}tz4nm!g@gvT',
})
data['people'].append({
	'name': 'Spiritugenics',
	'password': "$$CF+HNA9t'z$@xD",
})
data['people'].append({
	'name': 'MoneyMetrics',
	'password': '$#P9p)NUs9VR6-*d',
})
data['people'].append({
	'name': 'Minvio',
	'password': "8*'c-E(ChMh]\\!q+",
})
data['people'].append({
	'name': 'Jungskin23',
	'password': 'n>dXa5zxHzXR]eh>',
})
data['people'].append({
	'name': 'Styxia',
	'password': 'h,-R836A6*DyK&]u',
})
data['people'].append({
	'name': 'Chirpin23',
	'password': 'u78Cpk)JNWgyyzwD',
})
data['people'].append({
	'name': 'owrighttotheface',
	'password': 'J=p:s6M?D69m*XyF',
})
data['people'].append({
	'name': 'KlugSizzlin',
	'password': "%c,S=ZY4!D77U=,x",
})
data['people'].append({
	'name': 'Limentia',
	'password': "bFYQbV6tU]'Cn:CR",
})
data['people'].append({
	'name': 'a896b269',
	'password': "?6t@w9zNVXR<g,=\\",
})
data['people'].append({
	'name': 'MissChronos96',
	'password': '~@~8)XL[EM}TduG,',
})
data['people'].append({
	'name': 'maamuumm',
	'password': 'f3p$L~,6+vZWC(VR',
})
data['people'].append({
	'name': 'defcon84',
	'password': '"7L$Q=5t=):AsN;?',
})
data['people'].append({
	'name': 'DestinationAlpha',
	'password': 'QprgJ:n%LCy`65Xz',
})
data['people'].append({
	'name': 'HighlyNarrational',
	'password': 'WD.h+<7:hT@T9<QL',
})
data['people'].append({
	'name': 'TheSuperTeam',
	'password': 'k6A)PX@m2{AVHps&',
})
data['people'].append({
	'name': 'juxtapolice',
	'password': "h.&>6mc'g3SC+6~^",
})
data['people'].append({
	'name': 'marissa69',
	'password': "^FM:Y$g7Q\\,:]%rP",
})
data['people'].append({
	'name': 'spoopy812',
	'password': 'FCT7Rbu%f8=mhqPG',
})
data['people'].append({
	'name': 'Infernal77',
	'password': 'c3$577`e$BcN(CYW',
})
data['people'].append({
	'name': 'SystemTermination',
	'password': "Za]rP'y.b2VUz3>w",
})      
data['people'].append({
	'name': 'dirtranger8',
	'password': 'jg*v8*q;%K#M@t=V',
})
data['people'].append({
	'name': 'deciduouslyappleslol',
	'password': "7Nx.56UE,+_/jdd!",
})
data['people'].append({
	'name': 'ultimatorium',
	'password': 'G^4@E=dms7`N}{[V',
})
data['people'].append({
	'name': 'daisyflower666',
	'password': 'eVd8RJ+Dnm_)Qn\\4',
})
data['people'].append({
	'name': 'Toffhud',
	'password': 'r)s<jB3\\7%W&#5d',
})
data['people'].append({
	'name': 'Treasure64',
	'password': 'J~2;j)7V}G(<L%8a',
})
data['people'].append({
	'name': 'DogsAnonymous',
	'password': "<;'R-rJ:mF@@x53V",
})
data['people'].append({
	'name': 'Tomas110',
	'password': 'qDYZ/%Arm`4E3t)T',
}) 
data['people'].append({
	'name': 'sarah880112',
	'password': 'Zu}xZ9%A4\\h9!N{%',
})
data['people'].append({
	'name': 'PickleJar',
	'password': '~V>G8%uh2"}Y@/#f',
})
data['people'].append({
	'name': 'PickleJar',
	'password': '~V>G8%uh2"}Y@/#f',
})
data['people'].append({
	'name': 'Alterra',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Axonpixel',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'PlanetNiberu',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Boltor9',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'aboxpair',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'BullSheert',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'DaComploy',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'CuteAndClassy',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Cyberstem8',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Featurama',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'InterestInComfort',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Isysalga33',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Kinghery',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'LinkinAlone',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Lovessa',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'MaxiDirty',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Numbecker',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Playernegative',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'TheRadiantWeaver',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Selfid',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Slyfm',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Smazester',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Spiceller',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'theresatabinside',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Thesoyerox',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Theiferoni',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Tucklist',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Vallieme',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Virtuostring',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'apieric674',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Baytono',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'ABillionMessages',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Cottonperfection',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'CrashPierce',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Czardi',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'DeluxePal44',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Dreastray',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'enjoy44',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'EverBoz',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'ForlifeBlazee',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'gleedital86',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'TheInvaderLudites',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Kaptaineti64',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'kidlipie',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Kinetfir',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Lexog33',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'LiveBad9009',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'MaxExotica',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'nonridym',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Odelucti9',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'PlusMdogg1',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'qmotaxsta',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Restricity',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'theriderpac',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'TheRitziLady',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'RoseSchool',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'Sionati',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'SnoopyTheFox',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'TheTritium',
	'password': 'c,S=ZY4!D77U=,x',
})
data['people'].append({
	'name': 'themilitiacorp',
	'password': 'c,S=ZY4!D77U=,x',
})
random.shuffle(data['people'])

minds_api = Minds(Profile("dConnect312","dC12-4"))

leadInternal = 0
leadExternal = 1

# internal = add the GUIDs of the other robots
# this allows for cross-pollination of external feeds
aguids = []
if leadInternal == 1:
	for p in data['people']:
		res = minds_api.get_channel(p['name'])
		if ('channel' in res):
			aguids.append(res['channel']['guid'])
		else:
			print('warning: missing channel info ' + p['name'])
			print(res)

# the newsfeed of the robot has posts from other accounts
# our intent is to grab the others that liked the posts of the other accounts
# and inject them into our funnel, giving them attention and subscriptions
# this will hopefully draw them in...
def get_leads(api,name):
	_guids = []
	g = api.get_channel(name)['channel']['guid']
	lead_posts = api.newsfeed_channel(g)

	if lead_posts['status'] == "success":
		for i in lead_posts['activity']:
			_i = i
			if _i['remind_object'] != False:
				_i = i['remind_object']

			c = 0
			if (c < 10 and _i['type'] == "activity"):
				counter = 0
				random.shuffle(_i['thumbs:up:user_guids'])
				for x in _i['thumbs:up:user_guids']:
					_guids.append(x)
					counter = counter + 1
				for x in _i['thumbs:down:user_guids']:
					_guids.append(x)
					counter = counter + 1
				c = c + 1
	return _guids

#if leadExternal == 1:
#	lead_posts = get_leads(minds_api,"dConnect312")

counter = 0
maximum = 100
subscribe = 1
if len(sys.argv) > 1:
	subscribe = int(sys.argv[1])
remind = 0
if len(sys.argv) > 2:
	remind = int(sys.argv[2])

print("subscribe: " + str(subscribe))
print("remind: " + str(remind))
print()

# for every robot, run this
def subrun(p):
	counter = 0

	print("> " + p['name'] + ".")
	minds_api = Minds(Profile(p['name'],p['password']))
	time.sleep(1)

	# load up potential profiles to browse - internal (insiders) and external (public minds)
	guids = []
	if leadExternal == 1:
		guids = get_leads(minds_api,p['name'])
	if leadInternal == 1:
		for x in aguids:
			guids.append(x)
	random.shuffle(guids)

	# go through at least 5 profiles up to MAXIMUM
	for x in range(0,random.randint(5,maximum)):

		target = random.choice(guids)
		
		s = 0
		pp = minds_api.newsfeed_channel(target,1,3)
		time.sleep(1)

		# scan their posts for things to remind, like, etc
		if pp['status'] != 'success' or pp.get('activity') == None:
			continue
		
		if len(pp['activity']) == 0:
			continue
		
		try:
			for _xx in pp['activity']:
				xx = _xx
				r = 0

				if xx['remind_object'] != False:
					xx = xx['remind_object']
					
				# block blacklisted posts
					
				#oo = minds_api.newsfeed_channel(xx['owner_guid'],0,1)
				#if oo['status'] == 'success' and oo.get('activity') != None:
				#	xx = oo['activity'][0]
					
				# only from past 24hrs
				epoch = time.time()
				if xx['guid'] != False and int(xx['time_created']) < epoch and int(xx['time_created']) > epoch - (86400 * 3):
					if xx['guid'] in blacklist:
						continue
						
					if xx.get('guid') == None:
						xx['guid'] = xx['entityGuid']

					# try and cancel out NSFW
					sfw = 1
					if "sexy" in xx['message'] or "#girl" in xx['message']:
						sfw = 0
						print("NSFW")
						print(xx['message'])
						continue
						
					# if haven't subscribed, then like
					if s == 0 and sfw == 1:
						if testmode == 0:
							minds_api.upvote(xx['guid'])
						print(" L " + p['name'] + ' ' + xx['guid'])
						r = 1
						time.sleep(random.randint(40,600))
					
					# share if desired
					if remind == 1 and r == 1 and random.choice([0,0,1]) == 1 and sfw == 1:
						if testmode == 0:
							minds_api.remind(xx['guid'])
						s = 1
						r = 0
						print(" | R " + p['name'] + ' ' + xx['guid'])
						time.sleep(random.randint(140,800))
					
		except Exception as e:
			print(" ? failed " + str(e))
			s = 1
	
		# attempt to subscribe
		if subscribe == 1 and s == 1 and random.choice([1,1,1,0]) == 1:
			try:
				print(" | S " + p['name'] + " " + str(target))
				if testmode == 0:
					minds_api.subscribe(target)
					time.sleep(50,600)
			except Exception as e:
				print(" ? failed")
			counter = counter + 1

	for _x_ in nosub_list:
		if testmode == 0:
			minds_api.unsubscribe(_x_)
		print(" U - " + str(_x_))
		time.sleep(random.randint(8,10))

	print(" ^ " + p['name'] + " done.")			
	return

# do this for every one of our robots
random.shuffle(data['people'])
for p in data['people']:
	try:
		_thread.start_new_thread(subrun,(p,))
		if testmode == 1:
			time.sleep(10)
		else:
			time.sleep(random.randint(40,240))
	except Exception as e:
		print(e)
		continue

# keep program alive until complete
while 1 == 1:
	time.sleep(1)
