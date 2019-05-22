# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019

@author: mirco
"""
"""intervallo di fiducia per l'attesa""
"""""
import numpy as np
import tavole


arrx=np.array([15,20,21,26,20,14,13,17,22,21,
               24,19,18,22,17,17,19,23,21,22,
               31,14,14,24,24,21,20,25,17,20,
               20])
n=len(arrx)

arry=np.array([18,18,23,19,14,14,14,16,23,21,
               17,21,14,22,17,19,16,9,22,13,
               17,19,16,19,22,11,16,9,19,21,
               13])
m=len(arry)


alfa_bil=0.05
alfa_unil=0.01



"""1_mediax """
i=0
buf=0
sum=0
while i<n:
    sum+=arrx[i]
    i=i+1
    if i%10==0:         
        print(sum-buf)
        buf=sum
print('sum:{:1.4f}\t'.format(sum))
medx=(1/n)*sum
print('Media x:                {:1.3f}\t'.format(medx))


"""1_mediay """
i=0
buf=0
sum=0
while i<m:
    sum+=arry[i]
    i=i+1
    if i%10==0:         
        print(sum-buf)
        buf=sum
print('sum:{:1.4f}\t'.format(sum))
medy=(1/m)*sum
print('Media y:                {:1.3f}\t'.format(medy))


"""2_media con i quadrati_x"""
i=0
sumq=0
buf=0
while i<n:
    sumq+=arrx[i]**2
    i=i+1
    if i%10==0:         
        print(sumq-buf)
        buf=sumq
sumqx=(1/n)*sumq

print('Media con quadrati x:      {:1.3f}\t'.format(sumqx))

"""2_media con i quadrati_y"""
i=0
sumq=0
buf=0
while i<m:
    sumq+=arry[i]**2
    i=i+1
    if i%10==0:         
        print(sumq-buf)
        buf=sumq
sumqy=(1/m)*sumq

print('Media con quadrati y:      {:1.3f}\t'.format(sumqy))

print('')

varx=sumqx-(medx**2)
print('Varianza x :             {:1.3f}\t'.format(varx))
vary=sumqy-(medy**2)
print('Varianza y :             {:1.3f}\t'.format(vary))


print('')
varcx=(n/(n-1))*(varx)
print('Varianza campionaria x:             {:1.3f}\t'.format(varcx))

varcy=(m/(m-1))*(vary)
print('Varianza campionaria y:             {:1.3f}\t'.format(varcy))

print('')


print('------------------------------------------')

print('1 Test bilaterale di Fisher(no varianza) di livello alfa')
Fo=varcx/varcy
print('Fo:             {:1.3f}'.format(Fo))
print ('n-1: {}  m-1: {} \t'.format(n-1,m-1))
alfa1=alfa_bil/2

print ('alfa1:     {:1.3f}\t'.format(alfa1))

if alfa1==0.025:    
    i=(n-1)-4               #1 indice
    if   (m-1)==15:    j=11 #2 indice
    elif (m-1)==20:    j=12
    elif (m-1)==30:    j=13
    elif (m-1)==60:    j=14
    else:              j=n-1
    j=j-1
    Fisheralfa2=fisher0975[i,j]
    print(('Fisheralfa2:             {:1.3f}\n'.format(Fisheralfa2)))   
    Fisheralfa2=1/Fisheralfa2
print(('Fisheralfa2:             {:1.3f}\n'.format(Fisheralfa2)))

alfa2=(1-(alfa_bil/2))
print ('alfa2:     {:1.3f}\t'.format(alfa2))

if alfa2==0.975:
    i=(m-1)-4  
    if   (n-1)==15:     j=11
    elif (n-1)==20:     j=12
    elif (n-1)==30:     j=13
    elif (n-1)==60:     j=14
    else:               j=n-1
    j=j-1
    Fisher1alfa= fisher0975[i,j]

print(('Fisher1alfa:             {}'.format(Fisher1alfa)))
if Fo>Fisheralfa2 and Fo<Fisher1alfa : 
      print('accetto Ho')
else: 
    print('rifiuto Ho')




print('------------------------------------------')

print('2 Test unilaterale di Fisher(no varianza) di livello alfa')

varcomb=((n-1)*varcx+(m-1)*varcy)/(n+m-2)
print('Varianza combinata:             {:1.3f}\t'.format(varcomb))
devcomb=np.sqrt(varcomb)
print('Dev stdd combinata:             {:1.3f}\t'.format(devcomb))

"""4_Student"""

studalfa=1-alfa_unil
print('studalfa:     {:1.3f}    n-1:   {:1.0f} \t'.format(studalfa,n+m-2))
i=n+m-3
if studalfa==0.950:    j=0
elif studalfa==0.975:    j=1
elif studalfa==0.990:    j=2
elif studalfa==0.995:    j=3
if i==59: i=51
student= studen[i,j]
print('student:     {:1.5f}  \t'.format(student))

print('------------------------------------------')

print('2 Test bilaterale di student di livello alfa')

To=((medx-medy)/(devcomb *( np.sqrt((1/n)+(1/m)))))
print('|To|:                     {:1.2f}  \t'.format(np.abs(To)))
print('quantile student: {:1.3f}  \t'.format(student))

if np.abs(To)<student: 
    print('accetto Ho')
else: 
    print('rifiuto Ho')


