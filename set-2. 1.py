import numpy as np
import pandas as pd
from scipy.stats import pearsonr , spearmanr
data ={
    'age':[22,25,39,45,33],
    'salary':[40000,45000,150000,200000,120000]
    }
df = pd.DataFrame(data)
p_corr = pearsonr(df['age'],df['salary'])
s_corr = spearmanr(df['age'],df['salary'])

print("Pearson Correlation Coefficient:", p_corr)
print("Spearman's Rank Correlation Coefficient:", s_corr)
