import pandas as pd
from P2.text_preprocessing import clean_text,remove_emoji

# Create a sample dataframe
df = pd.read_excel('../P3/result.xlsx')
print('There are {} rows and {} columns in this report'.format(df.shape[0],df.shape[1]))

df['Word Count'] = df['Text'].str.split().str.len()

# find the lowest and largest word count number
lowest_word_count = df['Word Count'].min()
largest_word_count = df['Word Count'].max()
# get the average word count
average_word_count = df['Word Count'].mean()

print(f'Lowest word count: {lowest_word_count}')
print(f'Largest word count: {largest_word_count}')
print(f'Average word count: {average_word_count}')


# filter out the word count less than 5 and larger than 500
df = df[(df['Word Count'] >= 5) & (df['Word Count'] <= 1000)]

print(df.shape)

# preprocess the Text column
df["Text_new"] = df["Text"].apply(clean_text)
df["Text_new"] = df["Text_new"].apply(remove_emoji)

# Define the keywords to filter by
C0 = ['love', 'funny', 'worth', 'good', 'great', 'worst', 'annoy', 'cool']
C1 = ['bug','enable', 'fix', 'problem', 'wrong', 'charge', 'update','scam','spam']
C2 = ['could', 'would', 'improve', 'replace', 'need', 'change', 'set']
C3 = ['understand', 'use', 'play', 'response', 'question', 'read']

# Filter the dataframe by keywords
# df['category1'] = ''
# df.loc[df['Text_new'].str.contains('|'.join(C0)), 'category1'] = 0
# df.loc[df['Text_new'].str.contains('|'.join(C3)), 'category1'] = 3
# df.loc[df['Text_new'].str.contains('|'.join(C1)), 'category1'] = 1
# df.loc[df['Text_new'].str.contains('|'.join(C2)), 'category1'] = 2


# Define the function to classify text
def classify_text(text):
    # Initialize the category to 4
    category = 4
    
    # Check if text contains words in C0
    for word in C0:
        if word in text:
            category = 0
            break
    
    # Check if text contains words in C1
    if category == 4:
        for word in C1:
            if word in text:
                category = 1
                break
    
    # Check if text contains words in C2
    if category == 4:
        for word in C2:
            if word in text:
                category = 2
                break
    
    # Check if text contains words in C3
    if category == 4:
        for word in C3:
            if word in text:
                category = 3
                break
    
    # Return the category
    return category

# Apply the function to the dataframe
df['category_new'] = df['Text_new'].apply(classify_text)

# Count the numbers for each category
counts = df['category_new'].value_counts()

# Print the counts
print(counts)

# Get the percentages for each category
percentages = counts / counts.sum() * 100

percentages_formatted = percentages.apply(lambda x: '{:.2f}%'.format(x))

# Print the percentages
print(percentages_formatted)



df['Rating Star_new'] = df['Rating Star'].str.extract(r'(\d+\.\d+)')
# float to int
df['Rating Star_new'] = df['Rating Star_new'].fillna(0).astype(float).astype(int)

df['Reviewed Time'] = pd.to_datetime(df['Location & Time'], format='Reviewed in the United States on %B %d, %Y').dt.strftime('%m/%d/%Y')

# Convert the "Reviewed Time" column to datetime format
df['Reviewed Time'] = pd.to_datetime(df['Reviewed Time'], format='%m/%d/%Y')

# Extract only the date from the datetime column and create a new column named "reviewed data"
df['Reviewed Time'] = df['Reviewed Time'].dt.date

# Write the filtered dataframe to a new Excel file
df.to_excel('../P3/classified_data_all.xlsx') 
