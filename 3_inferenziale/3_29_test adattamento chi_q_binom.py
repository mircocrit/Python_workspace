# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019

@author: mirco
""STATISTICA DESCRITTIVA_con frequneze"""

import copy
import numpy as np
import math as mt
import tavole
import scipy.special as bino

arr= np.array([0,1,2,3,4,5])
freq= np.array([8,37,62,56,34,3])
bin_n=5
bin_p=1/2
alfa=0.05
n=np.sum(freq)
print(n)

"""0_tabella frequenze"""
j_=copy.copy(arr)
Nj=copy.copy(freq)
print('Tabella frequenze')
print(' j  {}     {}     {}      {}     {}     {}\t' .format(*j_))
print('-----------------------------------')
print('Nj  {}     {}     {}     {}     {}       {}\t'.format(*Nj))

pj=[]
for i in range(0, len(Nj)):
    pj.append(0)

for j in range(0, len(Nj)):
    pj[j]= ((bino.binom(bin_n, j)) * (np.power(bin_p,j)) * (np.power(1-bin_p,bin_n-j)))
#print(pk)
print('pj  {:1.4f}  {:1.4f}  {:1.4f}  {:1.4f}  {:1.4f}  {:1.4f}\t'.format(*pj))

npj=[]
for i in range(0, len(Nj)):
    npj.append(0)
    
n=np.sum(freq)
for i in range(0, len(Nj)):
    npj[i]= (pj[i]*n)
print('npj  {:1.3f}  {:1.3f}   {:1.3f}   {:1.3f}  {:1.3f}  {:1.3f}\t\n'.format(*npj))
print('-----------------------------------------------------------')

n=len(arr)
tot=np.sum(freq)

 



K=[]#statistica di Pearson
for i in range(0, len(Nj)):
    K.append(0)

for k in range (0,len(Nj)):#npj
    K[k]=(np.power((Nj[k]-(npj[k])),2))/(npj[k])
 
Ko=np.sum(K)    
print('Mj  {:1.3f}  {:1.3f} {:1.3f}  {:1.3f}  {:1.3f}  {:1.3f}\t'.format(*K))
print('Ko  {:1.3f} \t\n'.format(Ko))

n=len(Nj)
print('1 Chi quadro 1-alfa')
print('n-1: {}\t'.format(n-1))
chialfa=(1-(alfa))
print('1-Alfa x:     {:1.3f}\t'.format(chialfa))
print('------------------------------------------')

i=n-2

if   chialfa==0.005:    j=0
elif chialfa==0.010:    j=1
elif chialfa==0.025:    j=2
elif chialfa==0.050:    j=3
elif chialfa==0.950:    j=4
elif chialfa==0.975:    j=5
elif chialfa==0.990:    j=6
elif chialfa==0.995:    j=7

chi= chiq[i,j]
print ('chi1-α x:     {:1.3f}\t'.format(chi))


if Ko<chi: 
      print('accetto Ho')
else: 
    print('rifiuto Ho')

