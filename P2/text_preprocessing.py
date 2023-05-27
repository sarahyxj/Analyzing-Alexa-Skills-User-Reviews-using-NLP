import string
from nltk.stem import PorterStemmer
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import re
from nltk.stem.wordnet import WordNetLemmatizer
# nltk.download('wordnet')



# function to prepocess the text
def clean_text(text):
    stop = set(stopwords.words('english'))
    punc = set(string.punctuation)
    lemma = WordNetLemmatizer()
    stemmer = PorterStemmer()    
    keywords = ['alexa','voice','dog','fart','nan','skill','app','bark','amazon',
                  'kid','people','barking', 'echo','sam','samuel','jackson','jeopardy',
                  'time', 'want', 'know', 'thing','one','l','it’', "it's", 'definit', 'every',
                  'it’', 'Jurassic', 'go', 'sleep',
                  'much','better','wish', 'day','think', 'make', 'everything',
                  'thing', 'sound','answer','even', 'try','say','ask',
                  'really',"i'm",'baby','xbox','roomba',"can't",'ad','like',
                  'lol','old','side','got','get','also','definite',
                  'see', 'woof','work','play']
    
    # delete the blanket 
    text = str(text).strip()
    # Convert the text into lowercase
    text = text.lower()
    # Remove numbers
    text = re.sub(r'\d+', '', text)     
    # Split into list
    wordList = text.split()
    wordList = [str.strip(word) for word in wordList]
    # Remove punctuation
    wordList = ["".join(x for x in word if (x=="'")|(x not in punc)) for word in wordList]
    # Remove stopwords
    wordList = [word for word in wordList if word not in stop]
    # Lemmatisation
    wordList = [lemma.lemmatize(word) for word in wordList]
    # Remove other keywords
    wordList = [word for word in wordList if word not in keywords]
    # Stemming 
    wordList = [stemmer.stem(word) for word in wordList]
    
    return " ".join(wordList)


# function to remove emoji
def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emotions
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)    
    return emoji_pattern.sub(r'', str(string))

# print(remove_emoji("game is on 🔥🔥"))