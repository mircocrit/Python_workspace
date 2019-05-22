# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019y

@author: mirco
"""
"""intervallo di fiducia per l'attesa""
"""""
import numpy as np
import tavole

arrx=np.array([9.51,8.39,8.62,9.48,8.85,
               9.29,8.43,9.57,9.30,9.21])
n=len(arrx)
arry=np.array([8.10,8.58,9.05,7.28,7.64,5.83,
               8.61,7.10,6.44,7.43,8.63,7.94])
m=len(arry)
alfa=0.05

  
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

varcomb=((n-1)*varcx+(m-1)*varcy)/(n+m-2)
print('Varianza combinata:             {:1.3f}\t'.format(varcomb))
devcomb=np.sqrt(varcomb)
print('Dev stdd combinata:             {:1.3f}\t'.format(devcomb))

"""4_Student"""

studalfa=1-alfa
print('studalfa:     {:1.3f}    n-1:   {:1.0f} \t'.format(studalfa,n+m-2))
i=n+m-3
if studalfa==0.950:    j=0
elif studalfa==0.975:    j=1
elif studalfa==0.990:    j=2
elif studalfa==0.995:    j=3

student= studen[i,j]
print('student:     {:1.3f}  \t'.format(student))

print('------------------------------------------')

print('2 Test unilaterale di student di livello alfa')
print(medx-medy)
print( np.sqrt((1/n)+(1/m)))
To=((medx-medy)/(devcomb *( np.sqrt((1/n)+(1/m)))))
print('To:                     {:1.3f}  \t'.format(To))
print('quantile student: {:1.3f}  \t'.format(student))

if To<student: 
    print('accetto Ho')
else: 
    print('rifiuto Ho')

