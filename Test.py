# from Twitter import TweetByType
from Twitter import TweetsByType
from Twitter import Engagement
from Twitter import EngagementByDay
# a = Twitter.getRetweetCount()
# TweetsByType.setPath()
# print TweetsByType.getRetweetCount()
EngagementByDay.setPath()
EngagementByDay.process()
print EngagementByDay.getTweets()
print EngagementByDay.getFav()
print EngagementByDay.getMen()
print EngagementByDay.getEng()
# Engagement.openFile()
# print Engagement.getMentions()
# print Engagement.getTweets()
# print Engagement.getFavourites()

# def getTweets():
# 	return tweet_days

# def getFav():
# 	return fav_days

# def getMen():
# 	return mention_days


# def getEng():
# 	return eng_days