# -*- coding: utf-8 -*-
"""CodeClauseDStask2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bVMl0KWG_5OgM5bQLLgfnhuf3VZHlt_O

#CodeClause Data Science Internship

###Task 2 - Wine Quality Prediction

Importing necessary libraries:
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression

import warnings
warnings.filterwarnings('ignore')

"""Importing our dataset:"""

df = pd.read_csv('/content/WineQT.csv')
df

"""Exploratory data Analysis:"""

df.info()

df.describe().T

df.isnull().sum()

df.hist(bins=20, figsize=(10, 10))
plt.show()

"""Finding the number of data items for each quality of wine:"""

plt.bar(df['quality'], df['alcohol'])
plt.xlabel('quality')
plt.ylabel('alcohol')
plt.show()

plt.figure(figsize=(12, 12))
sb.heatmap(df.corr() > 0.7, annot=True, cbar=False)
plt.show()

"""Thus, we can see that there is no redundant data in our dataset.

Developing our model:
"""

df['best quality'] = [1 if x > 5 else 0 for x in df.quality]

df.replace({'white': 1, 'red': 0}, inplace=True)

features = df.drop(['quality', 'best quality'], axis=1)
target = df['best quality']

xtrain, xtest, ytrain, ytest = train_test_split(
	features, target, test_size=0.2, random_state=40)

xtrain.shape, xtest.shape

"""Normalising the data:"""

norm = MinMaxScaler()
xtrain = norm.fit_transform(xtrain)
xtest = norm.transform(xtest)

"""Training Support Vector Classifier and Logisitic Regression models using our prepared data:"""

models = [LogisticRegression(), SVC(kernel='rbf')]

for i in range(2):
	models[i].fit(xtrain, ytrain)

	print(f'{models[i]} : ')
	print('Training Accuracy : ', metrics.roc_auc_score(ytrain, models[i].predict(xtrain)))
	print('Validation Accuracy : ', metrics.roc_auc_score(
		ytest, models[i].predict(xtest)))
	print()

print(metrics.classification_report(ytest,
									models[1].predict(xtest)))