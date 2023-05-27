import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from P2.text_preprocessing import clean_text,remove_emoji


"This test is to extract the 'scam' from the C1" 

df = pd.read_excel('../P3/classified_data_all.xlsx', header=0, index_col=None)


# df.loc[:, 'Text_new'] = df['Text'].apply(clean_text).apply(remove_emoji)

# df['children'] = df['Text_new'].str.contains('kid|child') & df['Text_new'].str.contains('enable')
df['children'] = df['Text'].str.contains('enable by')

child_df = df[df['children'] == True]

print(child_df)

child_df.to_excel('child_report.xlsx', index=False)


# df = pd.read_excel('../P5_C1/child_report.xlsx', header=0, index_col=None)

# df = df.dropna(subset=['Skill No'])


# count = df['Skill No'].value_counts().head(50).rename_axis('Skill No').reset_index(name='counts')

# print(count.head(10))
# count.plot.scatter(x='Skill No', y='counts')


# # # 添加标签和标题
# plt.ylabel("No. of skill's review")
# plt.title('Potential Scams from User Reviews')

# plt.tight_layout()
# # fig, ax = plt.subplots()
# # ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

# plt.show()