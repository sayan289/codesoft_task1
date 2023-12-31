# -*- coding: utf-8 -*-
"""Credict_card_fraud_detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ujjJLa-AWYLpvpM7VgPgwBZsvdno4EWp
"""

import numpy as np
import pandas as pd
df=pd.read_csv('fraudTrain.csv')

"""Taking the Dataset into the Dataframe so that we can easily perform operation on the Dataframe."""

df.head(10)

"""Type of column present in the DataFrame"""

df.dtypes

"""Drop the unnecessary Column from the Dataframe that does not important for our model"""

df=df.drop(['trans_date_trans_time','merchant','category','first','last','gender','trans_num','street','city','state','job','dob'],axis=1)

df.shape

"""Taking the feature set into x which is also called independent variable"""

x=df.iloc[:,1:10]
x

"""Take the output column in y variable which is called Dependent variable"""

y=df.iloc[:,10]
y

"""Check how many 0 and 1 present in the output column"""

print(df.is_fraud.value_counts())

df.isnull().sum()

"""replace nan value by it's mean value of the output column"""

df['is_fraud'].fillna(df['is_fraud'].median(), inplace = True)

df.replace(0,np.median)
df

color_wheel = {1: "#0392cf", 2: "#7bc043"}
colors = df["is_fraud"].map(lambda x: color_wheel.get(x + 1))
print(df.is_fraud.value_counts())
p=df.is_fraud.value_counts().plot(kind="bar")

"""The dataset is unbalanced, to balanced the dataset we used oversampeling. As a result total number of 0 and 1 of the output column become equal"""

from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler(random_state=42)

x_ros, y_ros = ros.fit_resample(x,y)

print('Original dataset shape', df.is_fraud.value_counts())
print('Resample dataset shape', np.unique(y_ros, return_counts=True))

x=x_ros
y=y_ros

import matplotlib.pyplot as plt
color_wheel = {1: "#0392cf", 2: "#7bc043"}
colors = y.map(lambda x: color_wheel.get(x + 1))
print(y.value_counts())
p=y.value_counts().plot(kind="bar")

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.3)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
xtrain=sc.fit_transform(xtrain)
xtest=sc.fit_transform(xtest)

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

"""DecisionTree Model"""

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier(criterion='entropy',max_depth=3)
dt.fit(xtrain,ytrain)
ypred=dt.predict(xtest)
scores=cross_val_score(dt,x,y,cv=10)
print("Accuracy of Decission Tree is :",scores.mean()*100)
print(classification_report(ytest,ypred,digits=2))

"""LogisticRegression Model"""

from sklearn.linear_model import LogisticRegression
lg=LogisticRegression()
lg.fit(xtrain,ytrain)
ypred1=lg.predict(xtest)
scores=cross_val_score(dt,x,y,cv=10)
print("Accuracy of Decission Tree is :",scores.mean()*100)
print(classification_report(ytest,ypred1,digits=2))

"""RandomForestClassifier Model"""

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(xtrain, ytrain)
rfc_pred = rfc.predict(xtest)
scores=cross_val_score(dt,x,y,cv=10)
print("Accuracy of Decission Tree is :",scores.mean()*100)
print(classification_report(ytest,rfc_pred,digits=2))