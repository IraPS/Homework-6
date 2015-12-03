__author__ = 'IrinaPavlova'

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


sonet_data = f2(f1(outs))
anna_data = f2(f1(outa))


data = np.vstack((anna_data, sonet_data))
p = mlab.PCA(data, True)
print(p.s)
print(p.Wt)
N = len(anna_data)
plt.plot(p.Y[:N, 0], p.Y[:N, 1], 'og', p.Y[N:, 0], p.Y[N:, 1], 'sb')
plt.show()

'''
ОТВЕТ: да, при такой ^ комбинации признаков, один текст на 70% (визуально) находится слева, а другой -- справа
'''

