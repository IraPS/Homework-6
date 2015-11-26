__author__ = 'IrinaPavlova'

'''Только выводит три самых значимых признака для текста'''

import numpy as np
import re
from matplotlib import pyplot as plt
from matplotlib import mlab
from collections import Counter


corpus1 = open('outs.txt', 'r', encoding='utf-8')
corpus1 = corpus1.read()
outs = re.split(r'(?:[.]\s*){3}|[.?!]+', corpus1)

corpus2 = open('outa.txt', 'r', encoding='utf-8')
corpus2 = corpus2.read()
outa = re.split(r'(?:[.]\s*){3}|[.?!]+', corpus2)


def f1(t):
    all1 = []
    for h in t:
        p = []
        for i in h.split():
            pos = re.findall('{.*?=([a-zA-Z]+)', i)
            if len(pos) is not 0:
                p.append(pos[0])
        if p != []:
            all1.append(Counter(p))
    return all1


def f2(l):
    res1 = []
    for k in l:
        resk = []
        if 'A' in k:
            resk.append(k['A'])
        else:
            resk.append(0)
        if 'S' in k:
            resk.append(k['S'])
        else:
            resk.append(0)
        if 'V' in k:
            resk.append(k['V'])
        else:
            resk.append(0)
        if 'ADV' in k:
            resk.append(k['ADV'])
        else:
            resk.append(0)
        if 'SPRO' in k:
            resk.append(k['SPRO'])
        else:
            resk.append(0)
        res1.append(resk)
    return res1

anna_data = f2(f1(outa))

anna_data = np.array(anna_data)
r = mlab.PCA(anna_data, True)
r = r.Wt
a = []
dic = {}

for d in r:
    a.append(d[0])

a = np.absolute(a)

dic[a[0]] = 'A'
dic[a[1]] = 'S'
dic[a[2]] = 'V'
dic[a[3]] = 'ADV'
dic[a[4]] = 'SPRO'


a = np.sort(a)[::-1]
for y in range(3):
    print(dic[a[y]])


