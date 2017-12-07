import numpy as np
from sklearn import datasets, tree, linear_model, svm;
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import timeit

def mytraining(X,Y):
    
    #reg = svm.SVR(kernel='rbf',C=1000,gamma=0.1)
    reg = KernelRidge(alpha=0.001, coef0=1, degree=3, gamma=0.1, kernel='rbf')
    reg.fit(X,Y.ravel())
   
    return reg
    
def mytrainingaux(X,Y,par):
    reg = GridSearchCV(KernelRidge(), cv = 5, param_grid = par, scoring =  'neg_mean_squared_error')
    reg.fit(X,Y)
    print("\nBest score: ", reg.best_score_)
    print("\nBest estimator: ", reg.best_estimator_)

    print("\nGrid scores: ")

    means = reg.cv_results_['mean_test_score']
    stds = reg.cv_results_['std_test_score']

    for mean, std, params in zip(means, stds, reg.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r"
              % (mean, std * 2, params))
    for mean, std, params in zip(means, stds, reg.cv_results_['params']):
        print("%0.3f"
              % (mean))
                
    return reg

def mytrainingaux2(X,Y,par):
    reg = GridSearchCV(svm.SVR(), cv = 5, param_grid = par, scoring =  'neg_mean_squared_error')
    reg.fit(X,Y.ravel())
    print("\nBest score: ", reg.best_score_)
    print("\nBest estimator: ", reg.best_estimator_)
    
    print("\nGrid scores: ")

    means = reg.cv_results_['mean_test_score']
    stds = reg.cv_results_['std_test_score']

    for mean, std, params in zip(means, stds, reg.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r"
              % (mean, std * 2, params))
    for mean, std, params in zip(means, stds, reg.cv_results_['params']):
        print("%0.3f"
              % (mean))

    return reg

def myprediction(X,reg):

    Ypred = reg.predict(X)

    return Ypred
