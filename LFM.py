# -*- coding:utf-8 -*-

"""
@author : houzhuo
@file: LFM.py
@time: 17/11/21 下午3:11
"""
import random

#随机采出热门但是没有行为的商品
def RandomSelectNegativeSample(self, items,items_pool):  #items是用户有过行为的集合
    ret = dict
    for i in items.keys:
        ret[i] = 1
    n = 0
    for i in range(0, len(items) * 3):
        item = items_pool[random.randint(0, len(items_pool) - 1)]    #itemspool维护的是候选物品的列表
        if item in ret:
            continue
        ret[item] = 0      #没有过行为的， 并且推荐的就设为0
        n += 1
        if n > len(items):
            break
    return ret
