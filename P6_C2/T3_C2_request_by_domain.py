
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

"Domain level testings"
"This test is to analyze the feature request C2 category for top10 domains"


# Load the data into a DataFrame
df = pd.read_excel('../P3/classified_data_all.xlsx')

# Filter by category
category_1 = df.loc[df['category_new'] == 2]


# Count the number of occurrences of each year
counts = category_1['Domain'].value_counts().head(10)

# Sort the counts by domains in aescending order
counts = counts.sort_values(ascending=True)

colors = plt.cm.Blues(np.linspace(0, 1.5, 10))
# Plot the data
ax = counts.plot(kind='bar', x='Domain', y='count', rot=90, color=colors)

# Set the title of the plot
ax.set_title('Feature Request by top10 Domains')

# Set the x-axis tick labels to only show the year
# ax.set_xticklabels(counts.index.astype(int))

plt.tight_layout()

# Save the plot as an image file
plt.savefig('feature_request_domain.png')

# Show the plot
plt.show()
