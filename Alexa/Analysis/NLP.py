# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 16:48:00 2022

@author: s
"""
import nltk

text = nltk.word_tokenize("And now for something completely different")
nltk.pos_tag(text)

text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")

