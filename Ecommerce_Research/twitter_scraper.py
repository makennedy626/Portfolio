######################################
##### Mining Twitter API #############
######################################

# https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/post-statuses-filter.html

import tweepy
from tweepy import OAuthHandler
 
consumer_key = '8AZsgftPqH9dbyLfc5IFWo39v'
consumer_secret = 'MuMAVS7rIEYa0dsyauTOeJMkjRgmU5NEvG2uzyOtWItJLli48u'
access_token = '963889537842851841-FGZVIMTpgCS760gVa3xNu9okSg8hB0j'
access_secret = 'obZiBaCujDaDzgT50s3q5fuKUTkvQuouQ57wUfl1YH2us'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

import json
import requests

car_audio_json = [status for status in api.search(q='Car Audio', lan='en')] 
# Optional paramters: [, locale][, rpp][, page][, since_id][, geocode][, show_user])

query = 'Car Audio'

car_audio_tweets = [status for status in tweepy.Cursor(api.search, q=query, tweet_mode='extended').items(100)]

ca_text = []
for text in car_audio_tweets:
    ca_text.append(text.full_text)
	
# Store the lists of texts into a DataFrame
import pandas as pd
texts = {'Category':[], 'Text':[]}
columns = texts.keys()
all_texts = pd.DataFrame(data=texts, columns=columns)
all_texts

texts = {'Category':'ca_text', 'Text':ca_text}
all_texts = all_texts.append(pd.DataFrame(data=texts, columns=texts.keys()))

query = 'Walkie Talkies'

walkie_talkie_tweets = [status for status in tweepy.Cursor(api.search, q=query, tweet_mode='extended').items(100)]

wt_text = []
for text in walkie_talkie_tweets:
    wt_text.append(text.full_text)
	
texts = {'Category':'wt_text', 'Text':wt_text}
all_texts = all_texts.append(pd.DataFrame(data=texts, columns=texts.keys()))

query = 'radar detector'

radar_detector_tweets = [status for status in tweepy.Cursor(api.search, q=query, tweet_mode='extended').items(100)]

rd_text = []
for text in radar_detector_tweets:
    rd_text.append(text.full_text)
	
texts = {'Category':'rd_text', 'Text':rd_text}
all_texts = all_texts.append(pd.DataFrame(data=texts, columns=texts.keys()))

# Save DataFrame object to csv
# Set index=False to prevent the extra column of the original indices
# all_texts.to_csv(path_or_buf=r'D:\GitHub\Final Capstone\Ecommerce Data\Tweets.csv', index=False)

# Now that the csv has been created, append it by writing with mode='a'
f = 'D:\GitHub\Final Capstone\Ecommerce Data\Tweets.csv'
all_texts.to_csv(f, mode='a', header=False, index=False)

print('Done!')