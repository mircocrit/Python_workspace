# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019

@author: mirco
"""
"""intervallo di fiducia per l'attesa""
"""""
import numpy as np
import tavole


n=21
medx=1.09
varx=2.34

m=31
medy=2.22
vary=3.11

alfa_att=0.05
alfa_var=0.01




print('------------------------------------------')



print('3 Test bilaterale di Fisher(no varianza) di livello alfa per varianza')
Fo=varx/vary
print('Fo:             {:1.3f}'.format(Fo))

print ('n-1: {}  m-1: {} \t'.format(n-1,m-1))
alfa1=alfa_att/2

print ('alfa/2:     {:1.3f}\t'.format(alfa1))

if alfa1==0.025:    
    i=(n-1)-4               #1 indice
    if   (m-1)==15:    j=11 #2 indice
    elif (m-1)==20:    j=12
    elif (m-1)==30:    j=13
    elif (m-1)==60:    j=14
    else:              j=n-1
    j=j-1
    Fisheralfa2=fisher0975[i,j]
    print(('Fisher alfa/2 parz:             {:1.3f}\n'.format(Fisheralfa2)))   
    Fisheralfa2=1/Fisheralfa2
print(('Fisher alfa/2:             {:1.3f}\n'.format(Fisheralfa2)))

alfa2=(1-(alfa_att/2))
print ('1-alfa/2:     {:1.3f}\t'.format(alfa2))

if alfa2==0.975:
    i=(m-1)-4  
    if   (n-1)==15:     j=11
    elif (n-1)==20:     j=12
    elif (n-1)==30:     j=13
    elif (n-1)==60:     j=14
    else:               j=n-1
    j=j-1
    Fisher1alfa= fisher0975[i,j]

print(('Fisher 1-alfa/2:             {:1.3f}'.format(Fisher1alfa)))
if Fo>Fisheralfa2 and Fo<Fisher1alfa : 
      print('accetto Ho')
else: 
    print('rifiuto Ho')

print('------------------------------')
print('')
print('2 Test bilaterale di Fisher(no varianza) di livello alfa per attesa')

varcomb=((n-1)*varx+(m-1)*vary)/(n+m-2)
print('Varianza combinata:             {:1.3f}\t'.format(varcomb))
devcomb=np.sqrt(varcomb)
print('Dev stdd combinata:             {:1.3f}\t'.format(devcomb))

print('------------------------------')
"""4_Student"""

studalfa=1-alfa_var/2
print('studalfa:     {:1.3f}    n-1:   {:1.0f} \t'.format(studalfa,n+m-2))
i=n+m-3
if studalfa==0.950:    j=0
elif studalfa==0.975:    j=1
elif studalfa==0.990:    j=2
elif studalfa==0.995:    j=3

student= studen[i,j]
print('student:     {:1.2f}  \t'.format(student))
print('------------------------------')

To=((medx-medy)/(devcomb *(np.sqrt((1/n)+(1/m)))))
print('|To|:                     {:1.2f}  \t'.format(np.abs(To)))
print('quantile student: {:1.3}  \t'.format(student))

if np.abs(To)<student: 
    print('accetto Ho')
else: 
    print('rifiuto Ho')




