# -*- coding: utf-8 -*-
"""Random_Forest_Assignment16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rabv78RQ-nYx2qkgbPkyJd-b5aNx_I8q
"""

#Social_Network_Ads.csv

"""**Importing the libraries**"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""**Importing the dataset**"""

df=pd.read_csv('/content/Social_Network_Ads.csv')
df

"""**Splitting the dataset into the Training set and Test set**"""

X=df.iloc[:,[2,3]]
X
y=df.iloc[:,-1]
y

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

"""**Feature Scaling**"""

from sklearn.preprocessing import StandardScaler
SS=StandardScaler()
X_train=SS.fit_transform(X_train)
X_test=SS.transform(X_test)

"""**Fitting Random Forest to the Training set**"""

from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier()
rfc.fit(X_train,y_train)

print(rfc.score(X_train,y_train))

print(rfc.score(X_test,y_test))

"""**Predicting the Test set results**"""

from sklearn.metrics import accuracy_score

y_pred=rfc.predict(X_test)

"""**Making the Confusion Matrix**"""

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,y_pred)

"""**Visualising the Training set results**"""

from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, rfc.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

"""**Visualising the Test set results**"""

from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, rfc.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()







