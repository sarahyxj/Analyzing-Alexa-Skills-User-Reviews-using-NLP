""" sentiment match testing_ check for C0"""

import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    sentiment = sia.polarity_scores(text)
    return sentiment

df = pd.read_excel('../P3/classified_data_all.xlsx')

df = df[df['category_new'] == 0].squeeze(axis=1)

df['sentiment'] = df['Text'].apply(lambda x: get_sentiment(str(x)))

def check_sentiment(row):
    if row['Rating Star_new'] > 3 and row['sentiment']['compound'] < 0:
        return 'Unmatch-Negative'
    elif row['Rating Star_new'] < 3 and row['sentiment']['compound'] > 0:
        return 'Unmatch-Positive'
    else:
        return 'Match'

df['sentiment_match'] = df.apply(check_sentiment, axis=1)


# Get the count of each unique value in the "sentiment_match" column
counts = df['sentiment_match'].value_counts()

# Calculate the percentage of negative and positive sentiments
total = len(df)
negative_pct = counts['Unmatch-Negative'] / total * 100
positive_pct = counts['Unmatch-Positive'] / total * 100

print(f"Negative sentiment percentage: {negative_pct:.2f}%")
print(f"Positive sentiment percentage: {positive_pct:.2f}%")

df.to_excel('sentiment-match.xlsx', index=False)

# Negative sentiment percentage: 1.81%
# Positive sentiment percentage: 10.83%


# Get the count of each unique value in the "sentiment_match" column
counts = df['sentiment_match'].value_counts()

# Create a list of labels for the bar chart
labels = ['Match', 'Unmatch-Negative', 'Unmatch-Positive']



# Create a list of values for the bar chart
values = [counts['Match'], counts['Unmatch-Negative'], counts['Unmatch-Positive']]

# Calculate the total number of values
total = sum(values)

# Create a list of percentages for each value
percentages = [value / total * 100 for value in values]


# Create a bar chart with labels and values
bars = plt.bar(labels, values)

# Add a title for the bar chart
plt.title('Sentiment Matching Analysis')

# Add labels for the x-axis and y-axis
plt.xlabel('Sentiment Category')
plt.ylabel('No.of Reviews')

# Loop through each bar and add a percentage annotation above it using plt.annotate()
for i, bar in enumerate(bars):
    # Get the height and width of the bar
    height = bar.get_height()
    width = bar.get_width()
    
    # Calculate the x and y coordinates for the annotation
    x = bar.get_x() + width / 2 # center the annotation horizontally
    y = height + 0.01 # add some margin above the bar
    
    # Format the percentage with two decimal places
    pct = f'{percentages[i]:.2f}%'
    
    # Add the annotation with some properties
    plt.annotate(pct, (x, y), ha='center', va='bottom', color='black', fontsize=12)

# # Add percentage labels to each bar using plt.bar_label()
# plt.bar_label(bars, labels=[f'{p:.2f}%' for p in percentages], label_type='center')

# Show the bar chart
plt.show()


