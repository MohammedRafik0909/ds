import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.datasets import load_iris
iris = load_iris()
X,y = iris.data,iris.target
print(y)
X_train, X_test, y_train, y_test = train_test_split(X,y ,test_size=0.2, random_state=42)


linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)


y_pred_linear = linear_model.predict(X_test)
y_pred_logistic = logistic_model.predict(X_test)


plt.plot(y_pred_linear, y_test, label='Original Data', color='red')
plt.title('Linear Regression')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Binary Classification')
plt.legend()
plt.show()

plt.plot(y_pred_logistic, y_test, label='Original Data', color='red')
plt.title('Logistic Regression')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Binary Classification Probability')
plt.legend()

plt.show()
