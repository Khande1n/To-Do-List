to_do_list = []
while True:
	name = raw_input("What you want to do ")
	#print name
	if name != 'DONE':
		to_do_list.append(name)
		print to_do_list
	else:
		for item in to_do_list:
			print item
		exit()