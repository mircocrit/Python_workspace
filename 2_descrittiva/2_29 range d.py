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


arrl=np.array([0.40,0.78,0.91,1.06,1.25,1.31,1.33,1.40,1.53,1.58,
               1.65,1.77,1.85,1.92,2.03,2.07,2.15,2.39,2.66,2.87,
               2.98,3.14,3.15,3.16,3.66,3.71,3.82,4.59,4.83,5.67,
               5.78,5.99,6.39,6.59,6.81,7.93,8.22])
rang=np.array([0, 1, 2, 3, 4, 6, 8, 10])

'''0_trasformazione in array + freq'''
##arr=list(set(arrl))
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


"""0_tabella frequenze"""
k=copy.copy(rang)
Nk=copy.copy(freq)
print('Tabella frequenze')

print('k:{} {} {} {}  {} {} {}\t' .format(*k))

print('------------------------------------')
print('Nk   {}   {}   {}   {}   {}    {}   \t'.format(*Nk))
Fk=[]
for i in range(0, len(k)):
    Fk.append(0)
    
Fk[0]=Nk[0]
for i in range(1, len(Nk)):
    Fk[i]=Nk[i]+Fk[i-1]
print('Fk   {}   {}   {}   {}   {} {}  \t'.format(*Fk))
print('------------------------------------')

pk=copy.copy(Nk)

for i in range(0, len(Nk)):
    pk[i]= pk[i]/Fk[len(freq)-1]    
print('pk  {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f}\t'.format(*pk))

fk=copy.copy(Fk)
for i in range(0, len(Fk)):
    fk[i]= fk[i]/ Fk[len(freq)-1]
print('fk  {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f}\t\n'.format(*fk))


n=len(arrl)
tot=np.sum(freq)

  
"""1_media """
i=0
sum=0
while i<n:
    sum+=arrl[i]
    i=i+1
med=(1/n)*sum
print('Media:                {:1.2f}\t'.format(med))


"""2_range"""
print('Range:                {:1.2f}\t\n'.format(arrl[len(arrl)-1]-arrl[0]))


"""3-mediana"""
print('Tot (dispari):          {}\t'.format(tot))

mediana=((tot+1)/2)
print('Quantile mediana dispari:      {}\t'.format(mediana))
flag=0
for i in range(0, len(Fk)):
    if mediana<= Fk[i]:
        mediana=k[i]
        break
print('Mediana :      {:1.2f}\t'.format(mediana))




"""4-1_quartile"""
quartile_1= (tot+1)/4
flag=0
for i in range(0, len(Fk)):
    if quartile_1<= Fk[i]:
        quartile_1=k[i]
        break
print('1_quartile:          {}\t'.format(quartile_1))

"""4-3_quartile"""

quartile_3= 3* ((tot+1)/4)
flag=0
for i in range(0, len(Fk)):
    if quartile_3<= Fk[i]:
        quartile_3=k[i]
        break
print('3_quartile:          {}\t\n'.format(quartile_3))


print('istogramma')
"""altezze"""
hk=[]
for i in range(0, len(freq)):
    hk.append(0)
j=0
for i in range(0, len(hk)):
    hk[i]=(Nk[i])/(k[j+1]-k[j]) 
    j+=1
print('akbk:  {:1.2f} {:1.2f} {:1.2f}  {:1.2f}  {:1.2f} {:1.2f}  {:1.2f} {:1.2f}          \t' .format(*k))
print('-------------------------------------------')  
print('Nk:    {:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f}  {:1.2f} \t'.format(*Nk))
print('pk:    {:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f}\t'.format(*pk))
vector=[]
for i in range(0, len(freq)):
    vector.append(0)
j=0
for i in range(0, len(hk)):
     vector[i]= k[j+1]-k[j]
     j+=1
print('-------------------------------------------')  
print('bk-ak: {:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f}\t'.format(*vector))
print('Hk:    {:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f}\t'.format(*hk))




"""6 media approssimata"""

w_k=[]
for i in range(0, len(freq)):
    w_k.append(0)

for i in range(0, len(rang)-1):
    w_k[i]=((rang[i+1]+rang[i])/2)
print('-------------------------------------------')  
print('wk_: {:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f}\t'.format(*w_k))

print('pk*wk_: ',end =" ")
for i in range(0, len(rang)-1):
    print('{:1.3f}'.format(w_k[i]*pk[i]),end =" ")
print('')


print('pk*wk_2: ',end =" ")
for i in range(0, len(rang)-1):
    print('{:1.3f}'.format(np.power(w_k[i],2)*pk[i]),end =" ")
print('')




m_x=0
for i in range(0, len(w_k)):
    m_x+=(w_k[i]*Nk[i]) 

m_x=(1/tot)*m_x
print('Media approssimata:          {:1.2f}\t'.format(m_x))


"""7 varianza approssimata"""

s_x2=0
for i in range(0, len(w_k)):
   s_x2+=(np.power((w_k[i]-m_x),2))*Nk[i]
s_x2=(1/tot)*s_x2
print('Varianza approssimata:          {:1.2f}\t'.format(s_x2))