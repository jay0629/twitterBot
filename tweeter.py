import tweepy


consumer_key = '85ENf6nJ6BbAUp21kj0JxHW0l'
consumer_secret = '8j8gwF64JDNAwEndjKIAUV46X2OrlGWSVbyrh3HUSC5R0TQdgz'
access_token = '1098669896240717829-bbr4wd0P6LOX8ymhdrLzfbhfvqh5tp'
access_token_secret = 'M3nMepB8TDS8zEaGESr42CvGAVqvshNfSeoG9ZbGcE9ax'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)


def retweet():
    search = ('#myfirstTweet')
    for tweet in tweepy.Cursor(api.search, search).items(1):
        try:
            api.retweet(tweet)
            
            print('@First tweet has been auto retweeted')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def main():
    retweet()

    
if __name__ == "__main__":
    main()



