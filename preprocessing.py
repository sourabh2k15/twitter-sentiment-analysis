#Beginning of Twitter sentiment analysis
#Preprocessing twitter tweets

import re

def preprocess(tweet):
	
	#Converting tweet to lower case
	tweet = "".join(tweet)
	#print tweet
	tweet = tweet.lower()
	
	#re.sub(pattern,replacement,string,max_count,flag) -> replace pattern found in string with replacement 
	#Replacing all instances of @Username in  tweet
	tweet = re.sub('@[\S]+',"__USER__",tweet)			#\S - matches nonwhitespace character
	
	#Replacing all urls in tweet
	tweet = re.sub('(www\.[\S]+)|(https?://[\S]+)',"__URL__",tweet)
	
	#Replacing hashtags without hash ex- #IPL by IPL
	tweet = re.sub('#',"",tweet)	
	
	#Remove whitespace from beginning and end
	tweet = tweet.strip()
	
	#Remove first/last (')/(") 
	tweet = tweet.lstrip('\'"')
	tweet = tweet.rstrip('\'"')
	
	#print tweet
	
	
	return tweet




