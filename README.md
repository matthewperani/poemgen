# poemgen
A project to generate a random poem.

In progress

$$$$$$$$$$$$$$$$$$$$

Sources/APIs used:

1) Syllable count reference:
	http://www.datamuse.com/api/
	
2) Word list
	http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain

	(inspired by: https://stackoverflow.com/questions/18834636/random-word-generator-python)
	
$$$$$$$$$$$$$$$$$$$$$

STEPS TO RUN LOCALLY:

TO GENERATE HAIKU TO CONSOLE
	Clone and navigate to root level of this repo.

	$ pip install requests

	$ python test.py

TO RUN AS LOCAL WEBAPP:

	Clone and navigate to root level of this repo.

	$ pip install requests

	$ pip install flask

	$ python api.py

	Then, navigate to http://localhost:5000/haiku to see a randomly generated haiku!



