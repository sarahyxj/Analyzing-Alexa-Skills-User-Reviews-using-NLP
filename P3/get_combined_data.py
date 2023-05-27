
import glob
import pandas as pd
import uuid



def combined_data(path):
# specifying the path to excel files

    # filename = str(uuid.uuid4()) + ".xlsx"
# csv files in the path
    file_list = glob.glob(path + "/*.xlsx")
     
    # concatenate all DataFrames in the list into a single DataFrame, returns new DataFrame.
    excl_list = []
     
    for file in file_list:
        excl_list.append(pd.read_excel(file))
    excl_merged = pd.concat(excl_list, ignore_index=True)
    
    excl_merged['Text'] = excl_merged['Text'].str.strip()
         
    # exports the 4 dataframe into 1 excel file
    excl_merged.to_excel('combined-all.xlsx', index=False)
    
    #loading the data
    # data = pd.read_excel (r'../P3/combined-all.xlsx')
    # print('There are {} rows and {} columns in this report'.format(data.shape[0],data.shape[1]))



# path = 

# combined_data("../Data/popular skill")
# combined_data("../Metadata/1/RE_110")

