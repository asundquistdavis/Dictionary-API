import requests
import pandas as pd

ALPHA = 'abcdefghijklmnopqrstuvwxyz'
definitions_path = 'http://localhost:5000/definitions?word='
words_path = 'http://localhost:5000/words?query='

def get_words(q, l='any'):
    if l == 'any':
        return requests.get(str(words_path+q)).json()['words']
    else:
        list = []
        ws = requests.get(str(words_path+q)).json()['words']
        for w in ws:
            if len(w) == l:
                list.append(w)
        return list

def get_distribution(q):
    list = []
    for l in range(1,21):
        list.append(len(get_words(q, l)))
    return list

def build_distributions_df(charset):
    df = pd.DataFrame()
    for q in charset:
        df[q] = get_distribution(q)
    return df