from flask import Flask
from flask import render_template
# import Database
# import Interaction
# from flask import 
#from flask import request

app = Flask(__name__)

@app.route("/Test")
def getData():
	return render_template("Template.html")

@app.route("/")
def hello():
    return render_template("blank-page.html")
#render_template("Index.html")


@app.route("/TwitterChart")
def TwitterCharts():
    return render_template("TwitterChart.html")


@app.route("/Form")
def Form():
    return render_template("Form.html")

@app.route("/EngagementByTweets")
def Engagement():
	from Twitter import TweetsByType
	TweetsByType.setPath()
	ept = TweetsByType.getRetweetCount()
	tweets = TweetsByType.getTypeCount()
	return render_template("EngagementByTweets.html",ept=ept,tweets=tweets)

@app.route("/EngagementBreakdown")
def EngagementBreakdown():
	from Twitter import Engagement
	Engagement.setPath()
	Engagement.openFile()
	Retweets =  Engagement.getTweets()
	Favourites = Engagement.getFavourites()
	Mentions = Engagement.getMentions()
	return render_template("EngagementBreakdown.html",Retweets=Retweets,Favourites=Favourites,Mentions=Mentions)

@app.route("/EngagementByDay")
def EngagementByDay():
	from Twitter import EngagementByDay
	EngagementByDay.setPath()
	EngagementByDay.process()
	Tweets = EngagementByDay.getTweets()
	Favourites = EngagementByDay.getFav()
	Mentions =  EngagementByDay.getMen()
	Engagement = EngagementByDay.getEng()
	return render_template("EngagementByDay.html",Tweets=Tweets,Favourites=Favourites,Mentions=Mentions,Engagement=Engagement)

@app.route("/User/<name>")
def getDatas(name):
	# import facebook
	import json
	import requests
	# from io import StringIO
	# graph = facebook.GraphAPI("CAACEdEose0cBAG2JCfCzNvOrYmfbQZBqTjtTDWvzXLAB2ucneTHBFywuJZBrjAZCEgCKJoZCvLfdFdgvHHUihZCdPuGBVZCpEHHKdm2a6Nen4MyHMHY7f9gHCnoKBTN7tiKi7lkZBUtC9jbwYHdNZCCypGXlDzm5nTRTxj6ZBuCmthr1GUnWO5oqCdeXbIFd0ZBoDWXy0iMZAQ2Kd7LKTq2jgZBBQP9fQnwI5O8ZD")
	# graph = facebook.GraphAPI(graph.get_app_access_token("1071602432855000",""))	
		# "7dd132dbd223cca34c34ac81259c5d75")
	# obj = graph.get_object()
	url="https://graph.facebook.com/%s?fields=posts.limit(5){id,message,name,description,status_type,created_time,likes}"%(name)
	parameters = {'access_token': "CAACEdEose0cBAG2JCfCzNvOrYmfbQZBqTjtTDWvzXLAB2ucneTHBFywuJZBrjAZCEgCKJoZCvLfdFdgvHHUihZCdPuGBVZCpEHHKdm2a6Nen4MyHMHY7f9gHCnoKBTN7tiKi7lkZBUtC9jbwYHdNZCCypGXlDzm5nTRTxj6ZBuCmthr1GUnWO5oqCdeXbIFd0ZBoDWXy0iMZAQ2Kd7LKTq2jgZBBQP9fQnwI5O8ZD"}
	r = requests.get(url)
	posts = r.json()
	content =  json.dumps(posts['posts']['data']) 
	likes = content[6]['data']
	for k,v in content.iteritems():
		message = content["message"]
		description = content["description"]	
		status_type = content["status_type"]
		iid = content["id"]
		description = content["description"]
		created_time = content["created_time"]
		status_type = content["status_type"]
		# obj = Interaction(iid,message,status_type,likes,shares,comments,ctime)

	# json.loads(r.text)
	# return posts["data"]

	return content
	# add to DB here
	# ['posts']['data']
	# posts['data']
	# posts = graph.get_connections(id="flipkart", connection_name="posts")
	# ret=""
		# {id,message,name,description,status_type,created_time}")
	# message = posts["message"]
	# description = posts["description"]
	# status_type = posts["status_type"]
	# ret+="""
	# 		<h2> <span style='color:red'>%s</span> : %s </h2>
	# 		<br/><br/>	
	# """%("message" , message)
	# data = {}
	# data = json.dumps(profile["data"])
	# for k,v in posts.iteritems():
	# 	# if(k=="message" or k=="description"):
	# 		ret +="""
	# 		<h2> <span style='color:red'>%s</span> : %s </h2>
	# 		<br/><br/>
	# 		"""%(k,v)

		# ret +=  str(k)
		# ret += " : "
		# ret += str(v)
		# '<br/>'.join(str(ret))
		#ret += " \n \n "
	# ret1=""	
	# ret1+="""<br/> %s """%(posts[1]["message"])	
	# return ret
	#render_template ("Details.html",profile=profile)

# @app.route("/Details/<>")
# def Details():
    # return render_template("Index.html")
    
# https://graph.facebook.com/flipkart?fields=posts.limit(5){id,message,name,description,status_type,created_time,likes.summary(true)}
# @app.route("/Visualize/")
	# a=0


if __name__ == "__main__":
    app.debug = True 
    app.run()
