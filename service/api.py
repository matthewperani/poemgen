from flask import Flask
import os
import wordgen

app = Flask(__name__)

@app.route('/')
def home_page():
	return 'Welcome to poemgen!  Try hitting /haiku endpoint'
	
@app.route('/haiku')
def haiku_page():
	return wordgen.haiku_gen()
	
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
