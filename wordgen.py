import requests, random, json


def generate_word():
	"""Generate a single random word."""
	word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
	
	response = requests.get(word_site)
	
	# makes list of all words
	WORDS = response.content.splitlines()
	
	listSize = len(WORDS)
	
	randIndex = random.randrange(0, listSize)
	
	randWordRaw = WORDS[randIndex]
	
	randWord = randWordRaw.decode("utf-8")
	
	return randWord


def syllable_count(word):
	"""Return number of syllables in input word."""
	data_site = "https://api.datamuse.com/words?max=1&md=ps&sp=" + word
	
	resp = requests.get(data_site)
	
	word_data = json.loads(resp.content)	
	word_dict = word_data[0]
	num_syllables = word_dict['numSyllables']
	
	return num_syllables
	
def haiku_gen():
	"""Generates a haiku using other module lins from wordgen."""
	
	line_1_count = 5
	line_1 = ""
	
	while line_1_count > 0:
		word = generate_word()
		syl_count = syllable_count(word)
		if line_1_count >= syl_count:
			line_1 += " " + word
			line_1_count = line_1_count - syl_count
	
	line_2_count = 7
	line_2 = ""
	
	while line_2_count > 0:
		word = generate_word()
		syl_count = syllable_count(word)
		if line_2_count >= syl_count:
			line_2 += " " + word
			line_2_count = line_2_count - syl_count
	
	
	line_3_count = 5
	line_3 = ""
	
	while line_3_count > 0:
		word = generate_word()
		syl_count = syllable_count(word)
		if line_3_count >= syl_count:
			line_3 += " " + word
			line_3_count = line_3_count - syl_count

	print(line_1)
	print(line_2)
	print(line_3)

