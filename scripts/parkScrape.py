import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import json


html = 'https://pcia2.com/parking-locations-availability/'

r = requests.get(html)

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('main', id='main')

e = s.find("tbody")

l = e.find_all("td")
#zZVs5pkrEsqPSdnkUwYhSfxXj

textList = []
for line in l:
    textList.append(line.text)

col_list=["structure","total","inUse","free","dateTime"]

n=4

def slice_per(source, step):
    return [source[i::step] for i in range(step)]

lists=slice_per(textList, 6)

print(lists)
data = list(zip(lists[0],lists[1],lists[2],lists[3],lists[4]))


df = pd.DataFrame(data, columns = col_list)


df.iloc[:,1:4] = df.iloc[:,1:4].astype(float)

recordTime = time.time()

df['recordTime'] = recordTime


with open("/home/saldutgr/parkingBot/output/a2_structure_data.txt", mode='a') as csvFile:
    df.to_csv(csvFile, header=False, index=False)


spaces={'freeSpaces': df['free'].sum(),\
       'squareFeet': df['free'].sum() * 180,\
        'time':recordTime}



tweet="Bleep, blorp...blop...There are currently " , "{:,}".format(round(spaces['freeSpaces'])),\
     " free spaces available in A2 parking lots. That's ", "{:,}".format(round(spaces['squareFeet'])), " square feet " \
        "of unused space in downtown Ann Arbor! Maybe the city could remove more on street parking and put that space to better use! "\
       "@A2DDA @A2GOV #a2council #parkingreform"

def convertTuple(tup):
    str = ''.join(tup)
    return str

str=convertTuple(tweet)

spaces['tweet'] = str

print(df)

with open("/home/saldutgr/parkingBot/output/tweet.json", "w") as outfile:
    json.dump(spaces, outfile)




