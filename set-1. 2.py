from sklearn.datasets import load_diabetes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the diabetes dataset
diabetes = load_diabetes()

# Create a DataFrame
diabetes_df = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)

# Add the target variable 'target' to the DataFrame
diabetes_df['target'] = diabetes.target

# Display the first few rows of the DataFrame
print(diabetes_df.head())
# Bar graph for 'target' variable
sns.countplot(x='target', data=diabetes_df)
plt.title('Distribution of Diabetes Progression')
plt.xlabel('Diabetes Progression')
plt.ylabel('Count')
plt.show()

# Line chart for 'age' variable
sns.kdeplot(diabetes_df['age'], fill=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Density')
plt.show()
