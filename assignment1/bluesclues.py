state = {}
with open("states.txt", "r") as f: 
	for line in f: 
		dictionary = line.rstrip("\n").split(",")
		key, val = dictionary[1], dictionary[0] 
		state[key] = val


def bluesclues(str): 
	state_answer = state[key]
	print state_answer

