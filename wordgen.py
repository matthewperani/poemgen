import requests, random

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)

# makes list of all words
WORDS = response.content.splitlines()

listSize = len(WORDS)

randIndex = random.randrange(0, listSize)

randWordRaw = WORDS[randIndex]

randWord = randWordRaw.decode("utf-8")

print(randWord)










