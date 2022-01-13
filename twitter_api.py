import tweepy
import configparser
import os 
import pandas as pd



# read credentials from config file
path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])

config = configparser.ConfigParser()
#config.read('config.ini')
config.read(os.path.join(path, 'config.ini'))


api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']


# aunthenticate

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
#print(public_tweets)
#print(public_tweets[0].text)

#for tweet in public_tweets:
#    print(tweet.text)

## saving tweets

#created_at  - when tweet happened
#text - text of tweet
#user.screen_name - who tweeted

columns = ['Time','User','Tweet']
data = []

for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])
                
df = pd.DataFrame(data, columns=columns)

df.to_csv('sampletweets.csv')