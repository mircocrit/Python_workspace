
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019

@author: mirco
"""
"""1__intervallo di fiducia per l'attesa""
"""""
import numpy as np

arr=np.array([4.09,4.56,5.01,5.49,4.82,5.56,3.95,4.04,2.63,
              3.78,3.58,4.52,4.86,3.65,4.44,4.62,3.97,3.63])
n=len(arr)
alfa=0.05
var=1

print('1: intervallo di fiducia per attesa')
"""1_media """
i=0
sum=0
while i<n:
    sum+=arr[i]
    i=i+1
med=(1/n)*sum
print('Media:                {:1.3f}\t'.format(med))


print('Varianza :             {:1.3f}\t'.format(var))

"""3_deviazione standard"""
devstdd=np.sqrt(var)
print('Deviazione standard :     {:1.3f}\t'.format(devstdd))
print('')

"""4_Gauss"""
normalfa=1-(alfa/2)
print('normalfa:     {:1.3f}    n-1:   {:1.0f} \t'.format(normalfa,n-1))
qnormale=1.96
print('gauss:     {:1.5f}  \t'.format(qnormale))

"""5_delta"""
delta=((devstdd)/(np.sqrt(n)))*qnormale
print('Delta:      {:1.3f}\t'.format(delta))
print('Intervallo:      {:1.3f} +/- {:1.3f} \t'.format(med,delta))

print('--------------------------------------------')
print('2_Test bilaterale di gauss di livello alfa')

"""2__test bilaterale di gauss di livello alfa"""
qnormale=1.96
med_o=4
print('uo:             {}'.format(med_o))
Uo=((med-med_o)/devstdd)*np.sqrt(n)
print('Uo:                     {:1.3f}  \t'.format(Uo))
print('quantile normale gauss: {:1.3f}  \t'.format(qnormale))
if Uo<qnormale: 
    print('accetto Ho')
else: 
    print('rifiuto Ho')
    
print('--------------------------------------------')
print('3 significatività test alfa di s')
"""3__significatività test alfa di s"""
print('Uo:                     {:1.3f}  \t'.format(np.abs(Uo)))
fiUo=0.88877
print('norm stdd(Uo):                 {:1.3f}  \t'.format(fiUo))
alfas=2*(1-fiUo)
print('alfas:                  {:1.3f}  \t'.format(alfas))





