import csv
import random
import nltk

import processing_data_set
import preprocessing
#import feature_vector
import all_words
import feature_words
import classifier2
import svmclassifier
import classifier_Self_NB




def Main():
	fp = csv.reader(open('Tweets_sample2.csv','rb'),delimiter=',',quotechar='"')
	
	#fp = open('../Data_Set/kaggle.txt','rb')
	
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
		
	
	
	#print len(feature_list)
	
	
	#Preparing a dictionary of words in feature_list and maintaining their count
	
	dic = {}
	
	for i in feature_list:
		if i in dic:
			dic[i] = dic[i] + 1
		else:
			dic[i] = 1
	
	print len(dic)
			
	#Reverse sorting the dictionary to get most frequently used words
	
	#print dic
			
	feature_list =  sorted(dic , key = dic.__getitem__ , reverse = True)[:3000]
		
	print "Length of feature list " , len(feature_list)
	
	#print feature_list[:15]	
	
	
	'''
	data_list2 = []
	
	for i in data_list:
		data_list2.append((i[0],i[1]))
	'''
	
	#classifier_Self_NB.call_NB(data_list,feature_list)
	
	
	classifier2.NB_classifier(data_list,feature_list)
	
	#svmclassifier.SVMClassifier(data_list,feature_list)
	

	

if __name__ == "__main__":
	Main()