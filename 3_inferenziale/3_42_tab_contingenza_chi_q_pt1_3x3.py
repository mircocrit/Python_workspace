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

arr= np.array([[30,68,10],
              [61,78,21],
              [98,43,21]])
r=3
c=3
alfa=0.05
#print(n)

"""0_tabella frequenze"""
j_=copy.copy(arr)

print('Tabella frequenze')
for i in range (0,3):    
    print('    {}      {}      {}     \n ' .format(*j_[i]))
print('-----------------------------------')
#print('Nj  {}     {}     {}     {}   \t'.format(*Nj))

pj=copy.copy(arr)

print('Margx:')
margx=np.array([0,0,0])
for i in range (0,len(margx)): 
    sum=0
    for j in range (0,len(margx)):
        sum+=j_[j][i]       
    margx[i]=sum
    sum=0
print('    {}      {}      {}     \n ' .format(*margx))

print('Margy:')
margy=np.array([0,0,0])
for i in range (0,len(margy)):
        margy[i]=np.sum(j_[i])
print('      {}\n\n      {}\n\n      {}\n ' .format(*margy))

tot=np.sum(margx)
print(tot)

print('\nTabella npjqk')
npjqk=np.array([[0.000,0.000,0.000],
                [0.000,0.000,0.000],
                [0.000,0.000,0.000]])




for i in range (0,len(margx)): 
    for j in range (0,len(margx)):
        npjqk[i,j]=(margx[j]*margy[i])/tot
 

for i in range (0,3):    
    print('    {:1.3f}      {:1.3f}      {:1.3f}     \n ' .format(*npjqk[i]))
    
    
print('Tabella Pearson')
Pearson=np.array([[0.0000,0.0000,0.0000],
                [0.0000,0.0000,0.0000],
                [0.0000,0.0000,0.0000]])

for i in range (0,len(margx)): 
    for j in range (0,len(margx)):#usare _j  npjqk
        Pearson[i,j]=np.power((j_[i][j]-npjqk[i][j]),2)/npjqk[i][j]
        
for i in range (0,3):    
    print('    {:1.3f}      {:1.3f}      {:1.3f}     \n ' .format(*Pearson[i]))

Ko=0    
for i in range (0,3): 
    Ko+=np.sum(Pearson[i])
print('Ko  {:1.3f} \t\n'.format(Ko))

print('**************************************')
print('Chi quadro 1-alfa:')
print('(r-1)x(s-1): {}x{} \t'.format(r-1,c-1))
chialfa=(1-(alfa))
print('1-Alfa:     {:1.3f}\t'.format(chialfa))
print('------------------------------------------')

i=(r-1)*(c-1)-1

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
