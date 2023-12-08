'''
Question 1
Write a function called proportion_of_education which returns the proportion of children in the dataset who had a mother with the education
 levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.
This function should return a dictionary in the form of (use the correct numbers, do not round numbers):
    {"less than high school":0.2,
    "high school":0.4,
    "more than high school but not college":0.2,
    "college":0.2}

def proportion_of_education():
    # your code goes here
    # YOUR CODE HERE
    raise NotImplementedError()

Question 2
Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider.
Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child, those who know did not.
This function should return a tuple in the form (use the correct numbers:
(2.5, 0.1)

def average_influenza_doses():
    # YOUR CODE HERE
    raise NotImplementedError()

assert len(average_influenza_doses())==2, "Return two values in a tuple, the first for yes and the second for no."

Question 3 (Home)
It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child. 
Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it 
(at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.
This function should return a dictionary in the form of (use the correct numbers):
    {"male":0.2,
    "female":0.4}
Note: To aid in verification, the chickenpox_by_sex()['female'] value the autograder is looking for starts with the digits 0.0077.
'''
import pandas as pd
import numpy as np

print('Задание 1')
def proportion_of_education():
    df = pd.read_csv("NISPUF17.csv", index_col=0)
    EDUC = df['EDUC1']
    educ = np.sort(EDUC.values)
    p_o_e = {"less than high school": 0,
             "high school": 0,
             "more than high school but not college": 0,
             "college": 0}
    n = len(educ)
    p_o_e["less than high school"] = np.sum(educ == 1)/n
    p_o_e["high school"] = np.sum(educ == 2)/n
    p_o_e["more than high school but not college"] = np.sum(educ == 3)/n
    p_o_e["college"] = np.sum(educ == 4)/n
    return p_o_e
print(proportion_of_education())

print('Задание 2')
def average_influenza_doses():
    df = pd.read_csv("NISPUF17.csv", index_col=0)
    vac = df[['CBF_01','P_NUMFLU']]
    cbf_1 = vac[vac['CBF_01'] == 1].dropna()
    cbf_2 = vac[vac['CBF_01'] == 2].dropna()
    flu1 = cbf_1['P_NUMFLU']
    flu2 = cbf_2['P_NUMFLU']
    ans1 = np.sum(flu1)/flu1.size
    ans2 = np.sum(flu2)/flu2.size
    return (ans1, ans2)
print(average_influenza_doses())

print('Задание 3')
def chickenpox_by_sex():
    df = pd.read_csv("NISPUF17.csv", index_col=0)
    c_vac = df[df['P_NUMVRC']>0] 
    st_m = c_vac[c_vac['SEX']==1]
    l_m = len(st_m[st_m['HAD_CPOX']==2])
    so_m = len(st_m[st_m['HAD_CPOX']==1])/l_m
    st_w = c_vac[c_vac['SEX']==2]
    l_w = len(st_w[st_w['HAD_CPOX']==2])  
    so_f = len(st_w[st_w['HAD_CPOX']==1])/l_w
    so = {'male':so_m,'female':so_f}
    return so
print(chickenpox_by_sex())