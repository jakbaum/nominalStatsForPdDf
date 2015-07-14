import scipy.stats as scs
import pandas as pd

def categories(series):
    return range(int(series.min()), int(series.max()) + 1)

def make_crosstable(df,col1,col2):
        df_col1, df_col2 = df[col1], df[col2]
        cats1, cats2 = categories(df_col1), categories(df_col2)

        def aux(is_cat1):
            return [sum(is_cat1 & (df_col2 == cat2)) 
                    for cat2 in cats2]

        return [aux(df_col1 == cat1)
                  for cat1 in cats1]

def sum_crosstable(table):
    s=0
    for l in table:
        s += sum(l)
    return s
    
def chi_square(df, col1, col2):
	'''computes Chi Square Test of Independence'''
    return scs.chi2_contingency(make_crosstable(df,col1,col2))

def cramers_v(df,col1,col2):
	'''computes Cramer's V'''
    table = make_crosstable(df,col1,col2)
    return math.sqrt(scs.chi2_contingency(table)[0]/(sum_crosstable(table)*(min(df[col1].max()+1,df[col2].max()+1)-1)))

def nominal_corr(df,col1,col2):
    '''computes chi_square test for independence and Cramer's V
    returns list with [chi2, p-Value, Cramer's V, significance-status]'''
    return_list = []
    chi2 = chi_square(df,col1,col2)
    return_list.append(chi2[:2])
    return_list.append(cramers_v(df,col1,col2))
    sig = ''
    if chi2[1] < 0.05:
        sig = '*'
    elif chi2[1] < 0.01:
        sig = '**'
    elif chi2[1] < 0.01:
        sig = '***'
    return_list.append(sig)
    return return_list