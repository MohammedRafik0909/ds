import numpy as np
import matplotlib.pyplot as plt

patients_smoke = [50, 60, 70, 80, 90]
patients_lung_cancer = [10, 15, 20, 25, 30]

correlation_coefficient = np.corrcoef(patients_smoke, patients_lung_cancer)[0, 1]

plt.scatter(patients_smoke, patients_lung_cancer)
plt.title('Correlation Between Smoking and Lung Cancer')
plt.xlabel('Number of Patients Who Smoke')
plt.ylabel('Number of Patients with Lung Cancer')
plt.text(60, 20, f'Correlation Coefficient: {correlation_coefficient:.2f}', bbox=dict(facecolor='white', alpha=0.5))

plt.show()
