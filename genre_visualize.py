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

corpus2 = open('outw.txt', 'r', encoding='utf-8')
corpus2 = corpus2.read()
outw = re.split(r'(?:[.]\s*){3}|[.?!]+', corpus2)


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

dataa = f2(f1(outa))
datas = f2(f1(outs))
dataw = f2(f1(outw))



def prep(c):
    corpus1 = open(c, 'r', encoding='utf-8')
    corpus1 = corpus1.read()
    outs = re.split(r'(?:[.]\s*){3}|[.?!]+', corpus1)
    s = []
    for i in outs:
        m = re.findall('{(.*?)=', i)
        s.append(m)

    for y in s:
        if [] in s:
            s.remove([])

    ss = []

    for y in s:
        ss.append(' '.join(y))

    return ss


def counts(sentence):
    length = len([letter for letter in sentence if letter not in ' '])
    different = len(set([letter for letter in sentence if letter not in ' ']))
    vowels = len([letter for letter in sentence if letter in 'уеыаоэёяию'])
    return length, different, vowels


def countw(sentence):
    words = sentence.split()
    lengthmed = np.median([len(word) for word in words])
    lengthmean = round(np.mean([len(word) for word in words]))
    vowels = []
    for word in words:
        v = 0
        for l in word:
            if l in 'уеыаоэёяию':
                v += 1
        vowels.append(v)
    vowels = np.median(vowels)
    return lengthmed, lengthmean, vowels


c1data = []
c2data = []


for i in prep('outa.txt'):
    c = []
    for u in counts(i):
        c.append(u)
    for y in countw(i):
        c.append(y)
    c.append(len(i.split()))
    c1data.append(c)

for i in prep('outs.txt'):
    c = []
    for u in counts(i):
        c.append(u)
    for y in countw(i):
        c.append(y)
    c.append(len(i.split()))
    c2data.append(c)


anna_data = []
sonet_data = []


for t in range(len(dataa)):
    anna_data.append(c1data[t]+dataa[t])

for t in range(len(datas)):
    sonet_data.append(c2data[t]+datas[t])


data = np.vstack((anna_data, sonet_data))
N = len(anna_data)
p = mlab.PCA(data, True)
a = p.Wt[0]
di = {}

di[a[0]] = 'A'
di[a[1]] = 'S'
di[a[2]] = 'V'
di[a[3]] = 'ADV'
di[a[4]] = 'SPRO'
di[a[5]] = 'len_in_letters'
di[a[6]] = 'len_in_diff_letters'
di[a[7]] = 'len_in_vowels'
di[a[8]] = 'median_length_of_words'
di[a[9]] = 'mean_length_of_words'
di[a[10]] = 'median_vowels_in_words'
di[a[11]] = 'length_of_sent_in_words'
d1 = np.absolute(a)

d1 = np.sort(d1)[::-1]


impkeys = []
for y in range(3):
    for u in di:
        if np.absolute(u) == d1[y]:
            print(di[u], u)
            impkeys.append(u)



dlist = []
for k in di:
    dlist.append(k)

a1 = []
for u in a:
    a1.append(u)

ind0 = a1.index(dlist[0])
ind1 = a1.index(dlist[1])
ind2 = a1.index(dlist[2])


plt.plot(p.Y[:N, ind0], p.Y[:N, ind1], 'sb', p.Y[:N, ind0], p.Y[:N, ind1], 'xr')
plt.savefig('OUT1.png')
plt.clf()
plt.plot(p.Y[:N, ind1], p.Y[:N, ind2], 'sb', p.Y[:N, ind1], p.Y[:N, ind2], 'xr')
plt.savefig('OUT2.png')
plt.clf()
plt.plot(p.Y[:N, ind0], p.Y[:N, ind2], 'sb', p.Y[:N, ind0], p.Y[:N, ind2], 'xr')
plt.savefig('OUT3.png')
plt.clf()
