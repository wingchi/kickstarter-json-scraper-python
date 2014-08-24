import json
import requests
import datetime

csv_output = open("top-funded.csv", "w")

for page in range(1,26):
    r = requests.get('https://www.kickstarter.com/discover/advanced.json?category_id=0&woe_id=0&sort=most_funded&page=' + str(page))
    data = r.json()
    for index in range(len(data["projects"])):
        #print "%s,%f,%s,%f" % (data["projects"][index]["name"], data["projects"][index]["goal"], data["projects"][index]["currency"], data["projects"][index]["pledged"])
        csv_output.write("\"%s\",%s,%.0f,%s,%.2f,%d,%s,%s,%s\n" % (data["projects"][index]["name"].encode('ascii', 'ignore'), 
            data["projects"][index]["category"]["name"],
            data["projects"][index]["goal"], 
            data["projects"][index]["currency"], 
            data["projects"][index]["pledged"],
            data["projects"][index]["backers_count"],
            str(datetime.datetime.fromtimestamp(data["projects"][index]["created_at"])),
            str(datetime.datetime.fromtimestamp(data["projects"][index]["launched_at"])),
            str(datetime.datetime.fromtimestamp(data["projects"][index]["deadline"]))))

csv_output.close()

#data = json.load(urllib2.urlopen('https://www.kickstarter.com/discover/advanced.json?category_id=16&woe_id=0&sort=most_funded&page=1'))