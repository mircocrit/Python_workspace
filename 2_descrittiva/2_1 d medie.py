# -*- coding: utf-8 -*-
import copy
import numpy as np
from scipy.stats.mstats import gmean


arrl=np.array([5,4,5,4,4,1,5,6,5,4,2,3,7,5,3,3,4,3,4])

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
print('k:  {}  {}  {}   {}  {}  {}  {}\t' .format(*k))
print('------------------------------------')
print('Nk  {}  {}  {}  {}  {}  {}   {}\t'.format(*Nk))
Fk=[]
for i in range(0, len(k)):
    Fk.append(0)
    
Fk[0]=Nk[0]
for i in range(1, len(Nk)):
    Fk[i]=Nk[i]+Fk[i-1]
print('Fk  {} {}  {} {} {}  {}  {}\t'.format(*Fk))
print('------------------------------------')

pk=copy.copy(Nk)

for i in range(0, len(Nk)):
    pk[i]= pk[i]/Fk[len(freq)-1]    
print('pk  {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f}  {:1.3f}  {:1.3f}\t'.format(*pk))

fk=copy.copy(Fk)
for i in range(0, len(Fk)):
    fk[i]= fk[i]/ Fk[len(freq)-1]
print('fk  {:1.3f} {:1.3f} {:1.3f} {:1.3f} {:1.3f}  {:1.3f}  {:1.3f}\t\n'.format(*fk))


n=len(arr)
tot=np.sum(freq)


  
"""1_media """
sum=0
for i in range(0,n):
    sum+=(arr[i]*freq[i])  
med=(1/tot)*sum
print('Media:                {:1.2f}\t'.format(med))


"""2_varianza"""
"""_media con i quadrati"""
sumq=0
for i in range(0,n):
    sumq+=((arr[i]**2)*freq[i])
sumq=(1/tot)*sumq
print(':             {:1.3f}\t'.format(sumq))
var=sumq-(med**2)
print('Varianza:             {:1.2f}\t'.format(var))


"""3_deviazione standard"""
devstdd=np.sqrt(var)
print('Deviazione standard:     {:1.2f}\t'.format(devstdd))



"""4_range"""
print('Range: {:1.2f}\t\n'.format(arr[len(arr)-1]-arr[0]))


"""5-mediana"""
print('Tot (dispari):          {}\t'.format(tot))

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


"""7_media armonica"""

arm=0
for i in range(0, n):
    arm+=((1/arr[i])*freq[i])
arm=tot/arm
print('Media armonica:          {:1.2f}\t'.format(arm))

"""8_media quadratica"""
sumq=0
for i in range(0, n):
    sumq+=freq[i]*(np.power(arr[i],2))
sumq=(1/tot)*sumq
quad=np.sqrt(sumq)
print('Media quadratica:       {:1.2f}\t'.format(quad))

"""9_media geometrica"""

geom=gmean(arrl)

print('Media geometrica:         {:1.2f}\t'.format(geom))











