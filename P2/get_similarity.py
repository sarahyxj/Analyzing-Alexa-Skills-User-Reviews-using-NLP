import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# function to calculate the cosine similarity between a sentence and a set of documents, 
# represented as a list of strings， using TF-IDF vectorization approach 
# to represent the sentence and documents as feature vectors.

def get_similarity(sentence,documents,df_train_feature_vector,features): 
 
    documents.insert(0,sentence) # include the sentence into the documents
    mylist_test = documents # mylist_test 是sentence和documents的集合list 
    
    # calculate tf-idf using TfidfVectorizer
    df_test_t= pd.DataFrame({"texts": mylist_test})
    tfidf_vectorizer_test = TfidfVectorizer(ngram_range=[1, 1])   
    tfidf_separate_test = tfidf_vectorizer_test.fit_transform(df_test_t["texts"].apply(lambda x: ','.join(x)))
    df_tfidf_test = pd.DataFrame(tfidf_separate_test.toarray(), 
                                 columns=tfidf_vectorizer_test.get_feature_names(), 
                                 index=df_test_t.index)

    # 
    df_sentence_feature_vector = pd.DataFrame(df_tfidf_test,columns = features).iloc[0]
    
    # calculates the cosine similarity between the sentence and each document 
    # in df_train_feature_vector using cosine_similarity
    similarities = []   
    for index in range(0, len(df_train_feature_vector)):
        document1_feature_vector = df_train_feature_vector.iloc[index]      
        df_sentence_feature_vector = df_sentence_feature_vector.fillna(0)
        document1_feature_vector = document1_feature_vector.fillna(0)
        similarity_temp = cosine_similarity(np.transpose(df_sentence_feature_vector.values.reshape(-1,1)),np.transpose(document1_feature_vector.values.reshape(-1,1)))       
        similarities.append(similarity_temp[0][0])
    return similarities

