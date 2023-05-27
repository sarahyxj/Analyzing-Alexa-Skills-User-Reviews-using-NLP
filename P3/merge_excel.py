import os
import pandas as pd


"merge the files from raw data"

def merge_excel_files(folder_path, output_file):
    all_data = pd.DataFrame()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.xlsx'):
                file_path = os.path.join(root, file)
                data = pd.read_excel(file_path , engine = 'openpyxl')
                all_data = pd.concat([all_data, data], ignore_index=True)
    all_data.to_excel(output_file, index=False)
    print('There are {} rows and {} columns in this report'.format(all_data.shape[0],all_data.shape[1]))
    


merge_excel_files('../Rawdata', 'merged_excel.xlsx')

df = pd.read_excel('merged_excel.xlsx')

# Remove leading and trailing spaces from cell A1
df['Text'] = df['Text'].str.strip()

df.to_excel('merged_excel.xlsx', index=False)
