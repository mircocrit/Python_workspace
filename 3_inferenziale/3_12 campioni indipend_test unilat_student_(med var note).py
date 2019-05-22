# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019y

@author: mirco
"""
"""intervallo di fiducia per l'attesa""
"""""
import numpy as np
import tavole

n=11
medx=1.36
varx=0.22

m=9
medy=0.7
vary=0.03

alfa=0.01

print('Media1:             {:1.2f}   Varianza1 {:1.2f}\t'.format(medx,varx))
print('Media2:             {:1.2f}   Varianza2 {:1.2f}\t'.format(medy,vary))
print('------------------------------------------')
"""4_Student"""

studalfa=1-alfa
print('studalfa:     {:1.3f}    n-1:   {:1.0f} \t'.format(studalfa,n+m-2))
i=n+m-3
if studalfa==0.950:    j=0
elif studalfa==0.975:    j=1
elif studalfa==0.990:    j=2
elif studalfa==0.995:    j=3

student= studen[i,j]
print('student:     {:1.5f}  \t'.format(student))

print('------------------------------------------')
varcomb=((n-1)*varx+(m-1)*vary)/(n+m-2)
print('Varianza combinata:             {:1.3f}\t'.format(varcomb))
devcomb=np.sqrt(varcomb)
print('Dev stdd combinata:             {:1.3f}\t'.format(devcomb))





print('2 Test unilaterale di student di livello alfa')

To=((medx-medy)/(devcomb *( np.sqrt((1/n)+(1/m)))))
print('To:                     {:1.3f}  \t'.format(To))
print('quantile student: {:1.3f}  \t'.format(student))

if To<student: 
    print('accetto Ho')
else: 
    print('rifiuto Ho')

