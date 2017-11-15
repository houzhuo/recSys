# -*- coding:utf-8 -*-

"""
@author : houzhuo
@file: UserCF2.py
@time: 17/11/15 下午9:00
"""

import pandas as pd

unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('movieData/users.dat',sep='::',header = None,names = unames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movieData/movies.dat', sep='::', header=None, names=mnames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('movieData/ratings.dat', sep='::', header=None, names=rnames)

all_data = pd.merge(pd.merge(ratings,users),movies)
data = pd.DataFrame(data=all_data,columns = ['user_id','movie_id'])
data.to_csv('movieData\data.csv')

