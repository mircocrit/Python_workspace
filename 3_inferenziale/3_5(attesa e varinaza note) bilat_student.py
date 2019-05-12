# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019

@author: mirco
"""
"""1__intervallo di fiducia per l'attesa""
"""""
import numpy as np

n=200
alfa=0.01
med=33.57
var=1.723

print('2 Test bilaterale di student di livello alfa')
"""1_media """
print('Media:                {:1.3f}\t'.format(med))
print('Varianza :             {:1.3f}\t'.format(var))

"""3_deviazione standard"""
devstdd=np.sqrt(var)
print('Deviazione standard :     {:1.3f}\t'.format(devstdd))
print('')

"""4_Student"""
studalfa=1-(alfa/2)
print('studalfa:     {:1.3f}    n-1:   {:1.0f} \t'.format(studalfa,n-1))

student=2.58
print('student:(uguale a normale standard)     {:1.5f}  \t'.format(student))


print('--------------------------------------------')

"""2__test bilaterale di student(no varianza) di livello alfa"""
med_o=34
print('uo:             {}'.format(med_o))
To=((med-med_o)/devstdd)*np.sqrt(n)
print('|To|:                     {:1.3f}  \t'.format(np.abs(To)))
print('quantile normale student/gauss: {:1.3f}  \t'.format(student))

if np.abs(To)<student: 
    print('accetto Ho')
else: 
    print('rifiuto Ho')

"""3__calcolabilita test alfa di s"""

