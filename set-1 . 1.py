import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data ={
    'age':[22,25,39,45,33],
    'salary':[40000,45000,150000,200000,120000]
    }
df = pd.DataFrame(data)
corre = df.corr()
cov = df.cov()

print("Correlation matrix\n",corre)
print("Covariance matrix\n",cov)
sns.heatmap(corre,annot = True)

plt.title('correlation plot')
plt.show()
