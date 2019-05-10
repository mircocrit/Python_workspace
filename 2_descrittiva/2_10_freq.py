# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019

@author: mirco
""STATISTICA DESCRITTIVA_con frequneze"""

import copy
import numpy as np
import math as mt
from scipy.stats.mstats import gmean


arr= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
freq= np.array([4,7,34,38,36,21,27,14,10,6,2,1])


""""0_tabella frequenze"""
k=copy.copy(arr)
Nk=copy.copy(freq)
print('Tabella frequenze')
print('k:  {}  {}  {}   {}   {}   {}  {}   {}   {}   {}   {}  {}  \t' .format(*k))
print('-----------------------------------')
print('Nk  {}  {}  {}  {}   {}   {}   {} {}   {}   {}   {}  {} \t'.format(*Nk))
Fk=[]
for i in range(0, len(k)):
    Fk.append(0)
    
Fk[0]=Nk[0]
for i in range(1, len(Nk)):
    Fk[i]=Nk[i]+Fk[i-1]
print('Fk  {}  {}  {}  {}   {}  {}  {}  {}   {}   {}   {}  {} \t'.format(*Fk))
print('------------------------------------')

pk=copy.copy(Nk)
max=Fk[len(freq)-1]
for i in range(0, len(Fk)):
    pk[i]= (pk[i]/ max)
print('pk  {:1.2f} {:1.2f} {:1.2f} {:1.2f}  {:1.2f}  {:1.2f}  {:1.2f} {:1.2f} {:1.2f}  {:1.2f}  {:1.2f}  {:1.2f} \t'.format(*pk))

fk=copy.copy(Fk)
for i in range(0, len(Fk)):
    fk[i]= (fk[i]/ max)
print('fk  {:1.2f} {:1.2f} {:1.2f} {:1.3f} {:1.2f}  {:1.2f}  {:1.2f} {:1.2f} {:1.2f}  {:1.2f}  {:1.2f}  {:1.2f}  \t\n'.format(*fk))


n=len(arr)
tot=np.sum(freq)

 
"1_media """
i=0
sum=0
while i<n:
    sum+=(arr[i]*freq[i])
    i=i+1    
med=(1/tot)*sum
print('Media:                {:1.2f}\t'.format(med))


"""2_varianza"""
"""_media con i quadrati"""
i=0
sumq=0
while i<n:
    sumq+=((arr[i]**2)*freq[i])
    i=i+1
sumq=(1/tot)*sumq

var=sumq-(med**2)
print('Varianza:             {:1.2f}\t'.format(var))


"""3_deviazione standard"""
devstdd=np.sqrt(var)
print('Deviazione standard:     {:1.2f}\t'.format(devstdd))


"""3.1_coefficiente di variazione"""
variaz=devstdd/np.abs(med)
print('Coefficiente di variazione:    {:1.2f}\t'.format(variaz))



"""5-mediana"""
print('Tot (pari):          {}\t'.format(tot))

mediana=((tot+1)/2)
print('Quantile mediana dispari:      {}\t'.format(mediana))
flag=0
for i in range(0, len(Fk)):
    if mediana<= Fk[i]:
        mediana=k[i]
        break
print('Mediana :      {:1.2f}\t'.format(mediana))




"""6-1_quartile"""
quartile_1= (tot+1)/4
flag=0
for i in range(0, len(Fk)):
    if quartile_1<= Fk[i]:
        quartile_1=k[i]
        break
print('1_quartile:          {}\t'.format(quartile_1))

"""6-3_quartile"""

quartile_3= 3* ((tot+1)/4)
flag=0
for i in range(0, len(Fk)):
    if quartile_3<= Fk[i]:
        quartile_3=k[i]
        break
print('3_quartile:          {}\t\n'.format(quartile_3))

