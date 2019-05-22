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


arrl=np.array([0.44,0.37,0.87,1.73,-0.41,2.84,1.40,-0.17,0.29,1.59,#arr=
               0.39,2.39,1.68,-0.05,1.01,1.17,0.62,2.83,0.73,0.91,
               0.31,-0.92,2.28,0.74,1.02,0.70,2.06,2.56,0.94,2.56,
              -0.34,1.40,1.42,-0.09,2.17,1.83,1.80,-0.14,1.40,0.91])
arrl.sort()
rang=np.array([-1000,0,1,2,1000])#freq= 
alfa=0.05
var=1
med=1


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
print(' j  {}     {}     {}      {}     {}\t' .format(*j_))
print('-----------------------------------')
print('Nj  {}     {}     {}     {}     \t'.format(*Nj))
print('')
print('***********************************************')

#NORMALE 1,1
pj=[]
for i in range(0, len(Nj)):
    pj.append(0)

for j in range(0, len(Nj)):
    pj[j]= (gauss_function((j_[j+1]-med)/var)-gauss_function((j_[j]-med)/var))
print('pj  {:1.3f}  {:1.3f}  {:1.3f}  {:1.3f} \t'.format(*pj))
print('***********************************************')




npj=[]
for i in range(0, len(Nj)):
    npj.append(0)
    
n=np.sum(freq)
for i in range(0, len(Nj)):
    npj[i]= (pj[i]*n)
print('npj  {:1.1f}  {:1.1f}   {:1.1f}   {:1.1f}\t\n'.format(*npj))
print('-----------------------------------------------------------')

"""
n=len(arr)
tot=np.sum(freq)


j2=[]
for i in range(0, len(Nj)):
    j2.append(0)
#print(len(j_))
#print( len(j2))
qj=[]
for i in range(0, len(Nj)):
    qj.append(0)
    
nqj=[]
for i in range(0, len(Nj)):
    nqj.append(0)
    
Mj=[]
for i in range(0, len(Nj)):
    Mj.append(0)
#Mj=copy.copy(freq)    

k=0#nqj
j=0#npj
while k<len(Nj):#npj
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
      

print('j2   {:1.0f}      {:1.0f}      {:1.0f}      {:1.0f}      {:1.0f}\t'.format(*j2))       
print('qj  {:1.3f}  {:1.3f} {:1.3f}  {:1.3f}  {:1.3f} \t'.format(*qj))
print('nqj  {:1.1f}   {:1.1f}  {:1.1f}   {:1.1f}   {:1.1f} \t'.format(*nqj))
#print('Mj  {:1.0f}     {:1.0f}    {:1.0f}     {:1.0f}     {:1.0f} \t'.format(*Mj))
print('--------------------------------------------------------')
 
"""


K=[]#statistica di Pearson
for i in range(0, len(Nj)):
    K.append(0)

for k in range (0,len(Nj)):#npj
    K[k]=(np.power((Nj[k]-(npj[k])),2))/(npj[k])
 
Ko=np.sum(K)    
print('Mj  {:1.3f}  {:1.3f} {:1.3f}  {:1.3f}  \t'.format(*K))
print('Ko  {:1.3f} \t\n'.format(Ko))

#UNIFORME -1,3
pj2=[]
for i in range(0, len(Nj)):
    pj2.append(0)

for j in range(0, len(Nj)):
    pj2[j]=1/len(Nj)
print('pj2  {:1.3f}  {:1.3f}  {:1.3f}  {:1.3f} \t'.format(*pj2))
print('')



print('***********************************************')
print('')

npj2=[]
for i in range(0, len(Nj)):
    npj2.append(0)
    
n=np.sum(freq)
for i in range(0, len(Nj)):
    npj2[i]= (pj2[i]*n)
print('npj2  {:1.1f}  {:1.1f}   {:1.1f}   {:1.1f}\t\n'.format(*npj2))
print('-----------------------------------------------------------')

K2=[]#statistica di Pearson
for i in range(0, len(Nj)):
    K2.append(0)

for k in range (0,len(Nj)):#npj
    K2[k]=(np.power((Nj[k]-(npj2[k])),2))/(npj2[k])
 
Ko2=np.sum(K2)    
print('Mj2  {:1.3f}  {:1.3f} {:1.3f}  {:1.3f}  \t'.format(*K2))
print('Ko2  {:1.3f} \t\n'.format(Ko2))



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

#2)

if Ko2<chi: 
      print('accetto Ho (Ko2)')
else: 
    print('rifiuto Ho (Ko2)')