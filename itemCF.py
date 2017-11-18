# -*- coding:utf-8 -*-

"""
@author : houzhuo
@file: itemCF.py
@time: 17/11/17 下午11:58
"""

def ItemSimilarity():

    data = pd.read_csv('movieData/data.csv')
    X = data['user_id']
    Y = data['movie_id']