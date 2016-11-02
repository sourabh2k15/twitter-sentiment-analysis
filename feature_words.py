from nltk.stem.porter import *

#Feature word	
def to_feature_words(word_list):
	
	#Featurewordlist
	feature_word_list = []
	
	#Remove stopwords
	stopwords = []
	
	fp = open('stopwords.txt','r')
	
	for line in fp:
		word = line.strip()
		stopwords.append(word)
	
	#ADD __USER__ , __NUM__ , __URL__ to stopwords
	stopwords.append("__USER__")
	stopwords.append("__NUM__")
	stopwords.append("__URL__")
	
	#Make a set of stopwords
	stopwords = set(stopwords)
	
	#print stopwords
	
	s = PorterStemmer()
	
	for w in word_list:
		if w not in stopwords :
			#Stemming
			
			x = s.stem(w)
			feature_word_list.append(x)
			
	return feature_word_list