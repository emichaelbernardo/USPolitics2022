

# importing libraries

import configparser
import os

import pandas as pd
import numpy as np
import re
import string
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

## for twitter data
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud

## NLP imports
import nltk
from nltk.corpus import stopwords
stopwords = nltk.corpus.stopwords.words('english')
new_stopwords = ['amp','biden','know','say','today','start','week','want','day','talk','new','thank','birthday','wish','happy','discuss']
stopwords.extend(new_stopwords)

import spacy 

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction import text 
stop_words = text.ENGLISH_STOP_WORDS.union(new_stopwords)


import pyLDAvis
import pyLDAvis.sklearn


## Progressbar
from tqdm import tqdm




# login to twitter dev account
config = configparser.ConfigParser()
config.read('config.ini')



api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']


# aunthenticate

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth, wait_on_rate_limit=True)


## Read in Congress twitter accounts
senate = pd.read_excel(open('data/congress_twitter.xlsx', 'rb'),
              sheet_name='Senate')  
house = pd.read_excel(open('data/congress_twitter.xlsx', 'rb'),
              sheet_name='House')  



## read in data again for modeling
dem_clean        = pd.read_csv('data/dem_clean.csv')
gop_clean        = pd.read_csv('data/gop_clean.csv')
all_tweets_clean = pd.read_csv('data/all_tweets_clean.csv')


# Create Dem only df
senate_dems = senate[senate['Party ']=='D']
house_dems  = house[house['Party']=='D']
# combine house and senate dfs
all_dems_df = pd.concat([senate_dems,house_dems])
all_dems_df = all_dems_df.drop(all_dems_df.columns[[2,3,4,5]], axis=1)  # df.columns is zero-based pd.Index
# recreate party column and get account from Link column
all_dems_df['Party']='D' 
all_dems_df['Acct']= all_dems_df['Link'].str.replace('https://twitter.com/','',regex=True)
all_dems_df




# Create Gop only df
senate_gop = senate[senate['Party ']=='R']
house_gop  = house[house['Party']=='R']
# combine house and senate dfs
all_gop_df = pd.concat([senate_gop,house_gop])
all_gop_df = all_gop_df.drop(all_gop_df.columns[[2,3,4,5]], axis=1)  # df.columns is zero-based pd.Index

# recreate party column and get account from Link column
all_gop_df['Party']='R' 
all_gop_df['Acct'] = all_gop_df['Link'].str.replace('https://twitter.com/','',regex=True)




## Create combined list of accounts
all_congress_accounts = pd.concat([all_gop_df,all_dems_df])
all_congress_accounts.to_csv('data/cong_accounts.csv', encoding='utf-8', index=False)
all_congress_accounts



## Scrape tweets using acct names##

## Get 1000 recent tweets from user

def get_1k_Tweets(user):
    
    tweets = []
    columns=['User','Content','Date','Favs','RTs']
        
    for tweet in tweepy.Cursor(api.user_timeline,screen_name=user).items(1000):
        tweets.append([tweet.user.screen_name, 
                       tweet.text, 
                       tweet.created_at, 
                       tweet.favorite_count, 
                       tweet.retweet_count])
    tempdf = pd.DataFrame(tweets, columns=columns)
    return tempdf
    

    
all_congress_tweets = pd.DataFrame()
no_accts = []
for cong in tqdm(all_congress_accounts[214:].Acct):
    try:
        temp_tweets = get_1k_Tweets(cong)
        all_congress_tweets = pd.concat([all_congress_tweets,temp_tweets])
    except:
        no_accts.append(cong)
        print(f'{cong} account is not active or does not have tweets')
# write out data to csv

all_congress_tweets.to_csv('data/all_cong_tweets_01012021_01162022.csv', encoding='utf-8', index=False)   

## Get Political Party and Name of account 
full_Cong_df = pd.merge(all_congress_tweets,all_congress_accounts, left_on='User', right_on='Acct')

## Remove redundant columns (link and Acct)
full_Cong_df.drop(['Link','Acct'], axis=1, inplace=True)

## Write out full dataframe
full_Cong_df.to_csv('data/all_party_tweets_01012021_01162022.csv', encoding='utf-8', index=False)

        

        