
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

"General testings"
"This test is to filter the C1-bug report by years"
" There is an increase of bugs through the year from 2016 to 2020"

# Load the data into a DataFrame
df = pd.read_excel('../P3/classified_data_all.xlsx')

# Convert the 'Reviewed Time' column to a datetime object
df['Reviewed Time'] = pd.to_datetime(df['Reviewed Time'])

# Filter by category
category_1 = df.loc[df['category_new'] == 1]

# Extract the year from the 'Reviewed Time' column
category_1['Year'] = category_1['Reviewed Time'].dt.year

# Count the number of occurrences of each year
counts = category_1['Year'].value_counts()

# Sort the counts by year
counts = counts.sort_index()

# Exclude 2021 data
counts = counts.loc[counts.index != 2021]

colors = plt.cm.Blues(np.linspace(0, 1.5, 10))
# Plot the data
ax = counts.plot(kind='bar', x='Year', y='count', rot=45, color=colors)

# Set the title of the plot
ax.set_title('Bug Report by Years')

# Set the x-axis tick labels to only show the year
ax.set_xticklabels(counts.index.astype(int))

# Save the plot as an image file
plt.savefig('bug_report.png')

# Show the plot
plt.show()


