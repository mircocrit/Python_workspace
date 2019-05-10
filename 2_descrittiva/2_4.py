# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019

@author: mirco
""STATISTICA DESCRITTIVA""

"""
import copy
import numpy as np
import math as mt
from scipy.stats.mstats import gmean


arrl=np.array([25,9,5,5,5,9,6,5,15,45,35,6,5,6,24,21,16,5,8,7,
               7,5,5,35,13,9,5,18,6,10,19,16,21,8,13,5,9,10,10,6,
               23,8,5,10,15,7,5,5,24,9,11,34,12,11,17,11,16,5,15,5,
               12,6,5,5,7,6,17,20,7,8,8,6,10,11,6,7,5,12,11,18,6,21,
               6,5,24,7,16,21,23,15,11,8,6,8,14,11,6,9,6,10])

'''0_trasformazione in array + freq'''
arrl.sort()


arr=list(set(arrl))
freq=[]
for i in range(0, len(arr)):
    freq.append(0)
j=0
for i in range(0,len(arrl)):
    if arrl[i] == arr[j]:
        freq[j]+=1
    else:
         j+=1
         freq[j]+=1
         
   
print ('array')
print (arr)
print ('frequenze')
print(freq)

"""0_tabella frequenze"""
k=copy.copy(arr)
Nk=copy.copy(freq)
print('Tabella frequenze')
print('k:  {}  {}  {}   {}  {}  {}  {} {}  {}  {}   {}  {}  {}  {} {}  {}  {}   {}  {}  {}  {}\t' .format(*k))
print('------------------------------------')
print('Nk  {}  {}  {}  {}  {}  {}   {} {}  {}  {}   {}  {}  {}  {} {}  {}  {}   {}  {}  {}  {}\t'.format(*Nk))
Fk=[]
for i in range(0, len(k)):
    Fk.append(0)
    
Fk[0]=Nk[0]
for i in range(1, len(Nk)):
    Fk[i]=Nk[i]+Fk[i-1]
print('Fk  {} {}  {} {} {}  {}  {} {}  {}  {}   {}  {}  {}  {} {}  {}  {}   {}  {}  {}  {}\t'.format(*Fk))
print('------------------------------------')
"""
pk=copy.copy(Nk)

for i in range(0, len(Nk)):
    pk[i]= pk[i]/Fk[len(freq)-1]    
print('pk  {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f}  {:1.3f}  {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f}  {:1.3f}  {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f}  {:1.3f}  {:1.3f}\t'.format(*pk))

fk=copy.copy(Fk)
for i in range(0, len(Fk)):
    fk[i]= fk[i]/ Fk[len(freq)-1]
print('fk  {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f}  {:1.3f}  {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f}  {:1.3f}  {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f}  {:1.3f}  {:1.3f}\t\n'.format(*fk))

"""
n=len(arr)
tot=np.sum(freq)


  
"""1_media """
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



"""4_range"""
print('Range: {:1.2f}\t\n'.format(arr[len(arr)-1]-arr[0]))


"""5-mediana"""

print('Tot (pari):          {}\t'.format(tot))

mediana1=(tot/2)
mediana2=((tot+2)/2)
for i in range(0, len(Fk)):
    if mediana1<= Fk[i]:
        mediana1=k[i]
        break
for i in range(0, len(Fk)):
    if mediana2<= Fk[i]:
        mediana2=k[i]
        break
mediana=((mediana1+mediana2)/2)
print('Mediana :      {:1.2f}\t'.format(mediana))




"""6-1_quartile"""
quartile_1_1= (tot)/4
quartile_1_2= (tot+2)/4
flag=0
for i in range(0, len(Fk)):
    if quartile_1_1<= Fk[i]:
        quartile_1_1=k[i]
        break
for i in range(0, len(Fk)):
    if quartile_1_2<= Fk[i]:
        quartile_1_2=k[i]
        break
quartile1= ((quartile_1_1+quartile_1_2)/2)
print('1_quartile:          {}\t'.format(quartile1))

"""6-3_quartile"""

quartile_3_1= 3*((tot)/4)
quartile_3_2= 3*((tot+2)/4)
for i in range(0, len(Fk)):
    if quartile_3_1<= Fk[i]:
        quartile_3_1=k[i]
        break
for i in range(0, len(Fk)):
    if quartile_3_2<= Fk[i]:
        quartile_3_2=k[i]
        break
quartile3= ((quartile_3_1+quartile_3_2)/2)
print('3_quartile:          {}\t\n'.format(quartile3))
