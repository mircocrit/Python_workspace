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
freq= np.array([822,804,300,67,7,0])
bin_n=5
bin_p=1/6
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
print('pj  {:1.5f}  {:1.5f}  {:1.5f}  {:1.5f}  {:1.5f}  {:1.5f}\t'.format(*pj))

npj=[]
for i in range(0, len(Nj)):
    npj.append(0)
    
n=np.sum(freq)
for i in range(0, len(Nj)):
    npj[i]= (pj[i]*n)
print('npj  {:1.3f}  {:1.3f}   {:1.3f}   {:1.3f}  {:1.3f}  {:1.3f}\t\n'.format(*npj))
print('*******************************************************************+')

n=len(arr)
tot=np.sum(freq)


j2=[]
for i in range(0, len(Nj)-1):
    j2.append(0)
#print(len(j_))
#print( len(j2))
qj=[]
for i in range(0, len(Nj)-1):
    qj.append(0)
    
nqj=[]
for i in range(0, len(Nj)-1):
    nqj.append(0)
    
Mj=[]
for i in range(0, len(Nj)-1):
    Mj.append(0)
#Mj=copy.copy(freq)    

k=0#nqj
j=0#npj
while k<len(Nj)-1:#npj
#for j in range(0, len(Nj)-1):
   if npj[k]>=5:
       j2[j]=j_[k]  #range
       Mj[j]=Nj[k]  #frequenze
       qj[j]=pj[k]  #freq compattate
       
       nqj[j]=npj[k]    #prodotto per n con freq compattate
       #print('if  {:1.0f}   {:1.3f}   {:1.0f} '.format(j,qj[j],k))
       k=k+1
       j=j+1
       
   else:#npj[j]<5:
       
       j2[j]= ((j+1)+j)/2    #range j2
       Mj[j]= Nj[k+1]+Nj[k]  #frequenze Mj
       qj[j]= pj[k+1]+pj[k]  #freq compattate qj
       
       nqj[j]=npj[k+1]+npj[k]      #prodotto per n con freq compattate nqj
       #print('else  {:1.0f}   {:1.3f}   {:1.0f} '.format(j,qj[j],k))
       k=k+2
       j=j+1
if npj[k]<5:
     j2[j-1]= ((j-1)+j)/2    #range j2
     Mj[j-1]= Nj[k-1]+Nj[k]  #frequenze Mj
     qj[j-1]= pj[k-1]+pj[k]  #freq compattate qj
     nqj[j-1]= npj[k-1]+npj[k]

print('j2   {:1.0f}      {:1.0f}      {:1.0f}      {:1.0f}      {:1.0f}  \t'.format(*j2))       
print('qj  {:1.5f}  {:1.5f} {:1.5f}  {:1.5f}  {:1.5f}  \t'.format(*qj))
print('nqj  {:1.4f}   {:1.4f}  {:1.4f}   {:1.4f}   {:1.4f}    \t'.format(*nqj))
print('Mj  {:1.0f}     {:1.0f}    {:1.0f}     {:1.0f}     {:1.0f}\t'.format(*Mj))
print('--------------------------------------------------------')
print('')



K=[]#statistica di Pearson
for i in range(0, len(Nj)-1):
    K.append(0)

for k in range (0,len(Nj)-1):#npj
    print
    K[k]=(np.power((Mj[k]-(nqj[k])),2))/(nqj[k])
 
Ko=np.sum(K)    
print('Kj  {:1.4f}  {:1.5f} {:1.4f}  {:1.4f}  {:1.4f}\t'.format(*K))
print('Ko  {:1.3f} \t\n'.format(Ko))

n=len(j2)
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

