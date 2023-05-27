import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Load the data into a DataFrame
df = pd.read_excel('../P5_C1/bug_report_key.xlsx')

df['mark'] = df['Text_new'].apply(lambda x: '*' if 'stop work' in x else '')

df[df['mark'] == '*'].to_excel('bug_report_key_stop_work.xlsx', index=False)

df = pd.read_excel('../P5_C1/bug_report_key_stop_work.xlsx')

top10_skill = df['Skill No'].value_counts().nlargest(10)

print(top10_skill)