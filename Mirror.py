def mirror(string):
	index = len(string) - 1
	word = ""
	num = 0
	while num < len(string):
		letter = string[index]
		word = word + letter
		index = index - 1
		num = 1 + num
	mir = string + word
	print(mir)
	return(mir)
	
test = print

test(mirror("good") == "gooddoog")
test(mirror("Python") == "PythonnohtyP")
test(mirror("") == "")
test(mirror("a") == "aa")
