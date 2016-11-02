import re


def to_all_words(tweet):
	
	#Split all words on delimiters ",:;-space"
	words =  re.split('[,;:\-\s]\s*',tweet)
	
	#print words
	
	#all tweet subjective and infoemative words
	word_list = []
	
	for w in words:
		
		#See if w starts with non alphabetic character
		val = re.match('^[^\w]+[\S]?$',w)
		if val != None :
			continue
			
		#Replace any character with blank i.e. replace any non-character
		w = re.sub('[^\w]+',"",w)
		
		#check if word contains only characters
		if w.isalpha() :
			word_list.append(w)
		
	#print word_list
	
	return word_list
	
	
	

	
	
			
		
	