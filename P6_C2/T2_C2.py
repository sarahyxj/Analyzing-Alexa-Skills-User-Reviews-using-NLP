import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

"This test is to filter the C2-feature request by years"
" There is an big amount in 2019&2020"

# Load the data into a DataFrame
df = pd.read_excel('../P3/classified_data_all.xlsx')

# Convert the 'Reviewed Time' column to a datetime object
df['Reviewed Time'] = pd.to_datetime(df['Reviewed Time'])

# Filter by category
category_1 = df.loc[df['category_new'] == 2]

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
ax = counts.plot(kind='bar', x='Year', y='count', rot=45,color=colors)

# Set the title of the plot
ax.set_title('Feature Request by Years')

# Set the x-axis tick labels to only show the year
ax.set_xticklabels(counts.index.astype(int))

# Save the plot as an image file
plt.savefig('feature_request.png')

# Show the plot
plt.show()

