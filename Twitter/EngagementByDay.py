import json
import datetime
import os


path=""
eng_days={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0}
tweet_days={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0}
mention_days={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0}
fav_days={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0}

def dayOfWeek(dt):
	year, month, day = (int(x) for x in dt.split('-'))  
	temp = datetime.date(year, month, day).isoweekday()	
	if(temp==1):
		return "Monday"
	elif(temp==2):
		return "Tuesday"
	elif(temp==3):
		return "Wednesday"
	elif(temp==4):
		return "Thursday"
	elif(temp==5):
		return "Friday"
	elif(temp==6):
		return "Saturday"
	else:
		return "Sunday"			

def setPath():
	global path
	tpath = __file__
	path=os.path.dirname(tpath)+"/chart1.json"
	# print path


def process():
	with open(path) as json_file:
		json_data = json.load(json_file)
	global eng_days
	global fav_days
	global mention_days
	global tweet_days
	for i in json_data:
		day = dayOfWeek(i["date"])
		mention_days[day]+=i["nmentions"]
		fav_days[day]+=int(i["nfavorite"]/1000)
		tweet_days[day]+=i["ntweets"]
		eng_days[day]+=(i["nmentions"]+int(i["nfavorite"]/1000)+i["ntweets"])


def getTweets():
	return tweet_days.values()

def getFav():
	return fav_days.values()

def getMen():
	return mention_days.values()

def getEng():
	return eng_days.values()
