import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("breast_cancer.csv")
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)


from sklearn.linear_model import LogisticRegression

classification = LogisticRegression(random_state=0)
classification.fit(x_train, y_train)

y_pred = classification.predict(x_test)


from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_pred, y_test)
from sklearn.metrics import accuracy_score

print(cm)


from sklearn.model_selection import cross_val_score

accuracies = cross_val_score(estimator=classification, X=x_train, y=y_train, cv=10)
print("accuracy with k_fold hai {:.2f} %".format(accuracies.mean() * 100))
print("standard deviation with k_fold hai {:.2f} %".format(accuracies.std() * 100))


import joblib

joblib.dump(classification, "breast_cancer.pkl")
