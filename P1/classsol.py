import numpy as np
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib
import timeit

#from sklearn.model_selection import cross_val_score

def features(X):
    
    F = np.zeros((len(X),5))
    for x in range(0,len(X)):
        F[x,0] = len(X[x])
        F[x,1] = ord(X[x][0])
        F[x,2] = nr_vogals(X[x])
        F[x,3] = ord(X[x][-1])
        F[x,4] = ASCII(X[x])

    return F     

def mytraining(f,Y):

    #KNeighborsClassifier
    n_neighbors = 2
    #weights = 'distance'
    weights = 'uniform'
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(f, Y)
   
    return clf
    
def mytrainingaux(f,Y,par):
    
    return clf

def myprediction(f, clf):
    Ypred = clf.predict(f)

    return Ypred



def ASCII(s):
    x = 0
    for i in range(len(s)):
        x += ord(s[i])*2**(8 * (len(s) - i - 1))
    return x

def nr_vogals(s):
    x = 0;
    for i in range(len(s)):
        if s[i] in ['a','A','e','E','i','I','o','O','u', 'U']:
            x+=1
    return x

