

def feature_list_extractor(fp):
	
	line = fp.readline()
	
 	while line :
		 
		feature_list = []
		#According to list of tweets and sentiments ,to be modified
		row = line.split()
		sentiment = row[0]
		tweet = row[1]
		 
		tweet = preprocess(tweet)
		
		tweet_all_words = all_words(tweet)
		
		#Selecting feature words
		feature_word_list = feature_words(tweet_all_words)
		
		feature_list.extend(feature_word_list)
		
		line = fp.readline()
	
	#Removing duplicates from feaature_list and making a set
	#feature_list = list(set(feature_list))
	return feature_list
		
		
		 
	
	
