def sortcat(range_random, *argv):
	final_lst = ""
	lst = []
	for x in argv:
		lst.append(len(x))
	for x in range(range_random):
		mx = max(final_lst)
		for y in range(len(final_lst)):
			if mx == final_lst[y]:
				final_lst = final_lst+argv[y]
				final_lst[y] = 0
	return final_lst

print sortcat(1, 'abc', 'bc')
print sortcat(2, 'bc', 'c', 'abc')