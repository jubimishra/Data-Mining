#SVM Classifier experiment

# In[63]:

import numpy as np
import pandas as pd
from sklearn import datasets, preprocessing
from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import accuracy_score


# In[181]:

cancer_data=[]
cancer_labels=[]
for line in file('breast-cancer-wisconsin.data'):
    if '?' in line:
        continue
    data=[float(x) for x in line.split(',')[1:-1]]
    cancer_data.append(data)
    cancer_labels.append(int(line.split(',')[-1]))
  

X_train, X_test,Y_train, Y_test= cross_validation.train_test_split(cancer_data,cancer_labels,test_size=0.8)
clf=svm.SVC(kernel="linear", C=0.01)
clf.fit(X_train, Y_train)
pred=clf.predict(X_test)
accuracy=accuracy_score(Y_test, pred)
test=pd.DataFrame(Y_test)
pred=pd.DataFrame(pred)
print "Mismatched prediction for class 2: ",pred[pred[test[0]==2]==4].count()
print "Mismatched prediction for class 4: ",pred[(pred[test[0]==4]==2)].count()

for i in range(10):
    X_train, X_test,Y_train, Y_test= cross_validation.train_test_split(cancer_data,cancer_labels,test_size=0.8)
    clf=svm.SVC(kernel="linear", C=0.01)
    clf.fit(X_train, Y_train)
    pred=clf.predict(X_test)
    accuracy=accuracy_score(Y_test, pred)
    total=total+accuracy
    print accuracy

print "\nAverage accuracy :"
print (total)/float(10)


