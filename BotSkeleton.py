import tweepy
import configparser

#Initialize parser for reading config file
config = configparser.ConfigParser()

#Read from config file
config.read('keys.ini')

#Uses keys defined in the config.ini file to authenticat connection with twitter account
#Don't forget to add your keys to config.ini
auth = tweepy.OAuthHandler(config['OAuth']['public'], config['OAuth']['private'])
auth.set_access_token(config['AccessToken']['public'],config['AccessToken']['private'])

#Initialize tweepy api with authentication keys
api = tweepy.API(auth) 

#TODO: Add twitter bot stuff