import json
import os


date=[]
retweets=[]
favourites=[]
mentions=[]
json_data=None
path=""

def setPath():
	global path
	tpath = __file__
	path=os.path.dirname(tpath)+"/chart1.json"
	print path

def openFile():
	with open(path) as json_file:
		json_data = json.load(json_file)
		for i in json_data:
			date.append(str(i["date"]))
			retweets.append(i["ntweets"])
			mentions.append(i["nmentions"])
			favourites.append(i["nfavorite"]/1000)

def getTweets():
	return retweets
def getFavourites():
	return favourites
def getMentions():
	return mentions

# print(favourites)

	# date+=json_data["date"]
        # "date": "2014-12-22", 
        # "ntweets": 9, 
        # "nmentions": 8, 
        # "nfavorite": 1918