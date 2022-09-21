from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

engine = create_engine('sqlite:///dictionary.sqlite')

Base = automap_base()
Base.prepare(autoload_with=engine)

Word = Base.classes.word
Definition = Base.classes.definition
Typemap = Base.classes.typemap

def get_definitions(word, limit=None, type='all'):
    with Session(engine) as s:
        try:
            w = s.query(Word).filter(Word.word==word).first()
            ds = s.query(Definition).filter_by(word_id=w.id).all()
        except:
            return f"Cound not find '{word}' in dictionary."
        list = []
        for d in ds:
            ts = s.query(Typemap).filter_by(base=d.type).all()
            dict = {}
            dict['types'] = []   
            for t in ts:
                dict['types'].append(t.converted)
            if not type == 'all':
                if type in dict['types']:
                    dict['base_types'] = d.type
                    dict['definition'] = d.definition
                    list.append(dict)
                else:
                    continue
            else:
                dict['base_types'] = d.type
                dict['definition'] = d.definition
                list.append(dict)
        dict = {}
        dict['word'] = w.word
        dict['definitions'] = list
    return dict

def get_words(query):
    with Session(engine) as s:
        ws = s.query(Word).filter(Word.word.like(f'{query}%')).all()
        dict = {}
        dict['words'] = []
        for w in ws:
            dict['words'].append(w.word)
    return dict