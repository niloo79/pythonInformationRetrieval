import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from whoosh.lang.porter import stem
stop_words = set(stopwords.words('english'))

import string
#from string import strip
import re


def term_frequency ( searcher, term, qp):
    qt = stem(term.lower())
    q = qp.parse(qt)

    try:
        tf = searcher.term_info('content', qt)._weight
        results = searcher.search(q)
        #print("term:", term, "TF", tf)
        return tf

    except:
        pass
        return 0


def term_modifications (file):
    final_terms=[]
    with open(file, 'r') as f:
        content = f.read()
        text_for_file = str.split(content)
        text_without_stop = [i for i in text_for_file if i.lower() not in stop_words]
        for term in text_without_stop:
            h = stem(term.lower())
            # print (h)
            final_terms.append(h)
    return final_terms


def remove_punctuation (file):
    with open(file, 'r') as f:
        content = f.read()
        text_for_file = str.split(content)
        new_text = [re.sub('[!#?,.:";]', '', word) for word in text_for_file]
    return new_text



def analyzer(file):
    review=open(file,'r')
    review=review.read()
    tokens=[e.lower() for e in map(str.strip, re.split("(\W+)", review)) if len(e) > 0 and not re.match("\W",e)]

    print (tokens)



#index is ix
def Pr_qi (term, doc, lam, N, searcher, qp, words):
    # if the term is in the doc and all the words, or if its only in the doc
    if term in doc:
        Pr_qi = lam * (doc[term] / (len(doc))) + ((1 - lam)) * ((term_frequency(searcher, term, qp)) / N)
        return Pr_qi
    #if term not in doc and only in the words
    elif term in words:
        Pr_qi= (1-lam) * (term_frequency(searcher, term, qp) / N)
        return Pr_qi
    # if the term is not in the doc and not in all the words
    else:
        Pr_qi=1
        return Pr_qi


