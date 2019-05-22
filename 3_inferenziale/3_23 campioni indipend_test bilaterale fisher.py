# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:48 2019

@author: mirco
"""
"""intervallo di fiducia per l'attesa""
"""""
import numpy as np
import tavole



arrx=np.array([-1.34,1.32,-0.96,0.29,-1.41,0.23,-0.56,-0.32,0.66,1.27])
n=len(arrx)

arry=np.array([4.83,-2.52,-1.79,-2.85,1.45,1.09,1.87,2.03,-2.60])
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

print('')
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


print('2 Test bilaterale di Fisher(no varianza) di livello alfa per varianza')
Fo=varcx/varcy
print('Fo:             {:1.3f}'.format(Fo))

print ('n-1: {}  m-1: {} \t'.format(n-1,m-1))
alfa1=alfa/2

print ('alfa1:     {:1.3f}\t'.format(alfa1))

if alfa1==0.025:    
    i=(n-1)-4               #1 indice
    if   (m-1)==15:    j=11 #2 indice
    elif (m-1)==20:    j=12
    elif (m-1)==30:    j=13
    elif (m-1)==60:    j=14
    else:              j=m-1
    j=j-1
    Fisheralfa2=fisher0975[i,j]
    print(('Fisher alfa/2 parz:             {:1.3f}\n'.format(Fisheralfa2)))   
    Fisheralfa2=1/Fisheralfa2
print(('Fisher alfa/2:             {:1.3f}\n'.format(Fisheralfa2)))

alfa2=(1-(alfa/2))
print ('alfa/2:     {:1.3f}\t'.format(alfa2))

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





