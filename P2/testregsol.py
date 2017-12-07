# -*- coding: utf-8 -*-
import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
import timeit
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

import regsol

tres = [.3, 800]    
for ii,test in enumerate(["regress.npy", "regress2.npy"]):
    print("Testing " + test)
    
    X,Y,Xp,Yp = np.load(test)
    
    par = [{'kernel': ['rbf','polynomial'], 'gamma': [1.0,0.1,0.01,0.001], 'alpha':[1.0,0.1,0.01,0.001]}]
    
    #reg = regsol.mytrainingaux(X,Y,par)

    par2 = [{'kernel': ['rbf'], 'C': [0.1,1e0,1e1,1e2,1e3,1e4,1e5,1e6], 'gamma':[0.0001,0.001,0.01,0.1,1]}]
    #reg = regsol.mytrainingaux2(X,Y,par2)
    
    reg = regsol.mytraining(X,Y)
  
    Ypred = regsol.myprediction(Xp,reg)
    print(-cross_val_score( reg, X, Y.ravel(), cv = 5, scoring = 'neg_mean_squared_error').mean(),"\n")
    if -cross_val_score( reg, X, Y.ravel(), cv = 5, scoring = 'neg_mean_squared_error').mean() < tres[ii]:
        print("Erro dentro dos limites de tolerância. OK\n")
    else:
        print("Erro acima dos limites de tolerância. FAILED\n")    
    plt.figure()
    plt.plot(Xp,Yp,'g.',label='datatesting')
    plt.plot(X,Y,'k+',label='datatrain')
    plt.plot(Xp,Ypred,'m',label='linregres1')
    plt.legend( loc = 1 )
    plt.show()


