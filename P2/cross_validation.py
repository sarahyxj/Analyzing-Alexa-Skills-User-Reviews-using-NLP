import numpy as np
import pandas as pd
import glob
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from sklearn.model_selection import KFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score



from text_preprocessing import clean_text,remove_emoji
from get_words import get_top20
from get_similarity import get_similarity



############################ MAIN PART ###########################
""" 获取原始数据 """
# specifying the path to excel files
path = "C:/Users/s/Desktop/Alexa/Data/Classification/v7"
 
# csv files in the path
file_list = glob.glob(path + "/*.xlsx")
 
# concatenate all DataFrames in the list into a single DataFrame, returns new DataFrame.
excl_list = []
 
for file in file_list:
    # excl_list.append(pd.read_excel(file,  usecols=['Text', 'category']))
    excl_list.append(pd.read_excel(file,  usecols=['Text', 'category'], nrows=100)) # get first 100 rows
excl_merged = pd.concat(excl_list, ignore_index=True)

 
# exports the 4 dataframe into 1 excel file
excl_merged.to_excel('combined.xlsx', index=False)

#loading the data
data = pd.read_excel (r'C:/Users/s/Desktop/Alexa/P2/combined.xlsx')
print('There are {} rows and {} columns in this report'.format(data.shape[0],data.shape[1]))

""" 对数据进行清理 """
data["Text"] = data["Text"].apply(clean_text).apply(remove_emoji)
data = data.sample(frac=1).reset_index(drop=True) #shuffle the data

# words_and_tags = nltk.pos_tag(data["Text"])

""" Cross Validation """
X = data["Text"].values
y = data["category"].values

# ten fold 
kf = KFold(n_splits = 10)
kf.get_n_splits(X)
precision_scores = [] 
recall_scores = []
f1_scores = []
iter_no = 1
top_num = 20

for i, (train_index, test_index) in enumerate(kf.split(X)):
    """Train"""
    # spliting the data into training and testing set
    X_train = X[train_index]
    Y_train = y[train_index]
    Y_train = Y_train.tolist()
    
    X_test = X[test_index]
    Y_test = y[test_index]
    Y_test = Y_test.tolist()
       
    df_train = pd.DataFrame({'Text':X_train,'category':Y_train})
    df_train["Text"] = df_train["Text"].map(lambda x: x + " ")   
    df_category0_train = df_train[df_train['category'] == 0]
    df_category1_train = df_train[df_train['category'] == 1] 
    df_category2_train = df_train[df_train['category'] == 2]
    df_category3_train = df_train[df_train['category'] == 3]
    
    # use the data to extract the features
    df_category0 = data[data['category'] == 0]
    df_category1 = data[data['category'] == 1] 
    df_category2 = data[data['category'] == 2]
    df_category3 = data[data['category'] == 3]
    
    most0 = get_top20(df_category=df_category0,num=top_num)
    most1 = get_top20(df_category=df_category1,num=top_num)
    most2 = get_top20(df_category=df_category2,num=top_num)
    most3 = get_top20(df_category=df_category3,num=top_num)
    
    top20_0 = [item[0] for item in most0]
    top20_1 = [item[0] for item in most1]
    top20_2 = [item[0] for item in most2]
    top20_3 = [item[0] for item in most3]
    
    
    print('C0:', top20_0)
    print('C1:', top20_1)
    print('C2:', top20_2)
    print('C3:', top20_3)
        
    merged_words = top20_0 + top20_1 + top20_2 + top20_3
    final_list = list(set(merged_words))
    
    features = final_list
            
    # calculate TFIDF using the training 
    text0 = list(df_category0_train["Text"].sum().split(" "))
    text1 = list(df_category1_train["Text"].sum().split(" "))
    text2 = list(df_category2_train["Text"].sum().split(" " ))
    text3 = list(df_category3_train["Text"].sum().split(" "))
    
    mylist = [text0, text1, text2, text3]

    df_train_t = pd.DataFrame({"texts": mylist})
    tfidf_vectorizer = TfidfVectorizer(ngram_range=[1, 1])
    tfidf_separate = tfidf_vectorizer.fit_transform(df_train_t["texts"].apply(lambda x: ','.join(x)))
    df_tfidf = pd.DataFrame(
          tfidf_separate.toarray(), columns=tfidf_vectorizer.get_feature_names_out(), index=df_train_t.index
      )
      
    # the features' tfidf 
    df_train_feature_vector = pd.DataFrame(df_tfidf,columns = features)
    
    """Test"""
    df_test = pd.DataFrame({'Text':X_test,'category':Y_test})    
    # category0_test = df_category0['Text']
    # category1_test = df_category1['Text']
    # category2_test = df_category2['Text']
    # category3_test = df_category3['Text']
    
    # text0_test = list(category0_test.sum().split(" "))
    # text1_test = list(category1_test.sum().split(" "))
    # text2_test = list(category2_test.sum().split(" " ))
    # text3_test = list(category3_test.sum().split(" "))
    # documents = [text0_test, text1_test, text2_test, text3_test]
    
    """Similarity"""
    df_test_predict = df_test
    y_predict = []
    for index,sentence in enumerate(df_test["Text"]):
        words = sentence.split(" ")
        # calculate the similarity between sentence and training document
        similarities = get_similarity(words,mylist,df_train_feature_vector,features)
        

        # print(similarities)
        # print(index)
        max_sim = max(similarities)
        # if(max_sim != 0):
        label = similarities.index(max_sim)
        y_predict.append(label)
        # else:
        #     ## 这里如是similarity果四个都是0
        #     df_test_predict.drop([index],inplace=True)
        #     # print("*********")
        #     # print(sentence)
            
    # df_test_predict['category'] = df_test_predict['category'].fillna(0)
 
        
    precision = precision_score(df_test_predict["category"], y_predict,average='macro')
    recall   =  recall_score(df_test_predict["category"], y_predict,average='macro')
    f1 = f1_score(df_test_predict["category"], y_predict,average='macro')
    precision_scores.append(precision)
    recall_scores.append(recall)
    f1_scores.append(f1)
   
    print("============= Cross-Validation-" + str(iter_no) + " =============")
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1:", f1)
    iter_no  = iter_no + 1
    # break
    

print("Precision Scores : ")
print(precision_scores)
print("Average Precision : " + str(np.average(precision_scores)))
print("Recall Scores : ")
print(recall_scores)
print("Average Recall : " + str(np.average(recall_scores)))
print("F1 Scores : ")
print(f1_scores)
print("Overall F1 Scores : {:.2f}".format(np.average(f1_scores)))




