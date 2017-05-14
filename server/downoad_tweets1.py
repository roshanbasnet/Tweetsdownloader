
import tweepy
import csv

def get_all_tweets(screen_name, count):

    # Twitter API Credential from the app you created in apps.twitter.com
    consumer_key = "" # consumer key
    consumer_secret = ""   # consumer secret
    access_key = ""      # access key
    access_secret = ""    # access secret


    # authorizing  twitter, initializing  tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    new_tweets = []
    if screen_name[0] == "@":
        print "downloading tweets of " + screen_name
        new_tweets = api.user_timeline(screen_name=screen_name, count=count, exclude_replies=True)
    else:
        print "downloading tweets releated to keywords " + screen_name
        new_tweets = api.search(q=screen_name,lang="en", includes_entities=False, count=count)

    print "...%s tweets downloaded" % (len(new_tweets))

    # transforming the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.text.encode("utf-8")]for tweet in new_tweets]

    # write the csv
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["text"])
        writer.writerows(outtweets)
    pass
    return outtweets

if __name__ == "__main__":
    username = raw_input("enter your username or any key word")
    #provide username or any key word and also the number of tweets you want to download
    tweet = get_all_tweets(username, 30)
