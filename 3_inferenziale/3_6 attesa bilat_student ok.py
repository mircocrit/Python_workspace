# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019

@author: mirco
"""
"""intervallo di fiducia per l'attesa""
"""""
import numpy as np

arr=np.array([2.58,0.25,3.96,4.89,3.80,1.42,0.96,7.99,2.47,4.32,
              2.19,0.66,1.37,6.22,1.41,2.56,1.06,1.40,0.45,1.40])
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

7
student=2.093
print('student:     {:1.5f}  \t'.format(student))

"""5_delta"""
delta=((devstdd)/(np.sqrt(n)))*student
print('Delta:      {:1.3f}\t'.format(delta))
print('Intervallo:      {:1.3f} +/- {:1.3f} \t'.format(med,delta))



print('------------------------------------------')

print('2 Test bilaterale di student(no varianza) di livello alfa')
med_o=3
print('uo:             {}'.format(med_o))
To=((med-med_o)/devstdd)*np.sqrt(n)
print('|To|:                     {:1.3f}  \t'.format(np.abs(To)))
print('quantile student: {:1.3f}  \t'.format(student))

if np.abs(To)<student: 
    print('accetto Ho')
else: 
    print('rifiuto Ho')

"""3__calcolabilita test alfa di s"""


