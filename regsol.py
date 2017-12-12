#Grupo 2: André Fonseca (84698), Leonor Loureiro (84736)
import numpy as np
from sklearn import datasets, tree, linear_model;
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
import timeit

def mytraining(X,Y):
    

    reg = KernelRidge(alpha=0.001, gamma=0.1, kernel='rbf')
    reg.fit(X,Y)
   
    return reg
    
def mytrainingaux(X,Y,par):
    reg.fit(X,Y)
                
    return reg


def myprediction(X,reg):

    Ypred = reg.predict(X)

    return Ypred
