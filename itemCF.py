# -*- coding:utf-8 -*-

"""
@author : houzhuo
@file: itemCF.py
@time: 17/11/17 下午11:58
"""
import pandas as pd
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
