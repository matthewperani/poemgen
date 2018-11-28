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
	






