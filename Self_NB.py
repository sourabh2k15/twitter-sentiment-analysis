import math


#Implementation of Naive Bayes Classifier

class NaiveBayesClassifier():
	
	# features = A dictionary of features with key as feature word and value as count 
		
	#labels = A dictionary of labels for keeping track of different labels with key as label and value as count of lavel
		
	#count_feature_matrix = matrix in dictionary with key as label and value as "feature" dictionary
				
	def __init__(self):			
		self.labels = dict()
		self.count_feature_matrix = dict()
		self.fll = 0
		
		self.flag_arr = []
		
		
		
	#training_row = A tuple with dictionary of features and label 
	
	def train(self,training_row):
		
		#f is a dictionary
		f = training_row[0]
		l = training_row[1]
		
		feature_keys = f.keys()
		
		if l not in self.labels:
			self.labels[l] = 0
			
			
			feature = {}
			for key in feature_keys:
				feature[key] = 0
			
			#Adding feature_list for that label with initail value 0
			self.count_feature_matrix[l] = feature
		
		self.labels[l] += 1
		
		for i in feature_keys:
			if f[i] == True:
				self.count_feature_matrix[l][i] += 1
				
	
	
	def test(self,testing_row):
		
		f = testing_row[0]
		l = testing_row[1]
		
		
		#sum = 0
		
		if self.fll == 0:
			
			for i in f.keys():
				cnt = 0
				
				for l in self.labels.keys():
					cnt += self.count_feature_matrix[l][i]
					#print cnt
				#print cnt
				if cnt == 0:
					self.flag_arr.append(0)
				else :
					self.flag_arr.append(1)
				#sum += cnt
			#print sum
			#print self.flag_arr
		self.fll = 1
		
		label_predicted = self.predict(f)
		
		if label_predicted == l:
			return True
		else:
			return False
				
		
	
	def predict(self,feature_vector):
			
		diff_labels = self.labels.keys()
		feature_keys = feature_vector.keys()
		
		
		#Calculating probabilities for each label "l"
		
		# 							((P(f1|l) * P(f2|l) * .. * P(fn|l)) * P(l))
		# P(l|feature_vector) = --------------------------------------------------
		#									P(f1) * P(f2) * P(f3) * .. * P(fn')
		# for n' True features in feature_vector
		# Calculate log probabilities help to sum rather than multiply since we don't want the probaabilities , only want which one is greater
		# If some P(fi|l) is 0, log will produce unexpected result, so replacing it with zero probability for that label
		
		max_prob = -10000000.50
		prob = []			
		
		
		l_sum = 0.0
		
		for l in diff_labels:
			l_sum += float(self.labels[l])
		
		
		
		for l in diff_labels:
			flag = 0
			p = 0.0
			i = 0
			for f in feature_keys:
				if self.flag_arr[i] == 0:
					continue
				p1 = float(self.count_feature_matrix[l][f])
				p2 = float(self.labels[l])
				
				if feature_vector[f] == False:
					p1 = p2 - p1
				
				if p1>0:
					p += math.log(p1)
					p -= math.log(p2)
				
				else :	
					prob.append([0.0,l])
					flag = 1 
					break
				
				i = i + 1
					
					
			
									
			p += math.log(float(self.labels[l]))
			p -= math.log(float(l_sum))
			
			#print len(feature_keys)
				
			if flag == 0:
				i = 0
				for f in feature_keys:
					if self.flag_arr[i] == 0:
						continue
					cnt = 0.0
					for l2 in diff_labels:
						cnt += self.count_feature_matrix[l2][f]
						
					if feature_vector[f] == False:
						cnt = l_sum - cnt
								
					p -= math.log(float(cnt))	
					p += math.log(float(l_sum))
					
					i = i + 1
				
				prob.append([p,l])
			
			#if flag == 0:
			#	prob.append([p,l])
			
		#Findind label corresponding to maximum probability
		
		#Some random number for label
		label_predicted = diff_labels[0]
	
		#print prob
		
		for i in prob:
			if max_prob < i[0] :
				max_prob = i[0]	
				label_predicted = i[1]
			
			#Tie-Break with label of maximum probability
			elif max_prob == i[0]:
				if self.labels[label_predicted] < self.labels[i[1]]:
					label_predicted = i[1] 
					
			
		return label_predicted
				
		
		
		
	