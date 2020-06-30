# Problem statement:
# Superhero Statistics
# The rise of superheroes and supervillains is at an all-time high. The 'Academy of Super Beings(ASB)' was formed to bring order to it. We have with us the data of more than 500 superhumans but we need your knowledge of descriptive statistics in figuring out the important insights from it.

#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here

data['Gender'].replace('-', 'Agender', inplace = True)
data.Gender.value_counts().plot(kind = 'bar')
plt.xlabel('Genders')
plt.ylabel('Count')
plt.xticks(rotation = 0)

plt.figure(figsize = (8,6))
data['Alignment'].value_counts().plot(kind = 'bar')
plt.show()


cov = data[['Strength', 'Combat']].cov().iloc[0,1]
pearson_strength = cov / data['Strength'].std() * data['Combat'].std()
print(pearson_strength)

cov = data[['Intelligence', 'Combat']].cov().iloc[0,1]
pearson_intelligence = cov / data['Intelligence'].std() * data['Combat'].std()
print(pearson_intelligence)

q_high = data['Total'].quantile(0.99)
super_best_names = list(data[data['Total'] > q_high]['Name'])
print(super_best_names)
