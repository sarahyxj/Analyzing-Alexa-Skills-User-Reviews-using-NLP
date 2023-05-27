import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from P2.text_preprocessing import clean_text,remove_emoji
from nltk.corpus import stopwords
from collections import  Counter
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud

# df = pd.read_excel (r'../Data/Classification/V7/bug report.xlsx')
# df = df.head(100)

df = pd.read_excel('../P3/classified_data_all.xlsx', header=0, index_col=None)
# df = df[df['category_new'] == 1]
df = df[df['category_new'] == 2].squeeze(axis=1)

df.loc[:, 'Text_new'] = df['Text'].apply(clean_text).apply(remove_emoji)


# Print the number of rows and columns in the dataframe
print('There are {} rows and {} columns in this report'.format(df.shape[0],df.shape[1]))

# Combine all text data into one string
text = ' '.join(df['Text_new'].tolist())


print("***************Top 20 words *******************")
# visualize top20 words
def word_freq_dict(text):
    # Convert text into word list
    wordList = text.split()
    # Generate word freq dictionary
    wordFreqDict = {word: wordList.count(word) for word in wordList}
    return wordFreqDict

stop = set(stopwords.words('english'))
split_it = text.split()
plt.figure(figsize=(16,5))  
counter = Counter(split_it) 
most=counter.most_common()

x=[]
y=[]
for word,count in most[:20]:
    if (word not in stop) :
        x.append(word)
        y.append(count)

plt.title("Top 20 most common words in user's review - Feature Request")
sns.barplot(x=y,y=x,)
# sns.barplot(x=y,y=x,palette='Blues_d')
print(counter.most_common(20))

print("***************Top 20 bigram words *******************")

# visualize top20 bigram words 
def get_top_alexa_bigrams(corpus, n=None):
    vec = CountVectorizer(ngram_range=(2, 2)).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]

plt.figure(figsize=(10,5))
plt.title("Top 20 most common bigrams in user's review - Feature Request")
top_alexa_bigrams=get_top_alexa_bigrams(df['Text_new'])[:20]
x,y=map(list,zip(*top_alexa_bigrams))
sns.barplot(x=y,y=x)
plt.show()

print(top_alexa_bigrams)
print("**********************************")

# Create a new column called "key" and set it to False
df['key'] = False

# Loop through each row in the dataframe
for index, row in df.iterrows():
    for bigram in top_alexa_bigrams:
        if bigram[0] in row['Text_new']:
            df.at[index, 'key'] = True

df.to_excel('feature_key.xlsx', index=False)   

"result-46753 -92% ask for more features"    
"need to let Alexa to ask the celebrity," 
"a few certain things and had very limited responses" 
   
            
# Create Wordcloud1
text = " ".join(i for i in df.Text_new)
wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# Create Wordcloud2
wordcloud = WordCloud(max_font_size=50,
                      max_words=100,
                      background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

wordcloud.to_file("wordcloud_C2.png")