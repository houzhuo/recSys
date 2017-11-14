# coding=utf-8
import numpy as np
from sklearn.model_selection import train_test_split
import random
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import cross_val_score

'''
sklearn split
'''
iris = datasets.load_iris()
print iris.data.shape,iris.target.shape

X_train, X_test, Y_train, Y_test = train_test_split(iris.data,iris.target,test_size=0.4,random_state=0)
print X_train.shape


clf = svm.SVC(kernel='linear', C=1).fit(X_train,Y_train)
print clf.score(X_train,Y_train)


scores = cross_val_score(clf, iris.data, iris.target, cv=5)
print scores
print ("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(),scores.std()*2))

'''
normal split
'''

def SplitData(data,M,k,seed):
    test = []
    train = []
    random.seed(seed)
    for user, item in data:
        if random.randint(0,M) == k:
            test.append([user,item])
        else:
            train.append([user,item])
    return train,test

'''
Recall = R(u)^T(u) / T(u) 推荐的 交 用户喜欢的     R(u)对用户u推荐n个物品
Precision = R(u)^R(T) / R(u) 
'''

def Recall(train, test, N):
    hit = 0;
    all = 0;
    for user in train.keys():
        tu = test[user]
        rank = GetRecommendation(user,N)
        for item , pui in rank:
            if item in tu:
        all += len(tu) #喜欢的物品个数,每个用户n个物品
    return hit / (all * 1.0)
def Precision(train, test, N):
    hit = 0;
    all = 0;
    for user in train.keys():
        tu = test[user]
        rank = GetRecommendation(user,N)
        for item , pui in rank:
            if item in tu:
        all += N #对每个用户推荐N个物品
    return hit / (all * 1.0)