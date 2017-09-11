import tweepy
import configparser

#Initialize parser for reading config file
config = configparser.ConfigParser()

#Read from config file in the above directory
config.read('../keys.ini')

#Uses keys defined in the keys.ini file to authenticat connection with twitter account
#Don't forget to add your keys to keys.ini
auth = tweepy.OAuthHandler(config['OAuth']['public'], config['OAuth']['private'])
auth.set_access_token(config['AccessToken']['public'],config['AccessToken']['private'])

#Initialize tweepy api with authentication keys
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True) 

#TODO: Rename this file
#TODO: Add twitter bot stuff
