import nltk
import random
from math import *
from nltk.classify import *



def NB_classifier(feature_set):
	
	random.shuffle(feature_set)
	
	length = len(feature_set)
	
	testing_length = int(ceil(length/4))
	print("Testing data length : ", testing_length)
	
	training_length = length-testing_length
	print("Training data length : ",training_length)
	
	training_set = feature_set[:training_length]
	
	testing_set = feature_set[training_length:]
	
	NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
	
	#NBClassifier = nltk.NaiveBayesClassifier.train(NBClassifier, training_set)
	
	
	print("Accuracy predicted by Naive Bayes Algorithm : ", (nltk.classify.accuracy(NBClassifier,testing_set))*100)
	
	print('\n\n')
	
	NBClassifier.show_most_informative_features(15)
	
	