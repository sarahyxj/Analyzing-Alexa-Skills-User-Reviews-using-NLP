# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 08:19:50 2022

@author: s

Get the Keyword and feature set extraction

"""

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')

import pandas as pd
# import numpy as np
# import pickle as pk

import warnings
warnings.filterwarnings("ignore")

# from bs4 import BeautifulSoup
# import unicodedata
# import re

# from nltk.tokenize import word_tokenize
# from nltk.tokenize import sent_tokenize

from nltk.corpus import stopwords

# from nltk.corpus import wordnet
# from nltk import pos_tag
# from nltk import ne_chunk

# from nltk.stem.porter import PorterStemmer
# from nltk.stem.wordnet import WordNetLemmatizer

# from nltk.probability import FreqDist
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud

from sklearn.feature_extraction.text import TfidfVectorizer


#https://michael-fuchs-python.netlify.app/2021/05/22/nlp-text-pre-processing-i-text-cleaning/#import-the-libraries-and-the-data
data = pd.read_excel (r'data/bug report.xlsx')


#read text from bug report
df = data['Text']
df.head()


#tokenization
df = nltk.word_tokenize(data['Text'][0])


#remove stop words with NTLK "https://www.geeksforgeeks.org/removing-stop-words-nltk-python/"  
stop_words = set(stopwords.words('english'))
  
filtered_sentence = [w for w in df if not w.lower() in stop_words]
  
filtered_sentence = []
  
for w in df:
    if w not in stop_words:
        filtered_sentence.append(w)
        
        
#remove duplicate word "https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/"

#res = [*set(filtered_sentence)]
#print(res)

#print(filtered_sentence)

#Weighting terms by the number of times they appear in a document
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(filtered_sentence)

print(vectorizer.get_feature_names())
print(X.toarray())


