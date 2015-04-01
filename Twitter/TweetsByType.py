import json
import os
# with open(os.path.abspath("tweets.json")) as json_file:
#     json_data = json.load(json_file)
retweets=0
# print os.path.abspath("tweets.json")
path=""
json_data = None


def setPath():
	global path
	tpath = __file__
	# TweetsByType.abc()
	path=os.path.dirname(tpath)+"/tweets.json"	
	# print path
	# return __file__


def getReTweets():
	for i in json_data:
		retweets+=i["retweet_count"]
		# got a dictionary of status
	return retweets

def getTypeCount():
	import json
	# print path "/home/prahalad/Desktop/Fyp/Twitter/tweets.json"
	with open(path) as json_file:
		json_data = json.load(json_file)
	tweettype={"link":0,"media":0,"plaintext":0}
	typeretweet={"link":0,"media":0,"plaintext":0}
	for i in json_data:
		if(i.get("entities",-1)!=-1):
			# temp = i["entities"]["media"] 
			if(i["entities"].get("media",-1)!=-1):
				tweettype["media"]+=1
				typeretweet["media"]+=i["retweet_count"]					
			else:
				if(i["entities"].get("urls",-1)!=-1):
					if(len(i["entities"]["urls"])!=0):
						tweettype["link"]+=1
						typeretweet["link"]+=i["retweet_count"]
					else:
						tweettype["plaintext"]+=1
						typeretweet["plaintext"]+=i["retweet_count"]					
				else:
					tweettype["plaintext"]+=1
					typeretweet["plaintext"]+=i["retweet_count"]
	ttype=[0,0,0]
	ttype[0]= tweettype["plaintext"]
	ttype[1]= tweettype["media"]
	ttype[2]= tweettype["link"]
	return ttype
	# print typeretweet

def getRetweetCount():
	import json
	# print "Path is  : "+path
	with open(path) as json_file:
		json_data = json.load(json_file)
	typeretweet=[0,0,0]
	for i in json_data:
		if(i.get("entities",-1)!=-1):
			# temp = i["entities"]["media"] 
			if(i["entities"].get("media",-1)!=-1):
				# tweettype["media"]+=1
				typeretweet[1]+=i["retweet_count"]					
			else:
				if(i["entities"].get("urls",-1)!=-1):
					if(len(i["entities"]["urls"])!=0):
						# tweettype["link"]+=1
						typeretweet[2]+=i["retweet_count"]
					else:
						# tweettype["plaintext"]+=1
						typeretweet[0]+=i["retweet_count"]					
				else:
					# tweettype["plaintext"]+=1
					typeretweet[0]+=i["retweet_count"]
	# print typeretweet
	return typeretweet 

# getRetweetCount()

	
# print retweets
# got all retweets
    # print(json_data)