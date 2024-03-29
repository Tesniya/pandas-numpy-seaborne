# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales=pd.read_csv('/content/Sales_add.csv')

sales.head()

sales.info()

#The company wishes to clarify whether there is any increase in sales after stepping into digital marketing.
let m1=avg sales after stepping into digital marketing
    m2=avg sales before stepping into digital marketing
    therefore hypothesis is
     H0=m1<=m2
     H1=m1>m2
     since sample size of both the groups is less than 30 we can use independent two sample T-test for testing the hypothesis

#Importing the function for T test
from scipy.stats import ttest_ind

t_stat,p_value=ttest_ind(sales['Sales_After_digital_add(in $)'],sales['Sales_before_digital_add(in $)'],alternative="greater")

t_stat

p_value

if p_value < 0.05:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
     Rejects the null hypothesis.
Hence we reject the null hypothesis at 5% level of significance. Therefore from the given sample observations we can say that there is a significant increase in sales after stepping into digital marketing.

#The company needs to check whether there is any dependency between the features “Region” and “Manager”.
using the Chisquare test of Independence to test whether there is any dependency between the features “Region” and “Manager”. The hypothesis to be tested is
H0: Region and Sales are independent of each other
H1: Region and Sales are not independent of each other

sales1=pd.melt(sales,id_vars=['Manager','Region'],value_vars=['Sales_before_digital_add(in $)','Sales_After_digital_add(in $)'],value_name='Sales')

sales1

ctab=pd.crosstab(sales1['Region'],sales1['Manager'],values=sales1['Sales'],aggfunc='sum')
ctab

from scipy.stats import chi2_contingency

chistat,pvalue,dof,expected=chi2_contingency(ctab)

chistat

pvalue

dof

if pvalue < 0.05:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
    Reject the null hypothesis.
Therefore the variables, manager and region are dependent at 4 degrees of freedom and 5% level of significance