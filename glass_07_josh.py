# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:58:49 2015

@author: joshstrupp
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read the data into the dataframe
df = pd.read_csv('glass.data', names=col_names)
df.head
col_names = ['ID', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'source']
df.describe()d
df.shape

#make a new bibary column
df['binary'] = np.where(df.source < 5, 0, 1) #When True, yield x, otherwise yield y.
df['binary'] = df.source.map({1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:1})
df.binary.value_counts()

#Create feature matrix X
features = ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']
X = df[features] 

y = df.binary #create the response vector

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=99)

#fit a KNN model on the training set using K=5
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred)
#90.741

#null accuracy - What is this exactly?
1 - y.mean() #= 76.168