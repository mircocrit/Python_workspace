# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019

@author: mirco
"""
"""intervallo di fiducia per l'attesa""
"""""
import numpy as np
import tavole

arr=np.array([2.05,1.42,6.18,6.69,4.47,5.36,3.47,6.74,5.19,0.91,
              3.22,9.50,5.85,3.41,5.66])



n=len(arr)
alfa=0.05

print('1: intervallo di fiducia per attesa')
"""1_media """
i=0
buf=0
sum=0
while i<n:
    sum+=arr[i]
    i=i+1
    if i%10==0:         
        print(sum-buf)
        buf=sum
print('sum:{:1.4f}\t'.format(sum))
med=(1/n)*sum
print('Media:                {:1.3f}\t'.format(med))

"""2_media con i quadrati"""
i=0
sumq=0
while i<n:
    print(arr[i]**2)
    sumq+=arr[i]**2
    i=i+1
print('sumq: {}'.format(sumq))
sumq=(1/n)*sumq
print('Media con quadrati:      {:1.3f}\t'.format(sumq))
print('Varianza:             {:1.3f}\t'.format((sumq-(med**2))))
varc=(n/(n-1))*(sumq-(med**2))
print('Varianza campionaria:             {:1.3f}\t'.format(varc))

"""3_deviazione standard"""
devstdd=np.sqrt(varc)
print('Deviazione standard camp:     {:1.3f}\t'.format(devstdd))
print('')

"""4_Student"""

studalfa=1-(alfa/2)
i=n-2
if studalfa==0.950:    j=0
elif studalfa==0.975:    j=1
elif studalfa==0.990:    j=2
elif studalfa==0.995:    j=3

print('studalfa:     {:1.3f}    n-1:   {:1.0f} \t'.format(studalfa,n-1))
student=studen[i,j]
print('student:     {:1.5f}  \t'.format(student))

"""5_delta"""
delta=((devstdd)/(np.sqrt(n)))*student
print('Delta:      {:1.3f}\t'.format(delta))
print('Intervallo:      {:1.3f} +/- {:1.3f} \t'.format(med,delta))
    

