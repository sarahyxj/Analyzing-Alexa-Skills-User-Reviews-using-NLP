# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:53:56 2022

@author: s
"""

import nltk
import pandas as pd
import re
import sys
import string

from sklearn.feature_extraction.text import TfidfVectorizer

from collections import defaultdict
from collections import Counter

#https://michael-fuchs-python.netlify.app/2021/05/22/nlp-text-pre-processing-i-text-cleaning/#import-the-libraries-and-the-data
#download data
data = pd.read_excel (r'data/bug report.xlsx')

print('There are {} rows and {} columns in bug report'.format(data.shape[0],data.shape[1]))


#read text from bug report
df = data['Text']
df.head()


#Reference : https://gist.github.com/slowkow/7a7f61f495e3dbb7e3d767f97bd7304b
def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

remove_emoji("Omg another Earthquake 😔😔")

df['text']=df['text'].apply(lambda x: remove_emoji(x))

#Removing punctuations
def remove_punct(text):
    table=str.maketrans('','',string.punctuation)
    return text.translate(table)

example="I am a #king"

print(remove_punct(example))

df['text']=df['text'].apply(lambda x : remove_punct(x))

#tokenization
df = nltk.word_tokenize(data['Text'][0])

# def remove_punct(text):
#     table= str.maketrans('','',string.punctuation)
#     return text.translate(table)

# print(remove_punct(df))

# len(df)

# df = df[:10]

# print(df)

# plt.figure(figsize=(12,8))
# word_cloud = WordCloud(
#                           background_color='black',
#                           max_font_size = 80
#                          ).generate(" ".join(df[:10]))
# plt.imshow(word_cloud)
# plt.axis('off')
# plt.show()