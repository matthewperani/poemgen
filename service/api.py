from flask import Flask
from flask_cors import CORS
import os
import wordgen

app = Flask(__name__)
CORS(app)

@app.route('/')
def home_page():
	return 'Welcome to poemgen!  Try hitting /haiku endpoint'
	
@app.route('/word')
def word_page():
	return wordgen.generate_word()

@app.route('/haiku')
def haiku_page():
	return wordgen.haiku_gen()
	
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
