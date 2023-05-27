import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel('../P3/classified_data.xlsx', header=0, index_col=None)
# df = df[df['category_new'] == 0].squeeze(axis=1)


# df = df[df['category_new'] == 0].squeeze(axis=1)
df = df[df['category_new'].isin([0, 1,2,3])]


# 删除包含NaN值的行
df = df.dropna(subset=['Skill No'])

# 将skill_no转换为int
df['Skill No'] = df['Skill No'].astype(int)


# 按技能编号分组并计算数量
df = df.groupby('Skill No').size().sort_values(ascending=True)

colors = plt.cm.Blues(np.linspace(0, 1, 10))

# 绘制条形图
df.plot.bar(rot=45,color = colors)



# 添加标签和标题
plt.xlabel('skill_no')
plt.ylabel("No. of skill's review")
plt.title('Top 10 Alexa Skills user reviews')

print(df)


# 显示图表
plt.show()