# -*- coding:utf-8 -*-

"""
@author : houzhuo
@file: itemCF.py
@time: 17/11/17 下午11:58
"""
import pandas as pd
import math

def ItemSimilarity():

    data = pd.read_csv('movieData/data.csv')
    X = data['user_id']
    Y = data['movie_id']
    user_item = dict()

    for i in range(X.count()):
        user = X.iloc[i]
        item = Y.iloc[i]
        if user not in user_item:
            user_item[user] = set()
        user_item[user].add(item)


    C = dict()
    N = dict()
    for users, items in user_item.items():
        for u in items:
            N.setdefault(u,0)
            N[u] += 1
            C.setdefault(u,{})
            for v in items:
                if u == v:
                    continue
                C[u].setdefault(v,0)
                C[u][v] += 1

    W = dict()
    for u , relatedItem in user_item.items():
        for v, cuv in relatedItem:
            W[u][v] = cuv / math.sqrt(N[u]*N[v])
    return W

def Recommendation(user, user_items, W, K):
    rank = dict()
    related_items = user_items[user_items]
    for i in user_items[user]:
        for j, wuv in sorted(W[i].items(),reverse=True)[0:K]:
            if j not in related_items:
                rank.setdefault(i, 0)
                rank[i] += wuv
    return rank
