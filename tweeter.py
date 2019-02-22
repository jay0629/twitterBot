#!/usr/bin/python3.5

import tweepy
import os
from datetime import datetime, timedelta

# Displays tweeters ID based on a search of the name of the tweet.
# This is over a seven day period and 100 users

consumer_key = '85ENf6nJ6BbAUp21kj0JxHW0l'
consumer_secret = '8j8gwF64JDNAwEndjKIAUV46X2OrlGWSVbyrh3HUSC5R0TQdgz'
access_token = '1098669896240717829-bbr4wd0P6LOX8ymhdrLzfbhfvqh5tp'
access_token_secret = 'M3nMepB8TDS8zEaGESr42CvGAVqvshNfSeoG9ZbGcE9ax'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def idTweet():
    comment = 'myfirstTweet'
    numberOfUsers = 100
    now = datetime.today().now()
    days = now-timedelta(days=7)
    now = now.strftime("%Y-%m-%d")
    prev = days.strftime("%Y-%m-%d")
    print('For the last 7 days these were the top 100 tweets labeled '
          + comment + ' by: \n')
    for tweet in tweepy.Cursor(api.search, comment,
                               since=prev,
                               until=now
                               ).items(numberOfUsers):
        print('@' + tweet.user.screen_name)


def main():
    idTweet()


if __name__ == "__main__":
    main()
