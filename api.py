from flask import Flask, request as r
from search import get_definitions,get_words

api = Flask(__name__)

@api.route('/')
def index():
    return 'This is the home page for the dictionary API. Use /"word" to search for a word!'

@api.route('/definitions')
def definitions():
    word = r.args.get('word')
    type = r.args.get('type', default='all')
    return get_definitions(word, type=type)

@api.route('/words')
def words():
    query = r.args.get('query')
    return get_words(query)

if __name__ == '__main__':
    api.run(debug=True)