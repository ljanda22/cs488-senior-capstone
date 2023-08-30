# import necessary libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# generate synthetic dataset for credit card fraud detection
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=0, n_classes=2, weights=[0.95, 0.05], random_state=42)

# split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create Random Forest model with default parameters
rf_model = RandomForestClassifier(random_state=42)

# train the model on the training data
rf_model.fit(X_train, y_train)

# make predictions on the test data
y_pred = rf_model.predict(X_test)

# calculate evaluation metrics
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc_roc = roc_auc_score(y_test, y_pred)

# print the evaluation metrics
print('Precision score:', precision)
print('Recall score:', recall)
print('F1-score:', f1)
print('AUC-ROC score:', auc_roc)

