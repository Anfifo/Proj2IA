from sklearn import neighbors, datasets
from sklearn import tree
from sklearn.metrics import accuracy_score

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

#Training Set
X = np.zeros((22,1))
X[:,0] = np.arange(0,11,.5)
noisesigma = 2.5
Y = np.ravel((2-(X-5)**2 + noisesigma * np.random.randn(22, 1))>0)

#Testing Set
Xp = np.zeros((110,1))
Xp[:,0] = np.arange(0,11,.1)


#KNeighborsClassifier
n_neighbors = 2
#weights = 'distance'
weights = 'uniform'
clfKNNC = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
clfKNNC.fit(X, Y)

#KNeighborsClassifier
n_neighbors = 3
weights = 'distance'
clfKNNC2 = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
clfKNNC2.fit(X, Y)


min_samples_split = 8
clftree = tree.DecisionTreeClassifier(min_samples_split=min_samples_split)
clftree = clftree.fit(X, Y)

YpKNNC = clfKNNC.predict(Xp)
YpKNNC2 = clfKNNC2.predict(Xp)
Yptree = clftree.predict(Xp)

accKNNC = accuracy_score(Y, clfKNNC.predict(X))
accKNNC2 = accuracy_score(Y, clfKNNC2.predict(X))
acctree = accuracy_score(Y, clftree.predict(X))

print("KNNC: " + str(accKNNC))
print("KNNC2: " + str(accKNNC2))
print("Tree: " + str(acctree))

#clf.predict_proba(Xp)
plt.plot(X,Y,'x',label='data')
#plt.show()
plt.plot(Xp,YpKNNC,'c',label='kNN2')
#plt.show()
plt.plot(Xp,YpKNNC2,'b',label='kNN3')
#plt.show()
plt.plot(Xp,Yptree,'r',label='DecisionTree')
plt.legend( loc = 1 )
#plt.show()

