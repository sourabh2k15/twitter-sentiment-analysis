
def to_feature_vector(feature_words,feature_list):
	
	words = set(feature_words)
	#A Dictionary for feature_vector
	feature_vector = {}
	
	
	for w in feature_list :
		feature_vector[w] = (w in feature_words)
	
	return feature_vector
	
	



