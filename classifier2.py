import nltk
import random
from math import *
from nltk.classify import *

#A wrapper to include scikit learn classifier in nltk classifier module
#from nltk.classify.scikitlearn import SklearnClassifier

from nltk.classify.scikitlearn import SklearnClassifier

#from scikitlearn1 import SklearnClassifier

#from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC,LinearSVC
#from sklearn.linear_model import LogisticRegression

featurelist = []

def extract_features(tweet):
	words = set(tweet)
	features = {}
	for w in featurelist:
		features[w] = (w in words)
	
	return features 


def NB_classifier(data_list,feature_list):
	
	acc_NB = []
	acc_MNB = []
	acc_LSVC = []
	acc_SVC = []
	acc_LR = []
	acc = []
	
	global featurelist
	
	featurelist = feature_list
	
	
	#print data_list[:10]
	
	feature_set = util.apply_features(extract_features,data_list)
	
	print feature_set[:2]
	
	#random.shuffle(feature_set)
	
	length = len(feature_set)
	
	#print feature_set[:10]
	
	#print length
	
	#No. of cross folds
	CF = 4
	i = 0
	
	testing_length = int(ceil(length/CF))
	print("Testing data length : ", testing_length)
		
	training_length = length-testing_length
	print("Training data length : ",training_length)
	
	for i in range(CF):
		
		start = i*testing_length
		end = start + testing_length
		
		testing_set = feature_set[start:end]
		
		training_set1 = feature_set[0:start]
		training_set2 = feature_set[end:]
		training_set = training_set1 + training_set2
		
		NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
		acc.append((nltk.classify.accuracy(NBClassifier,testing_set))*100)
		print("Accuracy predicted by Naive Bayes Algorithm on attempt : ",i+1, (nltk.classify.accuracy(NBClassifier,testing_set))*100)
		
		'''
		#Naive Bayes
		NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
		acc_NB.append((nltk.classify.accuracy(NBClassifier,testing_set))*100)
		print "Accuracy predicted by Naive Bayes on attempt ", i+1 , acc_NB[-1]
		
		#Multinomial Naive Bayes
		MNBClassifier = SklearnClassifier(MultinomialNB())
		MNBClassifier.train(training_set)
		acc_MNB.append((nltk.classify.accuracy(MNBClassifier,testing_set))*100)
		print acc_MNB[-1]
		
		#Logistic LogisticRegression
		LRClassifier = SklearnClassifier(LogisticRegression())
		LRClassifier.train(training_set)
		acc_LR.append((nltk.classify.accuracy(LRClassifier,testing_set))*100)
		print acc_LR[-1]
		'''
		'''
		#SVC
		SVCClassifier = SklearnClassifier(SVC())
		SVCClassifier.train(training_set)
		acc_SVC.append((nltk.classify.accuracy(SVCClassifier,testing_set))*100)
		print acc_SVC[-1]
		
		'''
		'''
		#LinearSVC
		LSVCClassifier = SklearnClassifier(LinearSVC())
		LSVCClassifier.train(training_set)
		acc_LSVC.append((nltk.classify.accuracy(LSVCClassifier,testing_set))*100)
		print "Accuracy predicted by Linear SVM on attempt ", i+1 , acc_LSVC[-1]
		
		'''
	
	#print("Accuracy by Naive bayes on different folds : ",acc)
	acc = sum(acc)/CF
	#print("Overall accuracy by Naive bayes algo",acc)
	'''
	print("Accuracy by Multinomial Naive bayes on different folds : ",acc_mNB)
	acc = sum(acc_MNB)/CF
	print("Overall accuracy by Multinomial Naive bayes algo",acc)
	
	print("Accuracy by LogisticRegression on different folds : ",acc_LR)
	acc = sum(acc_LR)/CF
	print("Overall accuracy by LogisticRegression algo",acc)
	
	print("Accuracy by SVC on different folds : ",acc_SVC)
	acc = sum(acc_SVC)/CF
	print("Overall accuracy by SVC algo",acc)
	
	
	#print("Accuracy by Linear SVC on different folds : ",acc_LSVC)
	acc = sum(acc_LSVC)/CF
	print("Overall accuracy by Linear SVC algo",acc)
	
	print "\n\n"
	
	print "Overall accuracy " , sum(acc)/CF
	
	
	'''