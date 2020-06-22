# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file
loan_status = data['Loan_Status'].value_counts()
loan_status.plot.bar(title = "Record of companies Loan approval")
print(loan_status[0])
print(loan_status[1])
print(data.iloc[25,1])
print(data.iloc[53,9])
## Company has many loan approvals
#Creating a new variable to store the value counts
property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
print(property_and_loan.head())
#Plotting bar plot
property_and_loan.plot.bar(rot = 45)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')



# Step 2
#Plotting an unstacked bar plot




#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis
property_and_loan['N'][1]
property_and_loan['Y'][0]

# Step 3
#Plotting a stacked bar plot
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
education_and_loan.plot.bar(stacked = True, rot = 45)
plt.xlabel("Education Status")
plt.ylabel("Loan Status")



#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']
fig, (ax_1, ax_2) = plt.subplots(1,2, figsize=(8,6))
graduate['LoanAmount'].plot(kind ='density', label = 'Graduate', ax =ax_1)
ax_1.set_title('Graduate')
not_graduate['LoanAmount'].plot(kind ='density', label = 'Not Graduate', ax = ax_2)
ax_2.set_title('Non Graduate')
plt.show()
#Subsetting the dataframe based on 'Education' column


#Plotting density plot for 'Graduate'


#Plotting density plot for 'Graduate'


#For automatic legend display


# Step 5
#Setting up the subplots
fig ,(ax_1,ax_2,ax_3) = plt.subplots(3, 1, figsize = (15, 10))
ax_1.scatter(data['ApplicantIncome'], data['LoanAmount'])
ax_1.set_title('Applicant Income')

ax_2.scatter(data['CoapplicantIncome'], data['LoanAmount'])
ax_2.set_title('Coapplicant Income')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'], data['LoanAmount'])
ax_3.set_title('Total Income')




#Plotting scatter plot


#Setting the subplot axis title


#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title



