import csv
import random
import nltk

import processing_data_set
import preprocessing
import feature_vector
import all_words
import feature_words
import classifier


def Main():
	fp = csv.reader(open('Tweets_sample2.csv','rb'),delimiter=',',quotechar='"')
	
	data_list = processing_data_set.data_list(fp)
	
	random.shuffle(data_list)
	
	feature_list = []
	
	cnt = 0
	
	for i in data_list :
		
		i[0] = preprocessing.preprocess(i[0])
		
		i[0] = all_words.to_all_words(i[0])
		
		i[0] = feature_words.to_feature_words(i[0])
		#print i[1]
		feature_list.extend(i[0])
		
	#print feature_list
	feature_set = []
	
	print len(feature_list)
	
	#feature_list = list(set(feature_list))
	
	print len(feature_list)
	
	freq = nltk.FreqDist(feature_list)
	
	feature_list = list(freq.keys())[:1000]
	
	#print feature_list
	
	for i in data_list :
		f = feature_vector.to_feature_vector(i[0],feature_list)
		feature_set.append((f,i[1]))
		print cnt 
		cnt = cnt +1
		
	#print feature_set
	
	#print feature_set	
	
	classifier.NB_classifier(feature_set)
	

	

if __name__ == "__main__":
	Main()