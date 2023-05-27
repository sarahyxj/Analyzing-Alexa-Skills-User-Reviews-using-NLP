import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from P2.text_preprocessing import clean_text,remove_emoji


"This test is to extract the 'scam' from the C1" 

df = pd.read_excel('../P3/classified_data_all.xlsx', header=0, index_col=None)
# df = df[df['category_new'] == 1]
df = df[df['category_new'] == 1].squeeze(axis=1)

df.loc[:, 'Text_new'] = df['Text'].apply(clean_text).apply(remove_emoji)

df['scam'] = df['Text_new'].str.contains('scam') & ~df['Text_new'].str.contains('not scam')

scam_df = df[df['scam'] == True]

scam_df.to_excel('scam_report.xlsx', index=False)


df = pd.read_excel('../P5_C1/scam_report.xlsx', header=0, index_col=None)

df = df.dropna(subset=['Skill No'])


count = df['Skill No'].value_counts().head(50).rename_axis('Skill No').reset_index(name='counts')

print(count.head(10))
count.plot.scatter(x='Skill No', y='counts')


# # 添加标签和标题
plt.ylabel("Time of scams mentioned")
plt.title('Potential Scams from User Reviews')

plt.tight_layout()
# fig, ax = plt.subplots()
# ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

plt.show()