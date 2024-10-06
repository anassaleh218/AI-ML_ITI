# # Naive Bayes
# import pandas as pd

# dataset=pd.read_csv('hist_features.csv')
# #print(dataset.shape)

# x=pd.DataFrame(dataset.iloc[:,:-1])
# y=pd.DataFrame(dataset.iloc[:,-1])
# #print(y)

# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2)
# # GaussianNB
# from sklearn.naive_bayes import GaussianNB
# nBmodel = GaussianNB()
# nBmodel.fit(X_train , y_train)
# y_predicted = nBmodel.predict(X_test)
# # metrics
# from sklearn import metrics 
# print(metrics.accuracy_score(y_predicted , y_test))
# # confusion_matrix
# from sklearn.metrics import confusion_matrix
# print(pd.DataFrame(
#     confusion_matrix(y_test, y_predicted),
#     columns=['Predicted Not BT', 'Predicted BT'],
#     index=['Actual Not BT', 'Actual BT']
# ))
##########################
# KNN
import pandas as pd
import numpy as np

dataset=pd.read_csv('hist_features.csv')
#print(dataset.shape)

x=pd.DataFrame(dataset.iloc[:,:-1])
y=pd.DataFrame(dataset.iloc[:,-1])
#print(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=2)
# KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
# Fix the issue by using ravel() to convert y_train to a 1D array
knn.fit(x_train, y_train.values.ravel())
y_predicted = knn.predict(x_test)
# confusion_matrix
from sklearn.metrics import classification_report,confusion_matrix
# print(confusion_matrix(y_test,y_predicted))
print(pd.DataFrame(
    confusion_matrix(y_test, y_predicted),
    columns=['Predicted Not BT', 'Predicted BT'],
    index=['Actual Not BT', 'Actual BT']
))