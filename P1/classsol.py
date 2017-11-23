import numpy as np
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib
import timeit

from sklearn.model_selection import cross_val_score

def features(X):
    
    F = np.zeros((len(X),5))
    for x in range(0,len(X)):
        F[x,0] = len(X[x])
        F[x,1] = nr_numbers(X[x])
        F[x,2] = nr_vogals(X[x])
        F[x,3] = nr_accents(X[x])
        F[x,4] = 

    return F     

def mytraining(f,Y):
    
   
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
        if(s[i] in ['a','A','e','E','i','I','o','O','u', 'U'])
            x+=1
    return x

def nr_numbers(s):
    x = 0;
    for i in range(len(s)):
        if s[i] in ['0','1','2','3','4','5','6','7','8','9']:
            x+=1
    return x

def nr_accents(S):
    x = 0
    for i in range(len(s)):
        try:
            if s[i] > 128:
                x += 1
        except TypeError:
            x += 1
    return x