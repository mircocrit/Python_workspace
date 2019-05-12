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


arrl=np.array([14.00, 5.99,26.35,35.95,15.95,24.95,19.95,32.95,59.00,9.95,
               69.95,61.35,14.95,12.95,16.95,10.95,57.35,29.95,5.95 ,41.95,
               66.95,19.85,11.95,15.95,50.25,74.65,68.00,69.95])

rang=np.array([5.455 , 15.455, 25.455, 35.455, 45.455, 55.455, 65.455, 75.455])

"""1_media """
n=len(arrl)
i=0
buf=0
sum=0
while i<n:
    sum+=arrl[i]
    i=i+1
    if i%10==0:         
        print(sum-buf)
        buf=sum
print('sum:{:1.4f}\t'.format(sum))
med=(1/n)*sum
print('Media:                {:1.2f}\t'.format(med))

arrl.sort()
print('array ordinato:\n{} {} {} {}  {} {} {} {} {} {} \n  {} {} {} {}  {} {} {} {} {} {} \n {} {} {} {}  {} {} {} {}\t' .format(*arrl))

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

print('k:{} {} {} {}  {} {} {} {} \t' .format(*k))

print('------------------------------------')
print('Nk   {}   {}   {}   {}   {}  {}   {}    \t'.format(*Nk))
Fk=[]
for i in range(0, len(k)):
    Fk.append(0)
    
Fk[0]=Nk[0]
for i in range(1, len(Nk)):
    Fk[i]=Nk[i]+Fk[i-1]
print('Fk   {}   {}   {}   {}   {} {}   {} \t'.format(*Fk))
print('------------------------------------')

pk=copy.copy(Nk)

for i in range(0, len(Nk)):
    pk[i]= pk[i]/Fk[len(freq)-1]    
print('pk  {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f}\t'.format(*pk))

fk=copy.copy(Fk)
for i in range(0, len(Fk)):
    fk[i]= fk[i]/ Fk[len(freq)-1]
print('fk  {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} \t\n'.format(*fk))


n=len(arrl)
tot=np.sum(freq)

  




"""2_range"""
print('Range:                {:1.2f}\t\n'.format(arrl[len(arrl)-1]-arrl[0]))


"""3-mediana pari"""

print('Tot (pari):          {}\t'.format(tot))

mediana=((tot)/2)
print('Quantile mediana pari:      {}\t'.format(mediana))
mediana=arrl[int(mediana-1)] + arrl[int(mediana)]
mediana=mediana/2

print('Mediana :      {:1.3f}\t'.format(mediana))




"""4-1_quartile pari"""
quartile_1= (tot+1)/4
quartile_1=arrl[int(quartile_1-1)] + arrl[int(quartile_1)]
quartile_1=quartile_1/2
print('1_quartile:          {:1.3f}\t'.format(quartile_1))

"""4-3_quartile pari"""

quartile_3= 3*((tot+1)/4)
quartile_3=arrl[int(quartile_3-1)] + arrl[int(quartile_3)]
quartile_3=quartile_3/2
print('3_quartile:          {:1.3f}\t\n'.format(quartile_3))


print('istogramma')
"""altezze"""
hk=[]
for i in range(0, len(freq)):
    hk.append(0)
j=0
for i in range(0, len(hk)):
    hk[i]=(Nk[i])/(k[j+1]-k[j]) 
    j+=1
print('akbk:  {} {} {}  {}  {} {}  {} {}          \t' .format(*k))
print('-------------------------------------------')  
print('Nk:    {} {} {} {} {} {} {}  \t'.format(*Nk))
print('pk:    {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f}\t'.format(*pk))
vector=[]
for i in range(0, len(freq)):
    vector.append(0)
j=0
for i in range(0, len(hk)):
     vector[i]= k[j+1]-k[j]
     j+=1
print('-------------------------------------------')  
print('bk-ak: {:1.0f} {:1.0f} {:1.0f} {:1.0f} {:1.0f} {:1.0f} {:1.0f}\t'.format(*vector))
print('Hk:    {:1.1f} {:1.1f} {:1.1f} {:1.1f} {:1.1f} {:1.1f} {:1.1f}\t'.format(*hk))




"""6 media approssimata"""

w_k=[]
for i in range(0, len(freq)):
    w_k.append(0)

for i in range(0, len(rang)-1):
    w_k[i]=((rang[i+1]+rang[i])/2)
print('-------------------------------------------')  
print('wk_: {} {} {} {} {} {} {}\t'.format(*w_k))

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
    print(w_k[i]*Nk[i])
    m_x+=(w_k[i]*Nk[i]) 
print('sum: {} '.format(m_x))
m_x=(1/tot)*m_x
print('Media approssimata:          {:1.2f}\t'.format(m_x))


"""7 varianza approssimata"""

"""_media con i quadrati"""

sumq=0
for i in range(0, len(w_k)):
    print((np.power((w_k[i]),2))*Nk[i])
    sumq+=(np.power((w_k[i]),2))*Nk[i]
print('sumq: {} '.format(sumq))
sumq=(1/tot)*sumq
print('sumq/tot: {} '.format(sumq))


s_x2=sumq-(m_x**2)
print('Varianza approssimata:          {:1.2f}\t'.format(s_x2))