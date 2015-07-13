import scipy.stats as scs
import pandas as pd

def create_list_sum_of_categories(df, var, cat, var2):
    list1 = []
    for cat2 in range(int(df[var2].min()), int(df[var2].max())+1):
            list1.append( len(df[ (df[var] == cat) & (df[var2] == cat2) ]))   
    return list1

def run(df,col1,col2):
    ''' for each category of col1 create list with sums of each category of col2'''
    result_list = []
    for cat in range(int(df[col1].min()), int(df[col1].max())+1):
        result_list.append(create_list_sum_of_categories(df,col1,cat,col2)) 

    return scs.chi2_contingency(result_list)



