# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file and Let's check which variable is categorical and which one is numerical so that you will get a basic idea about the features of the bank dataset.


bank_data = pd.read_csv(path)
categorical_var = bank_data.select_dtypes(include = 'object')
print(categorical_var.shape)
numerical_var = bank_data.select_dtypes(include = 'number')
print(numerical_var.shape)
#2 Sometimes customers forget to fill in all the details or they don't want to share other details. Because of that, some of the fields in the dataset will have missing values. Now you have to check which columns have missing values and also check the count of missing values each column has. If you get the columns that have missing values, try to fill them.

banks = bank_data.drop('Loan_ID', axis = 1)
# print(banks.isnull().sum())
bank_mode = banks.mode()
banks = banks.fillna(bank_mode.iloc[0])
# banks = banks.apply(lambda col: col.fillna(col.mode()), axis = 0)
print(banks.isnull().sum().values.sum())
print(banks.shape)
#3 Now let's check the loan amount of an average person based on 'Gender', 'Married', 'Self_Employed'. This will give a basic idea of the average loan amount of a person.

avg_loan_amount = pd.pivot_table(banks, index = ['Gender', 'Married', 'Self_Employed'], values = 'LoanAmount', aggfunc =np.mean)
print(round(avg_loan_amount['LoanAmount'][1],2))

#4 Now let's check the percentage of loan approved based on a person's employment type.

loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]

loan_stat = len (banks['Loan_Status'])
print(loan_stat)
percentage_se = round((len(loan_approved_se)/loan_stat) * 100, 2)
percentage_nse = round((len(loan_approved_nse)/loan_stat) * 100, 2)

print(percentage_nse, percentage_se)

#5 A government audit is happening real soon! So the company wants to find out those applicants with long loan amount term.
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x /12 )
big_loan_term = len(loan_term[loan_term >= 25])
print(big_loan_term)

#6 Now let's check the average income of an applicant and the average loan given to a person based on their income.
loan_groupby = banks.groupby('Loan_Status')['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()
print(round(mean_values.iloc[1,0], 2))



