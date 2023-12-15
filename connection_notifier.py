from ping3 import ping, verbose_ping
from preferredsoundplayer import *

hostname = "google.com"
sounded_up = False
sounded_down = False



def pingCount():
	count = 0
	count+= ping(hostname)
	count+= ping(hostname)
	count+= ping(hostname)
	return count


def checkMe():
	global sounded_up, sounded_down
	try:
		if pingCount() > 0:
			print("is up!")
			if sounded_up == False:
				soundplay("putin.mp3")
				sounded_up = True
				sounded_down = False
		else:
			print("is down!")
			if sounded_down == False:
				soundplay("boom.mp3")
				sounded_up = False
				sounded_down = True
	except TypeError:
		print("is down!")
		if sounded_down == False:
				soundplay("boom.mp3")
				sounded_up = False
				sounded_down = True
	pass
	



if __name__=="__main__": 
    while True:
    	checkMe()