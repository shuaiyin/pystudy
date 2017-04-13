while 1:
	n = raw_input()
	n_list = list(str(n))
	print n_list
	for i in range(len(n_list)):
		if n_list[i] > "1":
			n_list[i] = "1"
			if i + 1 < len(n_list):
				n_list[i+1] = "9"
	print int("".join(n_list),2)