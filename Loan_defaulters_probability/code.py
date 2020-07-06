# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#To calculate the joint probability it's very important that conditions are independent of each other. Les's check whether the condition fico credit score is greater than 700 and purpose == 'debt_consolidation' is independent of each other.
p_a = len(df[df['fico'] > 700])/len(df)
p_b = len(df[df['purpose'] == 'debt_consolidation'])/len(df)
df1 = df[df['purpose'] == 'debt_consolidation']
print(df1.shape)
p_a_b = len(df1[df1['fico'] > 700])/len(df1)

result = False
if p_a_b == p_a:
    result = True

#insight: They are dependant on each other

#Calculating conditional probability is a very important step. Let's calculate the Bayes theorem for the probability of credit policy is yes and the person is given the loan.
prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/ len(df)
prob_cs = len(df[df['credit.policy'] == 'Yes'])/len(df)

new_df = df[df['paid.back.loan'] == 'Yes']
prob_pd_cs = len(new_df[new_df['credit.policy'] == 'Yes'])/len(new_df)

bayes = prob_pd_cs * prob_lp  / prob_cs 
print(bayes)

# Let's visualize the bar plot for the purpose and again using condition where
#Instructions:
#Visualize the bar plot for the feature purpose.
#Calculate the paid.back.loan == No and the store the result in dataframe df1
#Visualize the bar plot for the feature purpose where paid.back.loan == No
df.purpose.value_counts().plot(kind = 'bar')

df1 = df[df['paid.back.loan'] == 'No']
df1.purpose.value_counts().plot(kind = 'bar')


#Let's plot the histogram for visualization of the continuous variable. So that you will get the basic idea about how the distribution of continuous variables looks like.
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()

df['installment'].hist(normed = True, bins = 50)
df['log.annual.inc'].hist(normed = True, bins = 50)









