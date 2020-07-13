# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)

#Code starts here
#Check if population mean of installment is in confidence interval
data_sample = data.sample(sample_size, random_state = 0)
sample_mean = data_sample['installment'].mean()
sample_std = data_sample['installment'].std()
margin_of_error = z_critical * (sample_std/np.sqrt(sample_size))

true_mean = data['installment'].mean()

confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

if (confidence_interval[0] < true_mean < confidence_interval[1] ):
    print('True mean is in Calculated confidence interval')
print(round(true_mean,2))
print(confidence_interval)

#find if CLT holds for installment column
fig, axes = plt.subplots(nrows = 3, ncols = 1)
sample_sizes = np.array([20, 50, 100])
for sz in range(len(sample_sizes)):
    mean_sample = []
    for i in range(1, 1000):
        data_sample = data.sample(sample_sizes[sz])
        mean_sample.append(data_sample['installment'].mean())
    axes[sz].hist(pd.Series(mean_sample))
plt.show()

#Hypothesis testing
#Null Hypothesis : No diff in interest rate given to people with purpose as 'small business'
#Alternate Hyothesis: Interest rate given to people with purpose 'small business is higher than the average interest rate.

data['int.rate'] = data['int.rate'].map(lambda x : x.strip('%')).astype('float64')
z_statistic_1, p_value_1 = ztest(x1 = data[data['purpose'] == 'small_business']['int.rate'],value = data['int.rate'].mean(), alternative = 'larger') 

print('z_statistic is : {}'.format(z_statistic_1))
print('p-value is :{}', p_value_1)

## Installment vs Loan Defaulting
#Null Hypothesis : No difference in installments being paid by loan defaulters and loan non defaulters
#Alternate Hypothesis H_1:Difference in installments being paid by loan defaulters and loan non defaulters

z_statistic_2, p_value_2 = ztest(x1=data[data['paid.back.loan']=='No']['installment'], x2=data[data['paid.back.loan']=='Yes']['installment'])
print('z-stat is :{}'.format(z_statistic_2))
print('p_val', p_value_2)

#Purpose vs Loan Defaulting
#Null Hypothesis : Distribution of purpose across all customers is same.
#Alternative Hypothesis : Distribution of purpose for loan defaulters and non defaulters is different.
critical_value = stats.chi2.ppf(q = 0.95, df = 6) #critical value = 95% , df = number of categories (in purpose)
yes = data[data['paid.back.loan'] == 'Yes']['purpose'].value_counts()
no = data[data['paid.back.loan'] == 'No']['purpose'].value_counts()
observed = pd.concat([yes.T, no.T], axis=1, keys=['Yes', 'No'])
chi2, p, dof, ex = chi2_contingency(observed)
print('Chi-2 Statistic: ',chi2)
print('Critical Value: ',critical_value)
print('p-value: ',p)
if(chi2>critical_value):
    print('Null Hypothesis Rejected!')
else:
    print('Null Hypothesis Accepted!')










