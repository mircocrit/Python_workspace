# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019y

@author: mirco
"""
"""intervallo di fiducia per l'attesa""
"""""
import numpy as np
import tavole

arr=np.array([9.0,12.0,11.0,7.5,10.2,9.8,13.0,12.0,12.5,10.4])
n=len(arr)
alfa=0.05

print('Intervallo di fiducia di livello α per la media')
"""1_media """
i=0
sum=0
while i<n:
    sum+=arr[i]
    i=i+1
med=(1/n)*sum
print('Media:                {:1.3f}\t'.format(med))

"""2_media con i quadrati"""
i=0
sumq=0
while i<n:
    sumq+=arr[i]**2
    i=i+1
sumq=(1/n)*sumq
print('Media con quadrati:      {:1.3f}\t'.format(sumq))
print('Media al quadrato:             {:1.3f}\t'.format(med**2))
varc=(n/(n-1))*(sumq-(med**2))
print('Varianza campionaria:             {:1.3f}\t'.format(varc))


"""3_deviazione standard"""
devstdd=np.sqrt(varc)
print('Deviazione standard camp:     {:1.3f}\t'.format(devstdd))
print('')
"""4_Student"""
studalfa=1-(alfa/2)
print('studalfa:     {:1.3f}    n-1:   {:1.0f} \t'.format(studalfa,n-1))
i=n-2
if studalfa==0.950:    j=0
elif studalfa==0.975:    j=1
elif studalfa==0.990:    j=2
elif studalfa==0.995:    j=3

student= studen[i,j]
print('student:     {:1.5f}  \t'.format(student))

print('------------------------------------------')

print('2 Test bilaterale di student di livello alfa')
med_o=10
print('uo:             {}'.format(med_o))
To=((med-med_o)/devstdd)*np.sqrt(n)
print('|To|:                     {:1.3f}  \t'.format(np.abs(To)))
print('quantile student: {:1.3f}  \t'.format(student))

if np.abs(To)<student: 
    print('accetto Ho')
else: 
    print('rifiuto Ho')

"""3__calcolabilita test alfa di s"""


