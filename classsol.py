#Grupo 2: André Fonseca (84698), Leonor Loureiro (84736)

import numpy as np
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib
import timeit

from sklearn.model_selection import cross_val_score


def features(X):

    F = np.zeros((len(X),5))
    for x in range(0,len(X)):
        F[x,0] = len(X[x])
        F[x,1] = ord(X[x][0])
        F[x,2] = nr_vogals(X[x])
        F[x,3] = ord(X[x][-1])
        F[x,4] = hash(X[x])

    return F

def mytraining(f,Y):

    clf = neighbors.KNeighborsClassifier(weights='distance',n_neighbors=3)
    clf.fit(f, Y)
    return clf

def mytrainingaux(f,Y,par):
    
    clf.fit(f,Y)

    return clf

def myprediction(f, clf):
    Ypred = clf.predict(f)

    return Ypred


def nr_vogals(s):
    x = 0;
    for i in range(len(s)):
        if s[i] in ['a','A','e','E','i','I','o','O','u', 'U']:
            x+=1
    return x
