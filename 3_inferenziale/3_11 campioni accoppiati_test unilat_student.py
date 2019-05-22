# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019y

@author: mirco
"""
"""intervallo di fiducia per l'attesa""
"""""
import numpy as np
import tavole

arrx=np.array([36.8,37.9,38.3,38.1,38.3,38.8,36.3,37.7,37.1,36.9,
              37.7,37.5,37.4,39.0,38.6,41.4,37.9,37.5,39.9,38.2,
              38.4,37.7,37.5,36.6,38.0,38.6,39.0,37.6,38.0,39.5])
arry=np.array([37.1,36.1,38.2,39.0,38.4,36.4,36.8,39.3,37.3,37.9,
               37.6,38.4,38.6,37.4,38.3,37.0,35.9,36.0,37.2,39.3,
               36.0,36.6,38.0,38.0,38.7,39.4,37.6,36.1,39.0,36.4])
n=len(arrx)
alfa=0.05

arrz=[]
print('Test unilaterale di livello alfa=0.05')

for i in range(0,len(arrx)):
    arrz.append(0)

for i in range(0,len(arrx)):
    arrz[i]=(arrx[i]-arry[i])
print('Campione Z')
print('  {:1.1f}  {:1.1f}  {:1.1f}   {:1.1f}  {:1.1f}  {:1.1f}  {:1.1f} {:1.1f} {:1.1f}  {:1.1f}    \n  {:1.1f}  {:1.1f}  {:1.1f}   {:1.1f}  {:1.1f}  {:1.1f}  {:1.1f} {:1.1f} {:1.1f}  {:1.1f}    \n  {:1.1f}  {:1.1f}  {:1.1f}   {:1.1f}  {:1.1f}  {:1.1f}  {:1.1f} {:1.1f} {:1.1f}  {:1.1f}    ' .format(*arrz))

n=len(arrz)

  
"""1_media """
i=0
buf=0
sum=0
while i<n:
    sum+=arrz[i]
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
buf=0
while i<n:
    sumq+=arrz[i]**2
    i=i+1
    if i%10==0:         
        print(sumq-buf)
        buf=sumq
sumq=(1/n)*sumq

print('Media con quadrati:      {:1.3f}\t'.format(sumq))
var=sumq-(med**2)
print('Varianza :             {:1.3f}\t'.format(var))
varc=(n/(n-1))*(var)
print('Varianza campionaria:             {:1.3f}\t'.format(varc))


"""3_deviazione standard"""

devstdd=np.sqrt(varc)
print('Deviazione standard camp:     {:1.3f}\t'.format(devstdd))
print('')


print('------------------------------------------')
print('2 Test unilaterale di student di livello alfa')

"""4_Student"""

studalfa=1-alfa
print('studalfa:     {:1.3f}    n-1:   {:1.0f} \t'.format(studalfa,n-1))
i=n-2
if studalfa==0.950:    j=0
elif studalfa==0.975:    j=1
elif studalfa==0.990:    j=2
elif studalfa==0.995:    j=3

student= studen[i,j]
print('student:     {:1.5f}  \t'.format(student))
print('')



To=((med)/devstdd)*np.sqrt(n)
print('To:                     {:1.3f}  \t'.format(To))

print('quantile student: {:1.3f}  \t'.format(student))

if To<student: 
    print('accetto Ho')
else: 
    print('rifiuto Ho')

