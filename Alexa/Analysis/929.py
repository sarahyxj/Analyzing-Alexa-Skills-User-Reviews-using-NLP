# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:23:55 2022
calculate the weighting terms

https://www.kaggle.com/code/edchen/tf-idf/notebook

@author: s
"""

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

corpus = [
 'the brown fox jumped over the brown dog',
 'the quick brown fox',
 'the brown brown dog',
 'the fox ate the dog'
]

X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
print(X.toarray())

