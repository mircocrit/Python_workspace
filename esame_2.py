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


arrl=np.array([0.00 ,0.01, 0.01, 0.02, 0.03, 0.04, 0.05, 0.09, 0.11, 0.13,
               0.16, 0.19, 0.28, 0.31, 0.35, 0.41, 0.47, 0.48, 0.48, 0.53,
               0.54, 0.56, 0.57, 0.57, 0.58, 0.72, 0.75, 0.77, 0.79, 0.82,
               0.82, 0.84, 0.85, 0.88, 0.89, 0.91, 0.91, 0.92, 0.93, 0.94,
               0.95, 0.96, 0.97, 0.99, 0.99, 1.00, 1.00, 1.00, 1.00, 1.00])
rang=np.array([0,0.1,0.2,0.5,0.8,0.9,1.0])

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

print('k:{} {} {} {}  {} {} {} \t' .format(*k))

print('------------------------------------')
print('Nk   {}   {}   {}   {}   {}  {}  \t'.format(*Nk))
Fk=[]
for i in range(0, len(k)):
    Fk.append(0)
    
Fk[0]=Nk[0]
for i in range(1, len(Nk)):
    Fk[i]=Nk[i]+Fk[i-1]
print('Fk   {}   {}   {}   {}   {}   {}\t'.format(*Fk))
print('------------------------------------')

pk=copy.copy(Nk)

for i in range(0, len(Nk)):
    pk[i]= pk[i]/Fk[len(freq)-1]    
print('pk  {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f}\t'.format(*pk))

fk=copy.copy(Fk)
for i in range(0, len(Fk)):
    fk[i]= fk[i]/ Fk[len(freq)-1]
print('fk  {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} \t\n'.format(*fk))


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
print('Tot (pari):          {}\t'.format(tot))

mediana=((tot+1)/2)
print('Quantile mediana pari:      {}\t'.format(mediana))
if mediana%2==0:##tot dispari
    mediana= arrl[mediana]
else:##tot pari
    print('___{:1.2f},{:1.2f}'.format(arrl[int(mediana)-1],arrl[int(mediana)]))
    mediana=(arrl[int(mediana)-1]+arrl[int(mediana)])/2
print('Mediana :      {:1.3f}\t'.format(mediana))



"""4-1_quartile"""
quartile_1= (tot+1)/4
print('Quantile quartile_1 pari:      {}\t'.format(quartile_1))
if quartile_1%4==0:
    quartile_1=arrl[quartile_1]
else:
    print('___{:1.2f},{:1.2f}'.format(arrl[int(quartile_1)-1],arrl[int(quartile_1)]))
    quartile_1=(arrl[int(quartile_1)-1]+arrl[int(quartile_1)])/2
print('1_quartile:          {:1.3f}\t'.format(quartile_1))

"""4-3_quartile"""

quartile_3= 3* ((tot+1)/4)
print('Quantile quartile_3 pari:      {}\t'.format(quartile_3))
if quartile_3%4==0:    
    quartile_3=arrl[quartile_3]
else:
    print('___{:1.2f},{:1.2f}'.format(arrl[int(quartile_3)-1],arrl[int(quartile_3)]))
    quartile_3=(arrl[int(quartile_3)-1]+arrl[int(quartile_3)])/2
print('3_quartile:          {:1.3f}\t\n'.format(quartile_3))


"""5 istogramma"""
"""altezze"""
hk=[]
for i in range(0, len(freq)):
    hk.append(0)
j=0
for i in range(0, len(hk)):
    hk[i]=(Nk[i])/(k[j+1]-k[j]) 
    j+=1


print('istogramma')
print('akbk:  {} {} {}  {}  {} {}  {}         \t' .format(*k))
print('-------------------------------------------')  
print('Nk:    {}     {}    {}    {}    {}    {}  \t'.format(*Nk))
print('pk:    {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f}\t'.format(*pk))
vector=[]
for i in range(0, len(freq)):
    vector.append(0)
j=0
for i in range(0, len(hk)):
     vector[i]= k[j+1]-k[j]
     j+=1
print('-------------------------------------------')  
print('bk-ak: {:1.1f} {:1.1f} {:1.1f} {:1.1f} {:1.1f} {:1.1f} \t'.format(*vector))
print('Hk:    {:1.0f} {:1.0f} {:1.2f} {:1.2f} {:1.0f} {:1.0f}\t'.format(*hk))




"""6 media approssimata"""

w_k=[]
for i in range(0, len(freq)):
    w_k.append(0)

for i in range(0, len(rang)-1):
    w_k[i]=((rang[i+1]+rang[i])/2)
print('-------------------------------------------')  
print('wk_:{:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f} {:1.2f} \t'.format(*w_k))

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
print('Media per dati raggruppati:          {:1.3f}\t'.format(m_x))


"""7 varianza per dati raggruppati"""

s_x2=0
for i in range(0, len(w_k)):
   s_x2+=(np.power((w_k[i]-m_x),2))*Nk[i]
s_x2=(1/tot)*s_x2
print('Varianza approssimata:          {:1.2f}\t'.format(s_x2))