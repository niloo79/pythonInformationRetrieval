# Python Information Retrieval

This project contains two python based post retrieval query performance predictors

-  WIG - Weighted Information Gain:
   - WIG Measures the separation between the mean retrieval score of the top-ranked documents and that of the entire corpus. A retrieval is deemed effective when there is a higher similarity between the top-ranked documents and the query, with respect to the similarity between the query and a non-relevant document, the corpus.
    
- Clarity:
  - The Clarity predictor measures the coherence between the list of retrieved documents in relation to the corpus. Coherence refers to the extent to which the top-ranked documents share the same vocabulary. 


### For more information on WIG and Clarity, please review the WIG and Clarity readme files. 




# Getting Started

In this example, the collection used to calculate the query performance scores is the Robust-04 data set.

Assuming you have extracted all files and queries from the data set, you can create an index to read all terms in the corpus. If needed, remove all stop-workds. 

For more information on indexing, please refer to the whoosh documentation found here: https://whoosh.readthedocs.io/en/latest/intro.html

## Creating Required Dictionaries 

For calculating the Clarity and WIG score multiple dictionaries are needed

### Dictionary 1
- **Key**: query number 
- **Elements**: Stemmed query terms that have stop-words removed. 

### Dictionary 2 
- **Keys**: Query numbers
- **Elements**: Corresponding top-ranked documents

### Final Nested Dictionary

- **Primary Keys**: Query numbers 
- **Primary Elements**: 
  - **Secondary Keys**: Corresponding top-ranked documents
  - **Secondary Elements**: 
    - **Tertiary Keys**: Unique terms found in the document 
    - **Tertiary Elements**: Term frequency



## Clarity Calculation (clarity-robust.py)

2 terms are needed in this calculation: Pr(t|D<sub>q</sub>) and Pr(t|D)

### Pr(t|D<sub>q</sub>) Calculation

- For each query number in your final dictionary, use the corresponding top ranked documents to access the unique terms and term frequencies.
   
- Using these factors, you can calculate the Pr(t|d), as seen in the equation in the Clarity readme file.

- For each query in Dictionary 1, if the query number is equal to the query number in the final dictionary, look into the corresponding query terms and calculate the Pr(q|d).

- With the Pr(t|d) and the Pr(q|d), you can calculate Pr(t|D<sub>q</sub>).

### Pr(t|D) Calculation

- For each term in the corpus, calculate the term frequncy 
- Divide the term frequency by the total size of the corpus
  

The final step is to calculate the clarity score using Pr(t|D<sub>q</sub>) and Pr(t|D).



## WIG Calculation (WIG.py)

