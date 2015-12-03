__author__ = 'IrinaPavlova'

import numpy as np
import re
from matplotlib import pyplot as plt
from matplotlib import mlab


corpus1 = open('c1.txt', 'r', encoding='utf-8')
corpus2 = open('c2.txt', 'r', encoding='utf-8')
corpus1 = corpus1.read()
corpus2 = corpus2.read()
s1 = re.split(r'(?:[.]\s*){3}|[.?!]+', corpus1)
print(s1)
s2 = re.split(r'(?:[.]\s*){3}|[.?!]+', corpus2)
if '' in s1:
    del s1[s1.index('')]
if '\n' in s1:
    del s1[s1.index('\n')]
if '' in s2:
    del s2[s2.index('')]
if '\n' in s2:
    del s2[s2.index('\n')]


def counts(sentence):
    length = len([letter for letter in sentence if letter not in ' '])
    different = len(set([letter for letter in sentence if letter not in ' ']))
    vowels = len([letter for letter in sentence if letter in 'уеыаоэёяию'])
    return length, different, vowels


def countw(sentence):
    words = sentence.split()
    length = np.median([len(word) for word in words])
    vowels = []
    for word in words:
        v = 0
        for l in word:
            if l in 'уеыаоэёяию':
                v += 1
        vowels.append(v)
    vowels = np.median(vowels)
    return length, vowels

c1data = []
c2data = []

for i in s1:
    c = []
    for u in counts(i):
        c.append(u)
    for y in countw(i):
        c.append(y)
    c1data.append(c)

for i in s2:
    c = []
    for u in counts(i):
        c.append(u)
    for y in countw(i):
        c.append(y)
    c2data.append(c)


c1data = np.array(c1data)
c2data = np.array(c2data)


data = np.vstack((c1data, c2data))
p = mlab.PCA(data, True)
N = len(c1data)

plt.plot(p.Y[:N, 0], p.Y[:N, 1], 'og', p.Y[N:, 0], p.Y[N:, 1], 'sb')

print(p.s)
print(p.Wt)

plt.show()
