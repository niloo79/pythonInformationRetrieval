from whoosh.reading import IndexReader
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh.lang.porter import stem
import supportingFunctions
import math
import nltk
import os
import re
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


ix=open_dir("indexdir_robust04_full")
IndexReader()
#xx=IndexReader.all_terms('content')
p=ix.reader()
p2=ix.schema
print((ix.schema))
bytestrings = list(p.lexicon("content"))
fieldobj = ix.schema["content"]
words = [fieldobj.from_bytes(bs) for bs in p.lexicon("content")]


lam = 0.5
searcher=ix.searcher()
qp = QueryParser("content", schema=ix.schema)
N = searcher._doccount
K = 1000

# queries is a dictionary with the keys being the query numbers and the elements are the query words

queries = {}
queries_path = '/home/niloo/rb04-queries2'
with open(queries_path,'r') as q_file:

    for line in q_file:
        query = []
        line = line.replace(':', ' ')
        q = line.split()
        key = q[0] # key is the Q number
        #print(key)
        q_without_stop = [i for i in q if i.lower() not in stop_words]
        for term in q_without_stop:
            h = stem(term).lower()
            query.append(h)
        q_words= query[1:]
        queries [key] = q_words

# DQ is a dictionary with keys being the query numbers and elements are the corresponding top ranked documents
DQ={}
Dq_dir = '/home/niloo/run.robust04.bm25.topics.robust04.txt'

for key in queries:
    dq_names = []
    with open(Dq_dir, 'r') as dq:
        lines = dq.readlines()
        for line in lines:
            #print(line)
            if line.startswith(key):
                d= line.split()
                doc_name = d[2]
                #print(doc_name)
                dq_names.append(doc_name)
        # print(dq_names)
        # print(len(dq_names))
        dq.close()
        DQ[key]=  dq_names

file_dir = '/home/niloo/robust04_extracted_full'
all_file_names = os.listdir(file_dir)

# final dict has the query number as main keys. the corresponding files to that query as secondary keys ( top ranked docs) , and each unique
# word in that file with its corresponding term frequency

final_dict= {}
for Q_name in DQ.keys():
    final_dict[Q_name]={}

    for doc_name in DQ[Q_name]:
        for file in all_file_names:
            if doc_name == file:
                path_for_file = os.path.join('/home/niloo/robust04_extracted_full/', file)
                with open (path_for_file, 'r') as pff:
                    read_file = pff.read()
                    file_terms = [e.lower() for e in map(str.strip, re.split("(\W+)", read_file)) if
                              len(e) > 0 and not re.match("\W", e)]
                    tf_dict = {i: file_terms.count(i) for i in file_terms}
                    # print(Q_name, doc_name, file, tf_dict)
                    final_dict[Q_name][file]= tf_dict



#wig = 0
for Q_name in final_dict.keys():
    K = len(final_dict[Q_name])

    for doc_name in final_dict[Q_name].keys():
        for word_in_doc, tf in final_dict[Q_name][doc_name].items():
            Pr_td = lam * (tf / (len(final_dict[Q_name][doc_name]))) + ((1 - lam)) * (
                        (supportingFunctions.term_frequency(searcher, word_in_doc, qp)) / N)
            Pr_tD = supportingFunctions.term_frequency(searcher, word_in_doc, qp)/ N
            if Pr_tD !=0 :

                for q_term, value in queries.items():
                    output = (1/(len(value)) * math.log(Pr_td/Pr_tD))

    wig = output/K
    print (wig)

print("done")













