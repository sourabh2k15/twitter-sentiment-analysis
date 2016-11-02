
from math import *

import Self_NB
import feature_vector


def call_NB(data_list,feature_list):
	#Calling Self Implemented Naive Bayes
	
	
	
	length = len(data_list)
	
	CF = 10
	i = 0
	
	testing_length = int(ceil(length/CF))
	print("Testing data length : ", testing_length)
		
	training_length = length-testing_length
	print("Training data length : ",training_length)
	
	acc = []
	
	for i in range(CF):
		
		NB_obj = Self_NB.NaiveBayesClassifier()
		
		cnt_true = 0
		
		start = i*testing_length
		end = start + testing_length
		
		testing_set = data_list[start:end]
		
		training_set1 = data_list[0:start]
		training_set2 = data_list[end:]
		training_set = training_set1 + training_set2
	
		#Training
		for j in training_set :
			f = feature_vector.to_feature_vector(j[0],feature_list)
			#feature_set.append(f,i[1]))
			training_row = (f,j[1])
			NB_obj.train(training_row)
			
	
		#Testing
		for j in testing_set:
			f = feature_vector.to_feature_vector(j[0],feature_list)
			testing_row = (f,j[1])
			if NB_obj.test(testing_row) == True:
				cnt_true += 1	
				
		#print cnt_true
		#Accuracy prediction
		
		acc.append((float(cnt_true)/testing_length)*100)
		print "Accuracy predicted by Self Implemented Naive Bayes on attempt ", i+1 , acc[i]
		
	print("Overall accuracy by Self Implemented Naive Bayes algo",sum(acc)/CF)
				
		#print feature_set
		
		#print feature_set	