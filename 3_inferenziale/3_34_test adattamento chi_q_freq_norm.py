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


"""4_Gauss"""
def gauss_function(x):
    if x>=100:
        return 1
    elif x<=-100:
        return 0
    elif x<0 and x>-100:
       qnormale=1-normstd[int(-x*10),0] 
    else:
        qnormale=normstd[int(x*10),0]
    return qnormale


arrl=np.array([-3.601,1.064,3.370,1.535,1.017,
               1.933,3.100,-0.569,1.141,1.815,
               2.267,0.195,-0.506,-0.167,-2.936,
               -0.211,-0.659,-0.375,0.024,2.765])
arrl.sort()
rang=np.array([-1000,0,2,1000])#freq= 
alfa=0.05
med=1
var=2

print('---------------------------------------------------')

'''0_trasformazione in array + freq'''


#arr=list(set(arrl))
freq=[]
for i in range(0, len(rang)-1):
    freq.append(0)
    
j=0
for i in range(0,len(arrl)):
    if (arrl[i] <= rang[j+1]) and (arrl[i] >= rang[j]):
        freq[j]+=1
    else:
         j+=1
         freq[j]+=1
    
   
print ('range')
for i in range(0, len(rang)-1):
    print('[{},{}] '.format(rang[i],rang[i+1]),end =" ")
print ('frequenze')
print(freq)

"""0_tabella frequenze"""
j_=copy.copy(rang)
Nj=copy.copy(freq)


print('Tabella frequenze')
print(' j  {}     {}     {}      {}     \t' .format(*j_))
print('-----------------------------------')
print('Nj  {}     {}     {}         \t'.format(*Nj))
print('')
print('***********************************************')

#NORMALE 1,1
pj=[]
for i in range(0, len(Nj)):
    pj.append(0)

for j in range(0, len(Nj)):
    pj[j]= (gauss_function((j_[j+1]-med)/var)-gauss_function((j_[j]-med)/var))
print('pj  {:1.3f}  {:1.3f}  {:1.3f}   \t'.format(*pj))
print('***********************************************')




npj=[]
for i in range(0, len(Nj)):
    npj.append(0)
    
n=np.sum(freq)
for i in range(0, len(Nj)):
    npj[i]= (pj[i]*n)
print('npj  {:1.1f}  {:1.1f}   {:1.1f}  \t\n'.format(*npj))
print('-----------------------------------------------------------')



K=[]#statistica di Pearson
for i in range(0, len(Nj)):
    K.append(0)

for k in range (0,len(Nj)):#npj
    K[k]=(np.power((Nj[k]-(npj[k])),2))/(npj[k])
 
Ko=np.sum(K)    
print('Mj  {:1.3f}  {:1.3f} {:1.3f}   \t'.format(*K))
print('Ko  {:1.3f} \t\n'.format(Ko))




print('')
print('*********************Test del Chi Quadro**************************')
##1)

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

