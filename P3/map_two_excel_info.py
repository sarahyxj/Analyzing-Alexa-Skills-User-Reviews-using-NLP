import pandas as pd
import warnings

warnings.filterwarnings("ignore")

# Read both Excel files into dataframes
df1 = pd.read_excel('../P3/merged_excel.xlsx',usecols='A:Z')
df2 = pd.read_excel('../Rawdata/UQ-AAS21-I.xlsx', usecols=['Index', 'Developers','Category'])

merged_df = pd.merge(df1, df2, left_on='Skill No', right_on='Index')

merged_df['Domain'] = df2['Category']

merged_df.to_excel('result.xlsx', index=False)
