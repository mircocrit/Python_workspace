# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019

@author: mirco
"""
"""1__intervallo di fiducia per l'attesa""
"""""
import numpy as np
import tavole

arr=np.array([2.23,4.09,3.97,5.57,3.09,3.00,2.85,2.12,3.26,2.11,
              3.10,1.82,2.82,1.99,3.25,1.53,2.99,1.03,3.86,2.45])
n=len(arr)
alfa=0.05

print('1: intervallo di fiducia per attesa')
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


print('--------------------------------------------')

"""2 Test bilaterale di student(no varianza) di livello alfa"""
print('test bilaterale di student(no varianza) di livello alfa')
med_o=3
print('uo:             {}'.format(med_o))
To=((med-med_o)/devstdd)*np.sqrt(n)
print('|To|:                     {:1.3f}  \t'.format(np.abs(To)))
print('quantile normale gauss: {:1.3f}  \t'.format(student))

if np.abs(To)<student: 
    print('accetto Ho')
else: 
    print('rifiuto Ho')

print('--------------------------------------------')
#print('3 significatività test alfa di s')
"""3__significatività test alfa di s"""
"""print('To:                     {:1.3f}  \t'.format(np.abs(To)))
studentTo=2.86093
print('student(To):                 {:1.3f}  \t'.format(studentTo))
alfas=2*(1-studentTo)
print('alfas:                  {:1.3f}  \t'.format(alfas))
"""




