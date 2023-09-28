# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Load the dataset
data = pd.read_csv("/kaggle/input/creditcardfraud/creditcard.csv")

# Standardize the 'Amount' feature
data['normAmount'] = StandardScaler().fit_transform(data['Amount'].values.reshape(-1, 1))
data = data.drop(['Time', 'Amount'], axis=1)

# Split the dataset into features (x) and target (y)
x = data.drop("Class", axis=1)
y = data["Class"]

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# Initialize and train a Random Forest Classifier
random_forest_classifier = RandomForestClassifier(random_state=0)
random_forest_classifier.fit(x_train, y_train)

# Make predictions on the test set
y_pred = random_forest_classifier.predict(x_test)

# Evaluate the model
confusion_mat = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print("Confusion Matrix:\n", confusion_mat)
print("Accuracy:", accuracy)
