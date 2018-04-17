import twitter
import os

def main():
    """Sets up API and searches for Tweets as specified"""
    twitter_api = setup_api() # Initialises API
    search_twitter(twitter_api,"'roger federer' OR tennis (suisse OR swiss) (url:news OR url:nouvelles) -lang:de") #Tweet search

def setup_api():
    """Gets user API credentials from .txt file"""
    filename = "api_creds.txt"
    credentials = []
    if os.path.isfile(filename):
        file = open(filename, "r") # Open file in read-only mode
        for line in file:
            credentials.append(line.split()[0]) # Read in credentials from .txt file
        api = twitter.Api(consumer_key = credentials[0], consumer_secret = credentials[1],
                          access_token_key=credentials[2], access_token_secret=credentials[3]) # Initialise API
        file.close()
        print "Api initialised"
    else:
        print "Could not find user credentials, exiting"
        exit()

    return api

def search_twitter(api, search_term):
    """Gets tweets as specified in search and converts them to a Python dictionary format (showing text and language)"""
    tweets = api.GetSearch(term = search_term, count = 100)
    tweets = [t.AsDict() for t in tweets] # Converting into a Python dictionary
    for t in tweets:
        print t ["text"], t ["lang"]

main()
