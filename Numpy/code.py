# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

census = np.append(data, new_record, axis =0)
print("shape of data",data.shape)
print("shape of census",census.shape)
age = census[:,0]
print(age.shape)

max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)

print(max_age)
print(min_age)
print(round(age_mean,2))
print(round(age_std,2))


race = census[:,2]
race_0 = race[race == 0]
race_1 = race[race == 1]
race_2 = race[race == 2]
race_3 = race[race == 3]
race_4 = race[race == 4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

unique, counts = np.unique(race, return_counts = True)
freq = np.asarray((unique, counts)).T
result = np.where(freq[:,1] == np.min(freq[:,1]))
minority_race = int(freq[result[0],1])
print('minority_race', minority_race) 

senior_citizens = census[:,0][census[:,0] > 60]
working_hours_sum = int(sum(census[:,6][census[:,0] > 60]))

print(working_hours_sum)
avg_working_hours = round(working_hours_sum /len(senior_citizens), 2)
print(avg_working_hours)

high = census[:,:][census[:,1] > 10 ]
low = census[:,:][census[:,1] <= 10 ]
print(high.shape)
print(low.shape)

avg_pay_high = round(np.mean(high[:,7]), 2)
avg_pay_low = round(np.mean(low[:,7]), 2)

print(avg_pay_high)
print(avg_pay_low)









