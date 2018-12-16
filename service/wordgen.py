import requests, random, json, urllib.parse, time

print("hello from poemgen")

def generate_word():
	"""Generate a single random word."""

	start = time.time()

	word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
	
	response = requests.get(word_site)
	
	# makes list of all words
	WORDS = response.content.splitlines()
	listSize = len(WORDS)
	randIndex = random.randrange(0, listSize)
	randWordRaw = WORDS[randIndex]
	randWord = randWordRaw.decode("utf-8")

	end = time.time()

	# Performance info
	print("generate_word result: " + randWord)
	print("generate_word time taken (seconds): " + str(end - start))
	
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
	line_2_count = 7
	line_2 = ""
	line_3_count = 5
	line_3 = ""
	words_generated = 0
	
	start = time.time()
	
	while line_1_count > 0 or line_2_count > 0 or line_3_count > 0:
		words_generated += 1
		word = generate_word()
		syl_count = syllable_count(word)
		if line_1_count >= syl_count:
			line_1 += " " + word
			line_1_count = line_1_count - syl_count
		elif line_2_count >= syl_count:
			line_2 += " " + word
			line_2_count = line_2_count - syl_count	
		elif line_3_count >= syl_count:
			line_3 += " " + word
			line_3_count = line_3_count - syl_count

	end = time.time()
	
	# Print generated haiku locally 
	print(line_1)
	print(line_2)
	print(line_3)
	
	# Performance info
	print("kaiku_gen number of words generated: " + str(words_generated))
	print("haiku_gen time taken (seconds): " + str(end - start))
	
	# Prepare for JSON output
	output = {}
	output['line_1'] = line_1
	output['line_2'] = line_2
	output['line_3'] = line_3
	output['haiku'] = line_1 + '\n' + line_2 + '\n' + line_3
	json_output = json.dumps(output)
	
	return json_output
	
def check_grammar(line):
	
	formatted_line = urllib.parse.quote_plus(line)
	"""Check the grammar of a string by making an external API call.  Returns true/false."""
	api_endpoint = "http://api.grammarbot.io/v2/check?api_key=9JMF2Y56&language=en&text=" + formatted_line
	
	resp = requests.get(api_endpoint)
	resp_content = json.loads(resp.content)
	
	errors = len(resp_content['matches'])

	if errors > 1:
		return False
	else:
		return True
	

