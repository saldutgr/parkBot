import tweepy
import json

#auth

API_KEY="kJHJXB20Sy9GsqnN8xwyTofif"
API_SECRET="xkD2Guo13af6IXj6HLsbYYT7FC8yytsuxPIE0WU269aDVCMM2c"
BEARER="AAAAAAAAAAAAAAAAAAAAAMqdjwEAAAAAkRPLFbvfjC%2BlbOavfqhnJ7RTNAI%3Dgu4vDnmO9yq2EVbpLyXozccInmrepPi6GusauZ0jrpr1g00ttG"
ACCESS_TOKEN="1597939792322371589-gAyhwgoYaYmOriAGIWwaGLakpnWkpI"
ACCESS_TOKEN_SECRET="vngktZOiApBZ6Pc6egpMKK5qO5RfmbOo0OAq9TSe6lO0B"


client=tweepy.Client(
consumer_key=API_KEY,
consumer_secret=API_SECRET,
bearer_token=BEARER,
access_token=ACCESS_TOKEN,
access_token_secret=ACCESS_TOKEN_SECRET)

#with open('../output/tweet.txt') as f:
#    tweet = f.readlines()

f=open("/home/saldutgr/parkingBot/output/tweet.json")
data = json.load(f)


client.create_tweet(text=data['tweet'])

