import json
import os

tpath = __file__
# path=os.path.dirname(tpath)+"/chart1.json"
path=os.path.dirname(tpath)+"/tweets.json"
print os.path.dirname(tpath)
print path

with open(path) as json_file:
	json_data = json.load(json_file)

for i in json_data:
	if(i.get("Entities",-1)!=-1):
		if(i["Entities"].get("user_mentions",-1)!=-1):
			print i["Entities"]["user_mentions"]
