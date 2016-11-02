def data_list(fp):
	
	data_list = []
	
	#line = fp.readline()
	
	for line in fp :
		row = []
		row.append(line[1])
		row.append(line[0])
		data_list.append(row)
		#line = fp.readline()
		
	return data_list
	