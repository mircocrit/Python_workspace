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
def gauss(x):
    if x<0:
        print(' 1- fi({:1.3f})  \n'.format(x))
    else:
        print(' fi({:1.3f})  \n'.format(x))
        """
       row=int(-x*10)
       dec=int(-x*100)-((int(-x*10))*10)
       #print(row)
       dec=int(dec)
       #print(dec)
       qnormale=1-normstd[row,dec]   
    else:#x>0       
        row=int(x*10)
        dec=int(x*100)-((int(x*10))*10)
        #print(row)      
        dec=int(dec)
        #print(dec)
        qnormale=1-normstd[row,dec]
    return qnormale
    """


rang=np.array([-1000,135,140,145,150,1000])
freq=[5,10,33,24,12]
alfa=0.05
med=143.8
var=36.0
print('---------------------------------------------------')
j_=copy.copy(rang)
Nj=copy.copy(freq)


print('Tabella frequenze')
print(' j  {}     {}     {}      {}     {}      {}\t' .format(*j_))
print('-----------------------------------')
print('Nj  {}     {}     {}     {}      {}    \t'.format(*Nj))
print('')
print('***********************************************')

#NORMALE 1,1
pj=[]
for i in range(0, len(Nj)):
    pj.append(0)

for j in range(0, len(Nj)):

    if j_[j]==-1000:
        
       part0=(j_[j+1]-med)/np.sqrt(var)
       print('1) 1 - fi({:1.3f})  \n'.format(np.abs(part0)))

    elif j_[j+1]==1000:
       print('2) 1- fi({:1.3f})  \n'.format((j_[j]-med)/np.sqrt(var)))
        
    else: #non infinito     
        part1=((j_[j+1]-med)/np.sqrt(var))
        part0=((j_[j]-med)/np.sqrt(var))
        #print(part0)
        #print(part1)
        if part1>=0 and part0<0:
            print('3.1) fi({:1.3f}) - (1-fi({:1.3f}))  \n'.format(np.abs(part1),part0))
               
        elif part1<0 and part0>=0:
            print('3.2) (1-fi{:1.3f}) -  {:1.3f}  \n'.format(part1,np.abs(part0)))
               
        elif part1>=0 and part0>=0:
            print('3.3) fi({:1.3f}) - fi({:1.3f})  \n'.format(part1,part0))
               
        else: # part1<0 and part2<0
            print('3.4)  (1-fi({:1.3f})) - (1-fi({:1.3f}))  \n'.format(np.abs(part1),np.abs(part0)))
            
provv=[1-0.92922,                   #0.071
      (1-0.73565) -  (1-0.92785),   #0.192
      (0.57926) - (1-0.73565),      #0.316,
       0.84849 - (0.57926),         #0.270,
       1-0.84849]                   #0.151
       
print('-------------------------------------------------')
for j in range(0, len(Nj)):
    pj[j]=provv[j]
print('pj  {:1.4f}  {:1.4f}  {:1.4f}  {:1.4f}  {:1.4f}\t'.format(*pj))
print('')

npj=[]
for i in range(0, len(Nj)):
    npj.append(0)
    
n=np.sum(freq)
for i in range(0, len(Nj)):
    npj[i]= (pj[i]*n)
print('npj  {:1.3f}  {:1.3f}   {:1.3f} {:1.3f}  {:1.3f} \t\n'.format(*npj))
print('-----------------------------------------------------------')



K=[]#statistica di Pearson
for i in range(0, len(Nj)):
    K.append(0)

for k in range (0,len(Nj)):#npj
    K[k]=(np.power((Nj[k]-(npj[k])),2))/(npj[k])
 
Ko=np.sum(K)    
print('Mj  {:1.4f}  {:1.4f} {:1.4f} {:1.4f} {:1.4f}   \t'.format(*K))
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

i=n-2-2

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

