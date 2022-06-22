#This is a sentiment analysis program that parses the tweets fetched from twitter using python and return their polarity
import os
import requests
from flask import Flask,redirect, render_template, request
import numpy as np
import tweepy 
import pandas as pd
from textblob import TextBlob
from wordcloud import WordCloud
import re

app = Flask(__name__)
@app.route('/sentiment', methods = ['GET','POST'])
def sentiment():
    userName = request.form.get('userName')
    hashtag = request.form.get('hashtag')

    if userName == "" and hashtag == "":
        error = "Please Enter any of the field to procceed!"
        return render_template('index.html', error=error)
    
    if not userName == "" and not hashtag == "":
        error = "Only one entry is allowed at ago!"
        return render_template('index.html', error=error)

    if userName == "@" + "userName" and not hashtag == "#" + "hashtag":
        error = "follow instructions"
        return render_template('index.html', error=error)

    # Twitter API credentials
    consumerKey = "pHbWHQfUNAJEpeWzssvJRwqmM"
    consumerSecret = "GP1bkJKJqYBzw98RF220zl7XMMbKxgy7OkO9CvQ0QsdtObWruI"
    accessToken = "1499257066627772416-1sAEN9AWYzGM9arMVVv0RtzPDznRuB"
    accessTokenSecret = "TrnfK51OhAinu0JUgzRHp9ZGSFJEby32HilajDm0s7aWn"
    
    #Authentication
    authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)
    authenticate.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(authenticate, wait_on_rate_limit = True)
    
    # Creating a function to clean of tweets
    def cleanTxt(text):
        text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
        text = re.sub('#', '', text) # Removing '#' hash tag
        text = re.sub('RT[\s]+', '', text) # Removing RT
        text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
        return text
        
        #Create a function to get the subjectivity
    def getSubjectivity(text):
        return TextBlob(text).sentiment.subjectivity

        #Create a function to get the polarity
    def getPolarity(text):
        return TextBlob(text).sentiment.polarity

        #Create a function to compute the positive, neutral and negative analysis
    def getAnalysis(score):
            if score > 0:
                return 'Positive'
            elif score == 0:
                return 'Neutral'
            else:
                return 'Negative'

    if userName == "":
        # hash tag coding
        msgs = []
        msg =[]
        for tweet in tweepy.Cursor(api.search_tweets,q="hashtag", tweet_mode='extended').items(500):
            msg = [tweet.full_text] 
            msg = tuple(msg)                    
            msgs.append(msg)

        df = pd.DataFrame(msgs)
        df['Tweets'] = df[0].apply(cleanTxt)
        df.drop(0, axis=1, inplace=True)
        df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
        df['Polarity'] = df['Tweets'].apply(getPolarity)
        df['Analysis'] = df['Polarity'].apply(getAnalysis)
        positive = df.loc[df['Analysis'].str.contains('Positive')]
        negative = df.loc[df['Analysis'].str.contains('Negative')]
        neutral = df.loc[df['Analysis'].str.contains('Neutral')]


        negative_per = round((negative.shape[0]/df.shape[0])*100, 1)
        positive_per = round((positive.shape[0]/df.shape[0])*100, 1)
        neutral_per = round((neutral.shape[0]/df.shape[0])*100, 1)

        return render_template('sentiment.html', name=hashtag,positive=positive_per,neutral=neutral_per, negative=negative_per)
    else:
        # user coding
        userName = "@"+userName

        post = api.user_timeline(screen_name=userName, count = 500, lang ="en", tweet_mode="extended")
        twitter = pd.DataFrame([tweet.full_text for tweet in post], columns=['Tweets'])

        twitter['Tweets'] = twitter['Tweets'].apply(cleanTxt)
        twitter['Subjectivity'] = twitter['Tweets'].apply(getSubjectivity)
        twitter['Polarity'] = twitter['Tweets'].apply(getPolarity)

        twitter['Analysis'] = twitter['Polarity'].apply(getAnalysis)
        positive = twitter.loc[twitter['Analysis'].str.contains('Positive')]
        negative = twitter.loc[twitter['Analysis'].str.contains('Negative')]
        neutral = twitter.loc[twitter['Analysis'].str.contains('Neutral')]

        positive_per = round((positive.shape[0]/twitter.shape[0])*100, 1)
        negative_per = round((negative.shape[0]/twitter.shape[0])*100, 1)
        neutral_per = round((neutral.shape[0]/twitter.shape[0])*100, 1)

        return render_template('sentiment.html', name=userName,positive=positive_per,negative=negative_per,neutral=neutral_per)

@app.route('/')
def home():
    return render_template('index.html')

app.run(debug=True)
