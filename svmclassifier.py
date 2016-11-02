import svm 
from svmutil import *

from math import *

labels = []
feature_set = []

def feature_vector(data_list,feature_list):
	
	different_labels = dict()
	cnt = 0
	
	for i in data_list:
		
		#Data_Set creation
		words = i[0]
		sample = [] 
		for j in feature_list:	
			if (j in words):
				sample.append(1)
			else:
				sample.append(0)
		feature_set.append(sample)
		
		#Label creation,variable number of labels
		
		l = i[1]
		if l in different_labels.keys():
			labels.append(different_labels[l])
		else:
			different_labels[l] = cnt
			cnt = cnt + 1
			labels.append(different_labels[l])

		
		

def SVMClassifier(data_list,feature_list):
	
	#Full Data_Set
	feature_vector(data_list,feature_list)
	
	
	#SVM params
	
	param = svm_parameter()
	param.C = 0.1
	param.kernel_type = LINEAR
	
	
	
	
	length = len(feature_set)
	print length
	
	#No. of cross folds
	CF = 4
	i = 0
	
	testing_length = int(ceil(length/CF))
	print("Testing data length : ", testing_length)
		
	training_length = length-testing_length
	print("Training data length : ",training_length)
	
	acc_SVM = []	
	
	for i in range(CF):
		
		start = i*testing_length
		end = start + testing_length
		
		testing_set = feature_set[start:end]
		testing_labels = labels[start:end]
		
		training_set1 = feature_set[0:start]
		training_set2 = feature_set[end:]
		training_set = training_set1 + training_set2
		training_label1 = labels[0:start]
		training_label2 = labels[end:]
		training_label = training_label1 + training_label2
		
		#print training_set[:100]
		#print training_label[:100]
		
		#Instantiate the problem
		problem = svm_problem(training_label,training_set)
		
		#Train it
		model = svm_train(problem,param)
		
		p_label,p_acc,p_val = svm_predict([0]*len(testing_set),testing_set,model)
		
		#print p_label
		#print "\n\n\n"
		#print p_acc
		#print "\n\n\n"
		#print p_val
		
		cnt_true = 0
		cnt_total = len(p_val)
		
		j=0
		
		for j in range(len(testing_labels)):
			testing_labels[j] = float(testing_labels[j])
		
		#print testing_labels
		
		for j in range(len(p_label)):
			if p_label[j] == testing_labels[j]:
				cnt_true = cnt_true +1
		
		acc_SVM .append((float(cnt_true)/cnt_total)*100)
		print "Accuracy on testing data on attempt ", i+1 , acc_SVM[i]
		
	
	
	#print("Accuracy by Naive bayes on different folds : ",acc_NB)
	acc = sum(acc_SVM)/CF
	print("Overall accuracy by Linear SVM algo",acc)
	
	