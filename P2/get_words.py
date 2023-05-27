from collections import  Counter

# function to get the No. of words
def get_top20(df_category,num):
    ## process category
    category = df_category['Text']
    listToStr = ' '.join([str(elem) for elem in category])
    split_it = listToStr.split()
    counter = Counter(split_it) 
    most=counter.most_common()   
    return most[:num]

