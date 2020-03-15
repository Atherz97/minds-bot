from minds import Minds, Profile
import sys
import time, datetime
import random
import _thread

print(str(len(names)) + " to be registered")
# second run

def reg(x):
	p = "q&4.t9\k*mxW7j;#K-9!=Bh("
	minds_api = Minds(Profile(x,p),False)
	r = minds_api.register(x+str(random.randint(1930,1999))+"@"+random.choice(["einrot.com","teleworm.us","dayrep.com","jourrapide.com","armyspy.com","cuvox.de","fleckens.hu","gustr.com","rhyta.com","superrito.com"]))
	print(x)
	if r['status'] != "success":
		print(r)
	else:
		print("Registered: " + x + " Pass: " + p)

for x in names:
	try:
		_thread.start_new_thread(reg,(x,))
		time.sleep(5)
	except Exception as e:
		print(e)
		continue

while 1 == 1:
	time.sleep(1)
