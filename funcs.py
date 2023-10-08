# Put your functions in here.
# Feel free to run your design past me before beginning to implement.

def structure_puzzle(puzzle): #done and eyetested
	"""
	puzzle:(string) is the whole puzzle as a single string.
	returns a list of individial string with 10 characters, 
	i.e. a 2D list, where each row is a string.
	"""
	structured=[]
	
	for i in range(10):#[0123456789]
		from_ = i*10
		to = i*10+10
		structured.append(puzzle[from_:to])
	return structured	

 

def find_up(puzzle, words): #good
	"""
	puzzle: (list of strings) gets the puzzle from structure_puzzle()
	words: (list of words) gets words from structure_words()
	looks for the words in the UP direction, 
	if found return the word(s) found and their indicecs/row&col nums 
	
	STRATEGRY:
	put the characters with the same col num from the puzzle in a list of individual strings,
	then try match letter by letter for each of the words in words. 
	if the indeices of a sequencec of letters are neigboring numbers, 
	then a word is found. 
	"""

	col_list=[]
	for i in range(len(puzzle)):
		for j in range(len(puzzle)):
			col_list.append(puzzle[j][i])
	r_puzzle =''.join(col_list)
	r_struc_puzz = structure_puzzle(''.join(reversed(r_puzzle)))

	words_found=[]
	for i in range(len(words)):
		for j in range(len(r_struc_puzz)):
			find=r_struc_puzz[j].find(words[i])
			if find!=-1:
				words_found.append(words[i])
				words_found.append(-find+9)#row
				words_found.append(-j+9)#col

	return words_found

def find_down(puzzle, words): #good
	"""
	puzzle: (list of strings) gets the puzzle from structure_puzzle()
	words: (list of words) gets words from structure_words()
	looks for the words in the DOWN direction, 
	if found return the word(s) found and their indicecs/row&col nums 

	STRATEGRY:
	same stragetry as find_up(), but in the oppposite direction
	"""
	col_list=[]
	for i in range(len(puzzle)):
		for j in range(len(puzzle)):
			col_list.append(puzzle[j][i])
	struc_puzz=structure_puzzle(''.join(col_list))
	
	words_found=[]
	for i in range(len(words)):
		for j in range(len(struc_puzz)):
			find=struc_puzz[j].find(words[i])
			if find!=-1:
				words_found.append(words[i])
				words_found.append(find)#row
				words_found.append(j)#col

	return words_found

def find_forward(puzzle, words): #good
	"""
	puzzle: (list of strings) gets the puzzle from structure_puzzle()
	words: (list of words) gets words from structure_words()
	looks for the words in the FORWARD direction, 
	if found return the word(s) found and their indicecs/row&col nums in a list['word', row, col....]
	
	STRATEGRY:
	take each row of the puzzle and get the indeice of letters in a word,
	if the indices are negiboring numbers, then a word is found.
	"""
	words_found = [] #[word, row, col, word, row, col....]
	
	for i in range(len(words)):
		for j in range(len(puzzle)):
			find=puzzle[j].find(words[i])
			if find != -1:
				words_found.append(words[i])
				words_found.append(j)#row
				words_found.append(find) #col

	return words_found


def find_backward(puzzle, words): #Good, but MUST PASS UNSTRCTUED PUZZLE
	"""
	puzzle: (strings) gets the UNSTRUCTRED puzzle as a single string 
	words: (list of words) gets words from structure_words()
	looks for the words in the DONWWARD direction, 
	if found return the word(s) found and their indicecs/row&col nums 
	

	STRATEGRY:
	same stragetry as find_forward(), but in the oppposite direction
	"""
	r_puzzle = ''.join(reversed(puzzle))
	#print(puzzle, "\n rever:",r_puzzle)
	r_str_puzzle = structure_puzzle(r_puzzle)
	
	words_found = [] #[word, row, col, word, row, col....] col num is the place of the first letter of the word
	
	for i in range(len(words)):
		for j in range(len(r_str_puzzle)):
			find=r_str_puzzle[j].find(words[i])
			if find != -1:
				words_found.append(words[i])
				words_found.append(-j+9) #row
				words_found.append(-find+9) #col
	return words_found

def find_diagonal_dr(puzzle, word): 
	"""
	puzzle: (list of strings) gets the puzzle from structure_puzzle()
	word: (a singel word) gets word from structure_words()
	looks for the words in the DIAGONAL and RIGHT direction, 
	if found return the word found and their indicecs/row&col nums 
	"""
	word_i = 0

	for row in range(len(puzzle)):
		for col in range(len(puzzle)):
			word_i=0
			while row+word_i<=9 and col+word_i<=9 and word[word_i]==puzzle[row+word_i][col+word_i]:
				word_i+=1
				
				if word_i>=len(word):
					return (word, row, col)
	return None

# def structure_words(words): #done and eyetested. is this even nececssary?i could add it to strugture_puzzle and return a list of lists or a tuple
# 	"""
# 	words: (list) a list string of words separeted by space
# 	rerurns a list of indivial strings with each word in words
# 	"""
# 	return words.split()