# -*- coding:utf-8 -*-

"""
@author : houzhuo
@file: UserCF2.py
@time: 17/11/15 下午9:00
"""

import pandas as pd
import math

'''unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('movieData/users.dat',sep='::',header = None,names = unames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movieData/movies.dat', sep='::', header=None, names=mnames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('movieData/ratings.dat', sep='::', header=None, names=rnames)

all_data = pd.merge(pd.merge(ratings,users),movies)
data = pd.DataFrame(data=all_data,columns = ['user_id','movie_id'])
data.to_csv('movieData/data.csv')
'''


def UserSimilarity():

    data = pd.read_csv('movieData/data.csv')
    X = data['user_id']
    Y = data['movie_id']

    item_users = dict()

    for i in range(X.count()):#100万条数据 从0到100208 这里代表行号
        user = X.iloc[i]
        item = Y.iloc[i]
        if item not in item_users:   #可以这样直接检查字典的key？不用items
            item_users[item] = set()  #添加集合
        item_users[item].add(user)    #{movie:set([1,3,4,5,7])}

    C = dict()
    N = dict()
    for i, users in item_users.items():  #别忘了items()
        for u in users:
            N.setdefault(u,0)
            N[u] += 1        #用户有过正反馈的集合
            C.setdefault(u,{})
            for v in users:
                if u == v:
                    continue
                C[u].setdefault(v,0)
                C[u][v] += 1 / math.log(1 + len(users))   #用户之间有过关联的矩阵

    #calculate final similarity matrix W
    W = dict()
    for u, related_users in C.items():
        for v, cuv in related_users:
            W[u][v] = cuv / math.sqrt(N[u] * N[v])
    return W


def Recommend(user, user_items, W, K):
    rank = dict()
    interacted_items = user_items  #此用户有过记录的商品
    for v, wuv in sorted(W[user].items(),reverse=True)[0:K]:  #和用户u兴趣最接近的K个用户v
        for i in user_items[v]:       #v的购物列表
            if i not in interacted_items:   #此用户没买过
                rank.setdefault(i,0)
            rank[i] += wuv
    return rank





def loadData():
    new_file = file('movieData/ui.txt','w')
    for line in open('movieData/ratings.dat','r'):
        line = line.strip('\n').split('::')
        new_file.writelines(line[0]+' '+line[1]+'\n')
    new_file.close()


if __name__ == '__main__':
    UserSimilarity()