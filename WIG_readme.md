# WIG - Readme

Weighted Information Gain (WIG) is a predictor for analyzing the score distribution of a set of results, which is used to determine query difficulty. WIG measures the separation between the mean retrieval score of the top-ranked documents and that of the entire corpus. A retrieval is deemed effective when there is a higher similarity between the top-ranked documents and the query, with respect to the similarity between the query and a non-relevant document, the corpus.

In addition, the WIG method was originally entailed for the MRF retrieval framework, allowing term-dependences to be considered into the score. However, if term-dependencies are disregarded, the query likelihood model is used, and with this implementation, WIG is considered to be an effective post retrieval method.  

WIG is calculated as follows:

With a query q, corpus D, list of top-ranked documents Dq , the set of top-ranked documents k, and D<sub>q</sub><sup>k</sup>. 

![Wig Formula](/images/wig_formula.png)
 
&#955; (t) represents the relative weight of the term t and is inversely related to the square root of the number of query terms. When all the query terms are keywords, it is simplified to &#955;(t)=\frac{1}{\sqrt{\left|q\right|}}.
