# poemgen
A project to generate a random poem.

Sources/APIs used:

	1) Syllable count reference:
		http://www.datamuse.com/api/
		
	2) Word list
		http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain

		(inspired by: https://stackoverflow.com/questions/18834636/random-word-generator-python)
		
	3) Grammar Check API
		https://www.grammarbot.io/quickstart


STEPS TO RUN LOCALLY:

(As docker image)

	# Clone repo and navigate to service directory 

	# Build image
	$ docker build -t "poemgen" .

	# Run image
	$ docker run -p 5000:5000 poemgen

	# Generate haiku at http://localhost:5000/haiku



(As local python app)

TO GENERATE HAIKU TO CONSOLE:

	Clone and navigate to root level of this repo.

	(RECOMMENDED TO MAKE VIRTUALENV FOR PROJECT...  see here: https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)

	$ cd service

	$ pip install -r requirements.py

	$ python test.py

TO RUN AS LOCAL WEBAPP:

	Clone and navigate to root level of this repo.

	(RECOMMENDED TO MAKE VIRTUALENV FOR PROJECT...  see here: https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)

	$ cd service

	$ pip install -r requirements.py

	$ python api.py

	Then, navigate to http://localhost:5000/haiku to see a randomly generated haiku!


TO RUN UI

	npm run build 
	npm start
