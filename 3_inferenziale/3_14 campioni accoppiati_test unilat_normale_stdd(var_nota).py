# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019y

@author: mirco
"""
"""intervallo di fiducia per l'attesa""
"""""
import numpy as np
import tavole

arrx=np.array([0.61,0.90,2.76,1.31,3.33,
               2.08,1.42,-0.67,2.22,3.28])
n=len(arrx)
arry=np.array([0.80,2.28,1.11,-1.26,0.70,1.26,
               0.42,2.24,1.58,-0.21,-0.26,-2.02])
m=len(arry)
alfa=0.05
varx=1
vary=1

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

print('')
"""4_Gauss"""
normalfa=1-(alfa)
print('normalfa:     {:1.3f}    \t'.format(normalfa))
flag=0
for i in range(0,30):
    if flag==0:
        for j in range(0,10):
            if flag==0:
                a=(normstd[i,j]*1000)
                if normalfa==((int(a))/1000):
                    qnormale=(j/100)+(i/10)
                    flag=1
                    #kprint(i,j,normstd[i,j])
print('gauss:     {:1.2f}  \t'.format(qnormale))

print('------------------------------------------')

print('2 Test unilaterale di norm stdd di gauss di livello alfa')

To=((medx-medy)/(np.sqrt((varx/n)+(vary/m))))
print('Uo:                     {:1.2f}  \t'.format(To))
print('quantile normale: {:1.2f}  \t'.format(qnormale))

if To<qnormale: 
    print('accetto Ho')
else: 
    print('rifiuto Ho')

print('')
print('------------------------------------------')
print('2 Test unilaterale di student di livello alfa')
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



varcx=(n/(n-1))*(varx)
print('Varianza campionaria x:             {:1.3f}\t'.format(varcx))

varcy=(m/(m-1))*(vary)
print('Varianza campionaria y:             {:1.3f}\t'.format(varcy))

print('------------------------------------------')
print('')

varcomb=((n-1)*varcx+(m-1)*varcy)/(n+m-2)
print('Varianza combinata:             {:1.3f}\t'.format(varcomb))
devcomb=np.sqrt(varcomb)
print('Dev stdd combinata:             {:1.3f}\t'.format(devcomb))
print('')
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


print('numerat:                     {:1.3f}  \t'.format(medx-medy))
print('denominat:                     {:1.3f}  \t'.format(devcomb*np.sqrt((1/n)+(1/m))))
To=((medx-medy)/(devcomb *( np.sqrt((1/n)+(1/m)))))
print('To:                     {:1.3f}  \t'.format(To))
print('quantile student: {:1.3f}  \t'.format(student))

if To<student: 
    print('accetto Ho')
else: 
    print('rifiuto Ho')
