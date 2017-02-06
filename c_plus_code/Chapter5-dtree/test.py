file_object = open('./test.txt', 'rb')	
list_of_all_the_lines = file_object.readlines( )
s = set()

for line in list_of_all_the_lines:
	onion = line[64:]
	s.add(onion)
for ss in s:
	print ss