# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# Load the dataset from Power BI (Power BI automatically assigns this)
df = dataset

# Feature selection - Choosing relevant columns
X = df[['Margin', 'Const. No.']]  # Features (you can add more)
y = df['Status']  # Target column

# Convert categorical target column to numerical (won=1, lost=0)
y = y.map({'Result Declared': 1, 'Uncontested': 0})

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Visualize Feature Importance
importances = model.feature_importances_
features = X.columns
indices = importances.argsort()

# Plot Feature Importance
plt.figure(figsize=(10,6))
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()
