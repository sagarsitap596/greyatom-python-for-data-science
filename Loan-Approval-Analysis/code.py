# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
 # code starts here
bank = pd.read_csv(path,delimiter = ',')

categorical_var = bank.select_dtypes(include="object")

print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')

print(numerical_var)




# code ends here


# --------------
# code starts here

banks = bank.drop(labels = ['Loan_ID'],axis=1)

# print(banks.isnull().sum)

bank_mode = banks.mode()

print(bank_mode)

banks.fillna(bank_mode.loc[0,:], inplace=True)

print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here

avg_loan_amount = pd.pivot_table(banks,index = ['Gender','Married','Self_Employed'],values=['LoanAmount'],aggfunc='mean')
avg_loan_amount



# code ends here



# --------------
# code starts here

b = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] =='Y')]
loan_approved_se = len(b.index)
print(loan_approved_se)

b = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] =='Y')]
loan_approved_nse = len(b.index)
print(loan_approved_nse)

percentage_se = (loan_approved_se / 614 ) *100

percentage_nse = (loan_approved_nse / 614 ) *100

print(percentage_se,percentage_nse)

# code ends here


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x : x/12)

print(loan_term)

big_loan_term = len(loan_term[loan_term >= 25 ])

print(big_loan_term)

# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby(['Loan_Status'])

print(loan_groupby)

loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]

mean_values = loan_groupby.mean()

print(mean_values)

# code ends here


